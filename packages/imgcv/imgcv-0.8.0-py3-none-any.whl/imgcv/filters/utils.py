import numpy as np


def pad_image(img, filter_size):
    """Pad the image with zeros.

    Args:
        img (np.ndarray): Input Image array
        filter_size (Tuple[int, int]): Size of the filter.

    Returns:
        np.ndarray: Padded image array.
    """
    pad_height = filter_size[0] // 2
    pad_width = filter_size[1] // 2

    return np.pad(
        img, ((pad_height, pad_height), (pad_width, pad_width)), mode="constant"
    )


def apply_convolution(img, kernels, seperate, take_mean=False):
    """Apply convolution operation to the image.

    Args:
        img (np.ndarray): Input Image array
        kernels (List[np.ndarray, np.ndarray]): List of kernels to apply.
        seperate (bool): If True, apply the kernels seperately in x and y direction respectively.

    Raises:
        ValueError: If kernels is not a list of length 1 or 2.
        ValueError: If seperate is not a boolean value.
        ValueError: If both kernels are not of same shape.

    Returns:
        np.ndarray: Image array after applying convolution.
    """

    # kernels must be a list
    if not isinstance(kernels, list):
        raise ValueError("kernels should be a list")

    # kernels should be a list of length 1 or 2
    if len(kernels) not in [1, 2]:
        raise ValueError("Kernels should be a  of length 2")

    # seperate should be a boolean value
    if not isinstance(seperate, bool):
        raise ValueError("seperate should be a boolean value")

    # if kernels are of length 2, they should be applied seperately. Thus both kernels should be of same shape
    if len(kernels) == 2 and seperate:
        if kernels[0].shape != kernels[1].shape:
            raise ValueError("Both kernels should be of same shape")

    # if kernels are of length 1 or 2, padding is done based on the first kernel. Because if there is second kernel then it will be of same shape as first kernel
    padded_img = pad_image(img, kernels[0].shape)

    final_img = np.zeros(img.shape)
    for row in range(img.shape[0]):
        for col in range(img.shape[1]):
            # if kernels are of length 1, then apply the kernel directly
            if len(kernels) == 1:
                kernel = kernels[0]
                window = padded_img[
                    row : row + kernel.shape[0], col : col + kernel.shape[1]
                ]
            # if kernels are of length 2 and seperate is True, then apply the kernels seperately in x and y direction
            elif len(kernels) == 2 and seperate:
                kernel_x, kernel_y = kernels
                window = padded_img[
                    row : row + kernel_x.shape[0], col : col + kernel_x.shape[1]
                ]
                result1 = np.sum(window * kernel_x)
                result2 = np.sum(window * kernel_y)

                result = np.abs(result1) + np.abs(result2)

            if take_mean:  # useful for box filter
                result = np.mean(window * kernel)
            if not take_mean and len(kernels) == 1:
                result = np.sum(window * kernel)
            result = np.clip(result, 0, 255)
            final_img[row, col] = np.round(result)

    return final_img.astype(np.uint8)
