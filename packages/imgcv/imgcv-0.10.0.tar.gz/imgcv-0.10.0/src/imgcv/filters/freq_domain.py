import numpy as np
from imgcv.fftpack.fft import fft2, ifft2, fftshift


def low_pass_filter(img, cutoff, order=None, type="butterworth", return_img_fft=False):
    """Apply low pass filter in the frequency domain to an image.
    NOTE: Currently works only for square images and gray scale with size as power of 2.

    Args:
        img (np.ndarray): Input image to apply low pass filter.
        cutoff (int): Cutoff frequency of the filter.
        order (int, optional): Order of the Butterworth filter. Defaults to None. If None, order is set to 1.
        type (str, optional): Type of the filter. Choose one of 'ideal', 'butterworth', 'gaussian'. Defaults to "butterworth".
        return_img_fft (bool, optional): If True, return the filtered image in the frequency domain along with the original image in the frequency domain. Defaults to False.

    Raises:
        ValueError: If input image is not a numpy array.
        ValueError: If input image is not 2D.
        ValueError: If cutoff frequency is not an integer.
        ValueError: If order is not an integer.
        ValueError: If filter type is invalid.

    Returns:
        np.ndarray: Filtered image in the spatial domain.
        (np.ndarray, np.ndarray): Filtered image in the frequency domain and the original image in the frequency domain (if return_img_fft is True)
    """

    if not isinstance(img, np.ndarray):
        raise ValueError("Input image must be a numpy array.")

    if img.ndim != 2:
        raise ValueError("Input image must be 2D.")

    if not isinstance(cutoff, int):
        raise ValueError("Cutoff frequency must be an integer.")

    if order is not None and not isinstance(order, int):
        raise ValueError("Order must be an integer.")

    if type not in ["ideal", "butterworth", "gaussian"]:
        raise ValueError(
            "Invalid filter type. Choose one of 'ideal', 'butterworth', 'gaussian'."
        )

    if order is None and type == "butterworth":
        order = 1

    if img.ndim == 2:
        M, N = img.shape
        img_fft = fft2(img)
        img_fft_shifted = fftshift(img_fft)

        # create distance matrix
        u = np.arange(-M // 2, M // 2)
        v = np.arange(-N // 2, N // 2)
        U, V = np.meshgrid(u, v)
        D = np.sqrt(U**2 + V**2)

        H = np.zeros((M, N))

        if type == "ideal":
            H[D <= cutoff] = 1
        elif type == "butterworth":
            H = 1 / (1 + (D / cutoff) ** (2 * order))
        elif type == "gaussian":
            H = np.exp(-(D**2) / (2 * cutoff**2))

        img_fft_filtered = img_fft_shifted * H

        if return_img_fft:
            return (img_fft_filtered, img_fft_shifted)

        else:
            img_filtered = np.abs(ifft2(img_fft_filtered))
            return img_filtered


def high_pass_filter(img, cutoff, order=None, type="butterworth", return_img_fft=False):
    """Apply high pass filter in the frequency domain to an image.
    NOTE: Currently works only for square images and gray scale with size as power of 2.

    Args:
        img (np.ndarray): Input image to apply high pass filter.
        cutoff (int): Cutoff frequency of the filter.
        order (int, optional): Order of the Butterworth filter. Defaults to None. If None, order is set to 1.
        type (str, optional): Type of the filter. Choose one of 'ideal', 'butterworth', 'gaussian'. Defaults to "butterworth".
        return_img_fft (bool, optional): If True, return the filtered image in the frequency domain along with the original image in the frequency domain. Defaults to False.

    Raises:
        ValueError: If input image is not a numpy array.
        ValueError: If input image is not 2D.
        ValueError: If cutoff frequency is not an integer.
        ValueError: If order is not an integer.
        ValueError: If filter type is invalid.

    Returns:
        np.ndarray: Filtered image in the spatial domain.
        (np.ndarray, np.ndarray): Filtered image in the frequency domain and the original image in the frequency domain (if return_img_fft is True)
    """

    if not isinstance(img, np.ndarray):
        raise ValueError("Input image must be a numpy array.")

    if img.ndim != 2:
        raise ValueError("Input image must be 2D.")

    if not isinstance(cutoff, int):
        raise ValueError("Cutoff frequency must be an integer.")

    if order is not None and not isinstance(order, int):
        raise ValueError("Order must be an integer.")

    if type not in ["ideal", "butterworth", "gaussian"]:
        raise ValueError(
            "Invalid filter type. Choose one of 'ideal', 'butterworth', 'gaussian'."
        )

    if order is None and type == "butterworth":
        order = 1

    if img.ndim == 2:
        M, N = img.shape
        img_fft = fft2(img)
        img_fft_shifted = fftshift(img_fft)

        # create distance matrix
        u = np.arange(-M // 2, M // 2)
        v = np.arange(-N // 2, N // 2)
        U, V = np.meshgrid(u, v)
        D = np.sqrt(U**2 + V**2)

        H = np.zeros((M, N))

        if type == "ideal":
            H[D > cutoff] = 1
        elif type == "butterworth":
            H = 1 / (1 + (cutoff / D) ** (2 * order))
        elif type == "gaussian":
            H = 1 - np.exp(-(D**2) / (2 * cutoff**2))

        img_fft_filtered = img_fft_shifted * H

        if return_img_fft:
            return (img_fft_filtered, img_fft_shifted)

        else:
            img_filtered = np.abs(ifft2(img_fft_filtered))
            return img_filtered
