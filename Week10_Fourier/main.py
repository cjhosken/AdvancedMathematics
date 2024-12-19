#!/usr/bin/env python
import AM_module as am 
from PIL import Image
from math import *

def square_wave(x, freq):
    mid = freq/2

    return x % freq > mid

def dft(arr):
    out = []
    
    N = len(arr)

    for k in range(N):
        total = 0
        for n in range(N):
            total += arr[n] * e**(-1j * ((2*pi*n)/N)*k)

        print(total)

        out.append(total)

    return out


class AM_Canvas(am.AM_Canvas):
    def draw(self):
        super().draw()

    
        dt = 1
        offset_y = self.height/2

        freq = 100


        self.canvas.line([(0, offset_y), (self.width, offset_y)], fill=(75, 75, 75))

        arr = []

        for sx in range(self.width):
            x = sx * dt
            arr.append(square_wave(x, freq))

        fa = dft(arr)
        
        for i, a in enumerate(arr):
            sx = i/dt
            # Original function
            s0 = a * 100
            s1 = arr[i+1] * 100 if i < len(arr) - 1 else 0

            self.canvas.line([(sx, s0 + offset_y), (sx + 1, s1 + offset_y)], fill=(255, 255, 255))


            f0 = fa[i].real
            f1 = fa[i+1].real if i < len(arr) - 1 else 0

            self.canvas.line([(sx, f0 + offset_y), (sx + 1, f1 + offset_y)], fill=(255, 0, 0))

        self.image = self.image.transpose(Image.FLIP_TOP_BOTTOM)

def main():
    am_canvas = AM_Canvas(1024, 1024, (0, 0, 0))
    am_canvas.draw()
    am_canvas.show()
    am_canvas.save("Week10_Fourier/image.png")

if __name__ == "__main__":
    main()