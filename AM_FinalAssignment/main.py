import numpy as np
import cmath
from PIL import Image

def main():
    # Load the image and convert it into a NumPy data array. 
    # We use a greyscale image
    image = Image.open("./image.png").convert("L")
    arr = np.array(image, dtype=np.float64)

    dft_arr = np.zeros_like(arr, dtype=np.complex128)
    for idx, row in enumerate(arr):
        dft_arr[idx] = fft(row, False)
        print(idx)

    im = Image.fromarray(np.real(dft_arr))
    im.show()
    
    idft_arr = np.zeros_like(dft_arr, dtype=np.complex128)
    for idx, row in enumerate(dft_arr):
        idft_arr[idx] = fft(row, True)/len(idft_arr)
        print(idx)
    

    # Convert the NumPy array back into an image to be shown and saved.
    im = Image.fromarray(np.real(idft_arr))
    im.show()
    im.save("./output.png")

def fft(arr, inv=False):
    N = len(arr)
    sign = 1 if inv else -1
    result = np.zeros(N, dtype=np.complex128)

    if N == 1:
        result[0] = arr[0]
    
    else:
        dft_evens = fft(arr[::2], inv) 
        dft_odds = fft(arr[1::2], inv)

        for k in range(N//2):
            t = cmath.exp(sign * 2j * cmath.pi * k/N) * dft_odds[k]
            result[k] = dft_evens[k] + t
            result[k+N//2] = dft_evens[k] - t
    
    return result

main()