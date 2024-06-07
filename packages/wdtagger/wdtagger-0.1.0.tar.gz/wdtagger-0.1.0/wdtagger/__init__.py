import os
from collections import OrderedDict

import huggingface_hub
import numpy as np
import onnxruntime as rt
import pandas as pd
import rich
from PIL import Image

console = rich.get_console()

HF_TOKEN = os.environ.get("HF_TOKEN", "")
MODEL_FILENAME = "model.onnx"
LABEL_FILENAME = "selected_tags.csv"


def load_labels(dataframe) -> list[str]:
    name_series = dataframe["name"]
    kaomojis = [
        "0_0",
        "(o)_(o)",
        "+_+",
        "+_-",
        "._.",
        "<o>_<o>",
        "<|>_<|>",
        "=_=",
        ">_<",
        "3_3",
        "6_9",
        ">_o",
        "@_@",
        "^_^",
        "o_o",
        "u_u",
        "x_x",
        "|_|",
        "||_||",
    ]
    name_series = name_series.map(
        lambda x: x.replace("_", " ") if x not in kaomojis else x
    )
    tag_names = name_series.tolist()
    rating_indexes = list(np.where(dataframe["category"] == 9)[0])
    general_indexes = list(np.where(dataframe["category"] == 0)[0])
    character_indexes = list(np.where(dataframe["category"] == 4)[0])

    return tag_names, rating_indexes, general_indexes, character_indexes


class Result:
    def __init__(
        self, preds, sep_tags, general_threshold=0.35, character_threshold=0.9
    ):

        tag_names = sep_tags[0]
        rating_indexes = sep_tags[1]
        general_indexes = sep_tags[2]
        character_indexes = sep_tags[3]
        labels = list(zip(tag_names, preds[0].astype(float)))

        # Ratings
        ratings_names = [labels[i] for i in rating_indexes]
        rating_data = dict(ratings_names)
        rating_data = OrderedDict(
            sorted(rating_data.items(), key=lambda x: x[1], reverse=True)
        )

        # General tags
        general_names = [labels[i] for i in general_indexes]
        general_tag = [x for x in general_names if x[1] > general_threshold]
        general_tag = OrderedDict(sorted(general_tag, key=lambda x: x[1], reverse=True))

        # Character tags
        character_names = [labels[i] for i in character_indexes]
        character_tag = [x for x in character_names if x[1] > character_threshold]
        character_tag = OrderedDict(
            sorted(character_tag, key=lambda x: x[1], reverse=True)
        )

        self.general_tag_data = general_tag
        self.character_tag_data = character_tag
        self.rating_data = rating_data

    @property
    def general_tags(self):
        return tuple(self.general_tag_data.keys())

    @property
    def character_tags(self):
        return tuple(self.character_tag_data.keys())

    @property
    def rating(self):
        return max(self.rating_data, key=self.rating_data.get)

    @property
    def general_tags_string(self) -> str:
        string = sorted(
            self.general_tag_data.items(),
            key=lambda x: x[1],
            reverse=True,
        )
        string = [x[0] for x in string]
        string = ", ".join(string)

        return string

    @property
    def character_tags_string(self) -> str:
        string = sorted(
            self.character_tag_data.items(),
            key=lambda x: x[1],
            reverse=True,
        )
        string = [x[0] for x in string]
        string = ", ".join(string)
        return string

    def __str__(self) -> str:
        def get_tag_with_rate(tag_dict):
            return ", ".join([f"{k} ({v:.2f})" for k, v in tag_dict.items()])

        result = f"General tags: {get_tag_with_rate(self.general_tag_data)}\n"
        result += f"Character tags: {get_tag_with_rate(self.character_tag_data)}\n"
        result += f"Rating: {self.rating} ({self.rating_data[self.rating]:.2f})"
        return result


class Tagger:
    def __init__(
        self,
        model_repo="SmilingWolf/wd-swinv2-tagger-v3",
        cache_dir=None,
        hf_token=HF_TOKEN,
    ):
        self.model_target_size = None
        self.cache_dir = cache_dir
        self.hf_token = hf_token
        self.load_model(model_repo, cache_dir, hf_token)

    def load_model(self, model_repo, cache_dir=None, hf_token=None):
        with console.status("Loading model..."):
            csv_path = huggingface_hub.hf_hub_download(
                model_repo,
                LABEL_FILENAME,
                cache_dir=cache_dir,
                use_auth_token=hf_token,
            )
            model_path = huggingface_hub.hf_hub_download(
                model_repo,
                MODEL_FILENAME,
                cache_dir=cache_dir,
                use_auth_token=hf_token,
            )

            tags_df = pd.read_csv(csv_path)
            self.sep_tags = load_labels(tags_df)

            model = rt.InferenceSession(model_path)
            _, height, _, _ = model.get_inputs()[0].shape
            self.model_target_size = height
            self.model = model

    def prepare_image(self, image):
        if image.mode != "RGBA":
            image = image.convert("RGBA")
        target_size = self.model_target_size
        canvas = Image.new("RGBA", image.size, (255, 255, 255))
        canvas.alpha_composite(image)
        image = canvas.convert("RGB")

        # Pad image to square
        image_shape = image.size
        max_dim = max(image_shape)
        pad_left = (max_dim - image_shape[0]) // 2
        pad_top = (max_dim - image_shape[1]) // 2

        padded_image = Image.new("RGB", (max_dim, max_dim), (255, 255, 255))
        padded_image.paste(image, (pad_left, pad_top))

        # Resize
        if max_dim != target_size:
            padded_image = padded_image.resize(
                (target_size, target_size),
                Image.BICUBIC,
            )

        # Convert to numpy array
        image_array = np.asarray(padded_image, dtype=np.float32)

        # Convert PIL-native RGB to BGR
        image_array = image_array[:, :, ::-1]

        return np.expand_dims(image_array, axis=0)

    def tag(
        self,
        image,
        general_threshold=0.35,
        character_threshold=0.9,
    ):
        with console.status("Tagging..."):
            image = self.prepare_image(image)
            image_array = np.asarray(image, dtype=np.float32)
            image_array = image_array[:, :, ::-1]  # Convert PIL-native RGB to BGR

            image_array = np.expand_dims(image_array, axis=0)
            input_name = self.model.get_inputs()[0].name
            label_name = self.model.get_outputs()[0].name

            preds = self.model.run([label_name], {input_name: image_array[0]})[0]
            result = Result(
                preds, self.sep_tags, general_threshold, character_threshold
            )
            return result


__all__ = ["Tagger"]

if __name__ == "__main__":
    tagger = Tagger()
    image = Image.open("./tests/images/赤松楓.9d64b955.jpeg")
    result = tagger.tag(image, character_threshold=0.8, general_threshold=0.35)
    print(result)
