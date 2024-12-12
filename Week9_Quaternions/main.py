#!/usr/bin/env python
from PIL import Image, ImageDraw
import math
import cmath

def clamp(c, mi, mx):
    return max(mi, min(c, mx))


def dist(a, b):
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

def attenuation(d, ld):
    if (d==0):
        d=1
    return math.e**(2*math.pi * d * 1j/ld)/(d**2)

def main():
    WIDTH = 1024
    HEIGHT = 1024

    image=Image.new("RGB",(WIDTH, HEIGHT), (0, 0, 0))
    canvas=ImageDraw.Draw(image)

    ld = 25

    scale = 10000000
    l1 = (0, 0)

    l2 = (120, 35)

    for x in range(WIDTH):
        for y in  range(HEIGHT):
            d = dist(l1, (x, y))
            d2 = dist(l2, (x, y))



            a = attenuation(d, ld).real

            b = attenuation(d2, ld).real

            #print("a:", a, "\n", "b:", b)

            c = b + a

            c = clamp(c * scale, 0, 255)

            Cd = (int(c), int(c), int(c))

            canvas.point((x,y),Cd)


    image = image.transpose(Image.FLIP_TOP_BOTTOM)
    image.show()
    image.save("Week9_Quaternions/image.png")

if __name__ == "__main__":
    main()