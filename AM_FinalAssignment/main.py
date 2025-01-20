import numpy as np
import cmath, math
from PIL import Image

### \brief A script to blur a square image using convolution and Fast Fourier Transforms
### \version 1.0
### \date 20/01/2025

### Useful Terminology:
### - FFT (Fast Fourier Transform)
### - CFFT (Color Fast Fourier Transform)
### - FF2DT (Fast Fourier 2D Transform)
### - Kernel / Filter: The image / shape used to blur the image through convolution.

def main(im_path="./source.png", out_path="./output.png", filter="gaussian"):
    """
    Load in an image and blur it using a convolution filter with Fourier Transforms.

        im_path: Path to the source image. This is the image that will be blurred.
    
        out_path: Path to the output save file. This is where the blurred image will be saved.

        filter: Blur Type
            (1) Box: Uses a box to convolve the image. Can be quite jaggedy
            (2) Gaussian (default): Uses a gaussian circle to convolve the image. Softer blur than Box.

    """

    # Load in the image and convert it into a NumPy RGB array.
    image = Image.open(im_path).convert("RGB")
    arr = np.array(image, dtype=np.float64)

    # Use a 2d implementation of Fast Fourier Transform to get the image frequencies
    cfft_arr = ff2d_transform(arr)
    cfft_spectrum = cfft_arr

    # Display the CFFT (Color Fast Fourier Transform).
    cfft_image = Image.fromarray(np.uint8(np.abs(cfft_spectrum) * 255)) 
    cfft_image.show()

    # Create a convolution kernel to blur the image.
    # We normalize the kernel so that it works nicely when multiplied with the CFFT.
    kernel = create_kernel(arr, filter)
    kernel /= np.max(kernel)

    # Display the convolution kernel
    kernel_shape_image = Image.fromarray(np.uint8(kernel * 255)) 
    kernel_shape_image.show()

    # Fourier Transform the kernel so that it can be multiplied with the CFFT.
    kernel_arr = ff2d_transform(kernel)
    kernel_spectrum = np.abs(kernel_arr)

    # Display the FFT Kernel
    kernel_fft_image = Image.fromarray(np.uint8(kernel_spectrum/np.max(kernel_spectrum) * 255)) 
    kernel_fft_image.show()

    # Multiply the transformed convolution kernel with the transformed image.
    # This will blur the image.
    mult_arr = (cfft_spectrum * kernel_spectrum)

    # ICFFT the multiplied array so that it can be turned back into an image. We only need the real numbers.
    out_arr = ff2d_transform(mult_arr, inv=True)
    out_image = np.real(out_arr)

    ### Code from ChatGPT
    ### prompt: "make sure the image is not over or under exposed."
    out_image = (out_image - np.min(out_image)) / (np.max(out_image) - np.min(out_image)) * 255 
    ###
    
    # Save the blurred image to the out_path
    out_image = Image.fromarray(np.uint8(np.clip(out_image, 0, 255)))
    out_image.show()
    out_image.save(out_path)


def ff2d_transform(arr, inv=False):
    """
    Fast Fourier Transform in 2 dimensions.
        
        arr: the input 2D array to be FF2DT. This should be the NumPy data as "RGB"
        
        inv: Whether to apply IFF2DT or FF2DT. Allows for round-tripping FF2DT within the same function. 
            False: image -> transform. 
            True: transform -> image
    
    """

    # Create temporary arrays to do CFFT with.
    # The np.complex128 datatype allows for storing complex numbers within arrays.
    f0_arr = np.zeros_like(arr, dtype=np.complex128)
    f1_arr = np.zeros_like(arr, dtype=np.complex128)
    
    # Do CFFT for all the rows in the image.
    for idx, row in enumerate(arr):
        f0_arr[idx] = color_transform(row, inv)

    # Flip the rows and columns in the CFFT image.
    # Ideally, something like array.T or array.transpose would be used, 
    # However it doesn't work with CFFT therefore we have to iteratre through all the pixels. This can be slow in larger images.
    flipped = np.zeros_like(f0_arr, dtype=np.complex128)
    for i in range(f0_arr.shape[0]):
        for j in range(f0_arr.shape[1]):
            flipped[j, i] = f0_arr[i, j]

    # Do CFFT for all the new rows in the CFFT image.
    # Doing this CFFT twice (with flipping directions) allows for the whole image to be CFFT'd.
    for idx, row in enumerate(flipped):
        f1_arr[idx] = color_transform(row, inv)

    # Normalize the final array so that we don't have any extreme numbers.
    f1_arr /= (arr.shape[0] * arr.shape[1])

    return f1_arr


