import numpy as np
from PIL import Image


def read_image(file_name: str) -> np.array:
    return np.asarray(Image.open(file_name), dtype=np.uint8)


def image_from_array(array, mode):
    return Image.fromarray(array, mode=mode)


def save_image(array, file_path):
    mode = 'RGB'
    if array.ndim == 2:
        mode = 'L'
    image_from_array(array, mode=mode).save(file_path)
