#!/usr/bin/env python
from AM_module import *
from PIL import Image
from math import *
from random import random


def sinc(x):
    return 1 if x==0 else sin(x)/x

def pdf(x):
    return (1-(x/pi)) * (2/pi)


class AM_Canvas(AM_Canvas):
    def draw(self):
        super().draw()

        samples = 10000000

        integral = 0

        for s in range(samples):

            px = 0
            x = 0

            while True:
                x = random() * pi
                px = pdf(x)
                if random() * px < px:
                    break
                
            y = sinc(x) / px
            
            integral += y

            plot_x = x/pi * self.width
            plot_y = y/10 * self.height


            radius = 3
            self.canvas.ellipse((plot_x - radius, plot_y - radius, plot_x + radius, plot_y + radius),(255,0,0))

        integral /= samples 
        print(f"The Integral is: {integral}")

        self.image = self.image.transpose(Image.FLIP_TOP_BOTTOM)

def main():
    am_canvas = AM_Canvas(1024, 1024, (0, 0, 0))
    am_canvas.draw()

if __name__ == "__main__":
    main()