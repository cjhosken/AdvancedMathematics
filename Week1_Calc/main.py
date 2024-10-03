#!/usr/bin/env python
import AM_module.AM_Canvas as am 
from PIL import Image
from math import *


def f(x):
    return sin(x) * 100

def df(x, dt):
    return (f(x+dt) - f(x)) / dt

def F(x, dt):
    return (dt / 2) * (f(x) + f(x + dt))


class AM_Canvas(am.AM_Canvas):
    def draw(self):
        super().draw()

        

        dt = 0.05
        offset_y = self.height/2

        total = 0

        self.canvas.line([(0, offset_y), (self.width, offset_y)], fill=(75, 75, 75))

        for sx in range(self.width):       
            # remapping x from pixel space to graph space
            x = sx * dt

            # Original function
            f0 = f(x)
            f1 = f(x + dt) 

            self.canvas.line([(sx, f0 + offset_y), (sx + 1, f1 + offset_y)], fill=(255, 255, 255))

            # Derive it
            d0 = df(x, dt) 
            d1 = df(x+dt, dt)

            self.canvas.line([(sx, d0 + offset_y), (sx + 1, d1 + offset_y)], fill=(255, 0, 0))

            # Integrate it
            i0 = F(x, dt)
            i1 = F(x+dt, dt)

            self.canvas.line([(sx, i0 + total + offset_y), (sx + 1, i1 + i0 + total + offset_y)], fill=(0, 255, 0))

            total = i0 + total

        self.image = self.image.transpose(Image.FLIP_TOP_BOTTOM)

def main():
    am_canvas = AM_Canvas(1024, 1024, (0, 0, 0))
    am_canvas.draw()
    am_canvas.show()
    am_canvas.save("Week1_Calc/image.png")

if __name__ == "__main__":
    main()