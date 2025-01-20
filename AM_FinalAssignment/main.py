import numpy as np
import cmath
from PIL import Image

def main():
    # Load the image and convert it into a NumPy data array. 
    image = Image.open("./image.png").convert("RGB")
    arr = np.array(image, dtype=np.float64)

    # Apply 2D FFT on the image array
    cfft_arr = ff2d_transform(arr)/len(arr)

    # Show and save the magnitude spectrum (abs of FFT)
    cfft_spectrum = np.abs(cfft_arr)
    cfft_image = Image.fromarray(np.uint8(np.clip(cfft_spectrum, 0, 255)))  # Clip values between 0 and 255
    cfft_image.show()
    cfft_image.save("./cfft.png")

    kernel = create_kernel(arr, "box")
    kern_arr = ff2d_transform(kernel)

    kern_spectrum = np.abs(kern_arr)
    kern_spectrum = np.clip(kern_spectrum/np.max(kern_spectrum), 0, 1)
    kern_image = Image.fromarray(np.uint8(kern_spectrum*255))  # Clip values between 0 and 255
    kern_image.show()
    kern_image.save("./kern.png")

    mult_arr = (cfft_arr * kern_spectrum)

    # Apply 2D Inverse FFT to get back the image
    back_arr = ff2d_transform(mult_arr, inv=True)

    # Since the result might have small imaginary parts, we use the real part
    back_image = np.real(back_arr)/len(arr)
    back_image = Image.fromarray(np.uint8(np.clip(back_image, 0, 255)))
    back_image.show()
    back_image.save("./output.png")


def ff2d_transform(arr, inv=False):
    """
    Perform 2D Fourier transform: First FFT on rows, then on columns (and vice versa for inverse)
    """
    f0_arr = np.zeros_like(arr, dtype=np.complex128)
    
    # Apply FFT to rows (axis=1)
    for idx, row in enumerate(arr):
        f0_arr[idx] = color_transform(row, inv)

    flipped = np.zeros_like(f0_arr, dtype=np.complex128)
    for i in range(f0_arr.shape[0]):
        for j in range(f0_arr.shape[1]):
            flipped[j, i] = f0_arr[i, j]

    # Apply FFT to the transposed array (which corresponds to columns of the original)
    f1_arr = np.zeros_like(f0_arr, dtype=np.complex128)
    for idx, row in enumerate(flipped):
        f1_arr[idx] = color_transform(row, inv)


    return f1_arr


def color_transform(cd_arr, inv=False):
    """
    Apply the 1D FFT on the three color channels of an image (RGB)
    """
    r_arr = cd_arr[:, 0]  # Red channel
    g_arr = cd_arr[:, 1]  # Green channel
    b_arr = cd_arr[:, 2]  # Blue channel

    # Apply FFT to each color channel
    r_fft = fft(r_arr, inv)
    g_fft = fft(g_arr, inv)
    b_fft = fft(b_arr, inv)

    # Stack the transformed channels back together
    cd_fft = np.stack((r_fft, g_fft, b_fft), axis=-1)
    
    return cd_fft


def fft(arr, inv=False):
    """
    Apply 1D FFT (DFT) to a 1D array (signal)
    """
    N = len(arr)
    sign = 1 if inv else -1
    result = np.zeros(N, dtype=np.complex128)

    if N == 1:
        result[0] = arr[0]
    else:
        dft_evens = fft(arr[::2], inv) 
        dft_odds = fft(arr[1::2], inv)

        for k in range(N // 2):
            t = cmath.exp(sign * 2j * cmath.pi * k / N) * dft_odds[k]
            result[k] = dft_evens[k] + t
            result[k + N // 2] = dft_evens[k] - t


    return result


def create_kernel(arr, type="box"):
    # Create a simple kernel (box filter)
    kernel = np.zeros_like(arr, dtype=np.float64)

    if type == "box":
        # Define a box filter: 40% of image size
        y_start, y_end = int(arr.shape[0] * 0.4), int(arr.shape[0] * 0.6)
        x_start, x_end = int(arr.shape[1] * 0.4), int(arr.shape[1] * 0.6)
        kernel[y_start:y_end, x_start:x_end] = (25, 255, 255)  # Set the box region to 255 (white)

    return kernel


main()