def color_transform(cd_arr, inv=False):
    """
    CFFT (Colour Fast Fourier Transform) is a fast fourier transform for all the primary colors in a pixel. This allows for better visualization as well as filter control.

        cd_arr: The array containing "RGB" data.

        inv: Whether to apply ICFFT or CFFT. Allows for round-tripping CFFT within the same function. 
            False: image -> transform. 
            True: transform -> image

    """

    # Arrays are created for each of the colors.
    # We then FFT each color and combine it back into one large array.
    r_arr = cd_arr[:, 0] 
    r_fft = fft(r_arr, inv)

    g_arr = cd_arr[:, 1]  
    g_fft = fft(g_arr, inv)

    b_arr = cd_arr[:, 2]  
    b_fft = fft(b_arr, inv)

    ### Code from ChatGPT
    ### prompt: "combine my seperate R, G, B arrays into one large array."
    cd_fft = np.stack((r_fft, g_fft, b_fft), axis=-1)
    ###
    
    return cd_fft


def fft(arr, inv=False):
    """
    FFT (Fast Fourier Transform) is a fast way to convert images into their 'transform' space. It splits the array into even and odds and recusively applies FFT.
    
        arr: The array containing the data to be transformed.

        inv: Whether to apply IFFT or FFT. Allows for round-tripping FFT within the same function. 
            False: data -> transform. 
            True: transform -> data
    """

    ### The following section is modified from Ian Stevenson, Builtin.com, and ChatGPT.
    ### See the PDF Report for citations.
    
    # We calculate the size of the array, as well as the sign (depending on FFT or IFFT). This is used for the FFT calculations.
    # We also create a temporary array to store data in.
    N = len(arr)
    sign = 1 if inv else -1
    result = np.zeros(N, dtype=np.complex128)

    # Check to see the size of the array and managed accordingly.
    if N == 1:
        result[0] = arr[0]
    else:
        # Split the array, apply I/FFT, and combine together.
        dft_evens = fft(arr[::2], inv) 
        dft_odds = fft(arr[1::2], inv)

        for k in range(N // 2):
            t = cmath.exp(sign * 2j * cmath.pi * k / N) * dft_odds[k]
            result[k] = dft_evens[k] + t
            result[k + N // 2] = dft_evens[k] - t

    # We scale the result accordingly when doing IFFT.
    if inv:
        result /= np.sqrt(N)

    return result


def create_kernel(arr, type="gaussian"):
    """
    This function procedurally generates convolution kernels to be used for blurring.

        arr: Array used to specify shape and size for the kernels.

        type: Type of kernel to use for blurring
            (1) Box: Uses a box to convolve the image. Can be quite jaggedy
            (2) Gaussian (default): Uses a gaussian circle to convolve the image. Softer blur than Box.

    """

    # We create an empty shape for the kernel.
    kernel = np.zeros_like(arr, dtype=np.float64)

    # Due to the way that the CFFT has been done, the shapes must be centered around (0, 0) to work correctly.

    # The box filter is simple a box filled white by iterating over the pixels. Other colors can be specified but for the sake of this assignment it has been left as white.
    if type == "box":
        for x in range(0, 50):
            for y in range(0, 50):
                kernel[x][y] = (255, 255, 255)


    # Gaussian is a "smoothed circle". It has a much softer blur as there isn't a sharp overlap like with box filtering.

    ### This code took the formula mentioned by TowardsAi.net
    ### See the PDF Report for citations
    elif type == "gaussian":
        sigma = 10

        for x in range(0, arr.shape[0]):
            for y in range(0, arr.shape[1]):
                kernel[x][y] = 0.5 * math.pi * sigma**2 * np.exp(-(x**2 + y**2)/(2*sigma**2))
                
    return kernel
    ###

if __name__ == "__main__":
    main("./source.png", "./output.png", "gaussian")