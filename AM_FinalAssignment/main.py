import numpy as np
import cmath
from PIL import Image

def main():
    # Load the image and convert it into a NumPy data array. 
    # We use a greyscale image
    image = Image.open("./low.png").convert("L")
    arr = np.array(image, dtype=np.float64)

    dft_arr = np.zeros_like(arr, dtype=np.complex128)
    for idx, row in enumerate(arr):
        dft_arr[idx] = dft(row, False)
        print(idx)

    im = Image.fromarray(np.real(dft_arr))
    im.show()
    
    idft_arr = np.zeros_like(dft_arr, dtype=np.complex128)
    for idx, row in enumerate(dft_arr):
        idft_arr[idx] = dft(row, True)
        print(idx)
    

    # Convert the NumPy array back into an image to be shown and saved.
    im = Image.fromarray(np.real(idft_arr))
    im.show()
    im.save("./output.png")


def dft(arr, inv=False):
    N = len(arr)
    sign = 1 if inv else -1
    result = np.zeros(N, dtype=np.complex128)

    for k in range(N):
        total = 0
        for n in range(N):
            total += arr[n] * cmath.exp(sign * 2j * cmath.pi * k * n/N)

        if inv:
            total /= N

        result[k] = total
        

    return result

main()