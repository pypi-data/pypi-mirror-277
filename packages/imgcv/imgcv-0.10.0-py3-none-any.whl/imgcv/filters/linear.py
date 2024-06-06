import numpy as np
from imgcv.common import check_image
from imgcv.filters.utils import apply_convolution


def box_filter(img, filter_size):
    """Apply box filter to the image. This is a simple averaging filter.

    Args:
        img (np.ndarray): Input Image array
        filter_size (Tuple[int, int]): Size of the filter.

    Raises:
        ValueError: If filter_size is not a tuple.

    Returns:
        np.ndarray: Filtered image array.
    """
    check_image(img)
    if not isinstance(filter_size, tuple):
        raise ValueError("filter_size should be a tuple")

    if len(img.shape) == 2:
        kernel = np.ones(filter_size)
        final_img = apply_convolution(img, [kernel], seperate=False, take_mean=True)

        return final_img
    else:
        # apply filter to each channel
        final_img = np.zeros(img.shape)
        for i in range(img.shape[2]):
            final_img[:, :, i] = box_filter(img[:, :, i], filter_size)
        return final_img


def laplacian_filter(img, diagonal=False, return_edges=True):
    """Apply Laplacian filter to the image.

    Args:
        img (np.ndarray): Input Image array
        diagonal (bool, optional): If True, apply diagonal laplacian filter. Defaults to False.
        return_edges (bool, optional): If True, return image with edges detected else return the sharpened image. Defaults to True.

    Raises:
        ValueError: If diagonal is not a boolean value.

    Returns:
        np.ndarray: Image with edges detected
    """
    check_image(img)

    if not isinstance(diagonal, bool):
        raise ValueError(f"diagonal should be a boolean value. Got {diagonal}")

    if len(img.shape) == 2:
        if diagonal:
            if return_edges:
                kernel = np.array([[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]])
            else:
                kernel = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
        if not diagonal:
            if return_edges:
                kernel = np.array([[0, -1, 0], [-1, 4, -1], [0, -1, 0]])
            else:
                kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])

        final_img = apply_convolution(img, [kernel], seperate=False)

        return final_img
    else:
        # apply filter to each channel
        final_img = np.zeros(img.shape)
        for i in range(img.shape[2]):
            final_img[:, :, i] = laplacian_filter(img[:, :, i], diagonal, return_edges)
        return final_img.astype(np.uint8)


def robert_cross_filter(img):
    """Apply Robert Cross filter to the image. This uses 2x2 kernels. Extending this to 3x3 kernel will give us Sobel filter.

    Args:
        img (np.ndarray): Input Image array

    Returns:
        np.ndarray: Image with edges detected
    """
    check_image(img)

    if len(img.shape) == 2:
        kernel_x = np.array([[-1, 0], [0, 1]])  # kerenel for x direction
        kernel_y = np.array([[0, -1], [1, 0]])  # kernel for y direction

        final_img = apply_convolution(img, [kernel_x, kernel_y], seperate=True)

        return final_img
    else:
        # apply filter to each channel
        final_img = np.zeros(img.shape)
        for i in range(img.shape[2]):
            final_img[:, :, i] = robert_cross_filter(img[:, :, i])
        return final_img.astype(np.uint8)


def sobel_filter(img):
    """
    Apply Sobel filter to the image. This uses 3x3 kernels. This is extension of Robert Cross filter. Center of kerenel is weighted more than the corners. This gives us more accurate edge detection.

    Args:
        img (np.ndarray): Input Image array

    Returns:
        np.ndarray: Image with edges detected
    """

    check_image(img)

    if len(img.shape) == 2:
        kernel_x = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])
        kernel_y = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])

        final_img = apply_convolution(img, [kernel_x, kernel_y], seperate=True)

        return final_img
    else:
        # apply filter to each channel
        final_img = np.zeros(img.shape)
        for i in range(img.shape[2]):
            final_img[:, :, i] = sobel_filter(img[:, :, i])
        return final_img.astype(np.uint8)
