import numpy as np

sharpening_kernel = np.array([
    [0, -1, 0],
    [-1, 5, -1],
    [0, -1, 0],
])


# pads image with zeros according to the size of the kernel
def pad_image(image: np.array, pad_nr) -> np.array:
    res: np.array
    if image.ndim == 3:
        res = np.pad(image, ((pad_nr, pad_nr), (pad_nr, pad_nr), (0, 0)), 'constant')
    else:
        res = np.pad(image, pad_nr, 'constant')
    return res


# applies convolution with given kernel to an RGB picture
def conv_rgb(image: np.array, kernel: np.array, img_size) -> np.array:
    ker_size = kernel.shape[0]
    res = np.zeros((img_size[0], img_size[1], 3))
    for i in range(0, 3):
        for j in range(0, img_size[0]):
            for k in range(0, img_size[1]):
                view = (image[j:j + ker_size, k:k + ker_size, i] * kernel)
                res[j, k, i] = np.sum(view)
    return res


# applies convolution with given kernel to a grayscale picture
def conv_grayscale(image: np.array, kernel: np.array, img_size) -> np.array:
    ker_size = kernel.shape[0]
    res = np.zeros((img_size[0], img_size[1]))
    for j in range(0, img_size[0]):
        for k in range(0, img_size[1]):
            view = (image[j:j + ker_size, k:k + ker_size] * kernel)
            res[j, k] = np.sum(view)
    return res


# applies a filter to image by convolution using given kernel
# returns filtrated image
def apply_conv(image: np.array, kernel: np.array) -> np.array:
    assert image.ndim in [2, 3]
    assert kernel.ndim == 2
    assert kernel.shape[0] == kernel.shape[1]

    kernel = np.flip(kernel, 0)
    kernel = np.flip(kernel, 1)
    pad_nr = kernel.shape[0] // 2
    image_pad = pad_image(image, pad_nr)
    img_size = (image.shape[0], image.shape[1])

    res: np.array
    if image.ndim == 2:
        res = conv_grayscale(np.array(image_pad, dtype=np.float), kernel, img_size)
    else:
        res = conv_rgb(np.array(image_pad, dtype=np.float), kernel, img_size)

    res = np.clip(res, 0, 255)
    return np.array(res, dtype=np.uint8)


# rotates image by 90 degrees to the right
def rotation(image: np.array) -> np.array:
    return np.rot90(image, 1, (1, 0)).astype(np.uint8)


# returns mirrored image
def mirror(image: np.array) -> np.array:
    return np.flip(image, 1).astype(np.uint8)


# returns an inverse image
def inverse(image: np.array) -> np.array:
    return np.array(255 - image).astype(np.uint8)


# returns image in the grayscale
def bw(image: np.array) -> np.array:
    if image.ndim == 3:
        res = np.array((image[:, :, :3] * [0.299, 0.587, 0.114]).sum(axis=2)).astype(np.uint8)
        return res
    return image


# lightens image by given percent value
def lighten(image: np.array, percentage: int = 10) -> np.array:
    val = 1 + (percentage / 100)
    res = np.clip(image * val, 0, 255)
    return res.astype(np.uint8)


# darkens image by given percent value
def darken(image: np.array, percentage: int = 10) -> np.array:
    return np.array(image * (percentage / 100)).astype(np.uint8)

