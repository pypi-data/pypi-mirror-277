import numpy as np


def fft(signal):
    """Calculates 1D Fast Fourier Transform of a signal. It is a recursive function based on the Cooley-Tukey algorithm. Computes the DFT of a signal or array of signals in O(n log n) time.

    NOTE: Works only for signals with length as power of 2.

    Args:
        signal (np.ndarray): Input signal to calculate FFT.

    Raises:
        ValueError: If signal length is not power of 2.
        ValueError: If signal is not a numpy array.
        ValueError: If signal is not 1D.

    Returns:
        np.ndarray: FFT of the input signal. The output is a complex array.
    """
    if not isinstance(signal, np.ndarray):
        raise ValueError("Input signal must be a numpy array.")
    if signal.ndim != 1:
        raise ValueError("Input signal must be 1D.")
    N = len(signal)
    if N <= 1:
        return signal
    if N % 2 != 0:
        raise ValueError("Signal length must be power of 2.")
    even = fft(signal[0::2])
    odd = fft(signal[1::2])
    terms = np.exp(-2j * np.pi * np.arange(N) / N)
    return np.concatenate([even + terms[: N // 2] * odd, even + terms[N // 2 :] * odd])


def ifft(specturm):
    """Calculates 1D Inverse Fast Fourier Transform of a specturm. It is a recursive function based on the Cooley-Tukey algorithm. Computes the IDFT of a specturm or array of specturms in O(n log n) time.

    Args:
        specturm (np.ndarray): Input specturm to calculate IFFT. The input is a complex array.

    Raises:
        ValueError: If specturm is not a numpy array.
        ValueError: If specturm is not 1D.

    Returns:
        np.ndarray: IFFT of the input specturm. The output is a complex array.
    """
    if not isinstance(specturm, np.ndarray):
        raise ValueError("Input specturm must be a numpy array.")
    if specturm.ndim != 1:
        raise ValueError("Input specturm must be 1D.")

    N = len(specturm)
    if N <= 1:
        return specturm
    even = ifft(specturm[0::2])
    odd = ifft(specturm[1::2])
    terms = np.exp(2j * np.pi * np.arange(N) / N)
    return (
        np.concatenate([even + terms[: N // 2] * odd, even + terms[N // 2 :] * odd]) / 2
    )


def fft2(image):
    """Calculates 2D Fast Fourier Transform of an image. It is a recursive function based on the Cooley-Tukey algorithm. Computes the 2D DFT of an image or array of images in O(n^2 log n) time.

    NOTE: Currently works only for square images and gray scale with size as power of 2.

    Args:
        image (np.ndarray): Input image to calculate 2D FFT.

    Returns:
        np.ndarray: 2D FFT of the input image. The output is a complex array.
    """

    if not isinstance(image, np.ndarray):
        raise ValueError("Input image must be a numpy array.")
    if image.ndim != 2:
        raise ValueError("Input image must be 2D.")
    if (image.shape[0] != image.shape[1]) or (image.shape[0] % 2 != 0):
        raise ValueError("Image must be square and size must be power of 2.")

    M, N = image.shape
    specturm = np.zeros((M, N), dtype=complex)
    for i in range(M):
        specturm[i] = fft(image[i])
    for j in range(N):
        specturm[:, j] = fft(specturm[:, j])

    return specturm


def ifft2(specturm):
    """Calculates 2D Inverse Fast Fourier Transform of a specturm. It is a recursive function based on the Cooley-Tukey algorithm. Computes the 2D IDFT of a specturm or array of specturms in O(n^2 log n) time.

    Args:
        specturm (np.ndarray): Input specturm to calculate 2D IFFT. The input is a complex array.

    Returns:
        np.ndarray: 2D IFFT of the input specturm. The output is a complex array.
    """

    if not isinstance(specturm, np.ndarray):
        raise ValueError("Input specturm must be a numpy array.")
    if specturm.ndim != 2:
        raise ValueError("Input specturm must be 2D.")
    if (specturm.shape[0] != specturm.shape[1]) or (specturm.shape[0] % 2 != 0):
        raise ValueError("Specturm must be square and size must be power of 2.")

    M, N = specturm.shape
    image = np.zeros((M, N), dtype=complex)
    for i in range(M):
        image[i] = ifft(specturm[i])
    for j in range(N):
        image[:, j] = ifft(image[:, j])

    return image


def fftshift(spectrum):
    """Shifts the zero frequency component to the center of the spectrum.

    Args:
        spectrum (np.ndarray): Input spectrum to shift.

    Raises:
        ValueError: If spectrum is not a numpy array.
        ValueError: If spectrum is not 2D.
        ValueError: If spectrum is not square and size is not power of 2.

    Returns:
        np.ndarray: Shifted spectrum.
    """

    if not isinstance(spectrum, np.ndarray):
        raise ValueError("Input spectrum must be a numpy array.")
    if spectrum.ndim != 2:
        raise ValueError("Input spectrum must be 2D.")
    if (spectrum.shape[0] != spectrum.shape[1]) or (spectrum.shape[0] % 2 != 0):
        raise ValueError("Spectrum must be square and size must be power of 2.")

    M, N = spectrum.shape
    shift_spectrum = np.zeros((M, N), dtype=complex)
    shift_spectrum = np.concatenate([spectrum[M // 2 :], spectrum[: M // 2]], axis=0)
    shift_spectrum = np.concatenate(
        [shift_spectrum[:, N // 2 :], shift_spectrum[:, : N // 2]], axis=1
    )

    return shift_spectrum
