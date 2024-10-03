#!/usr/bin/env python
from PIL import Image, ImageDraw
from ..AM_module.AM_Canvas import AM_Canvas

def f(x):
    return x**3

def df(x, dt):
    return (f(x+dt) - f(x)) / dt

def F(x, dt):
    return dt * (f(x) + f(x + 1)) / 2

#!/usr/bin/env python
from PIL import Image, ImageDraw
import AM_module.AM_Canvas as am 

class AM_Canvas(am.AM_Canvas):
    def draw(self):
        super().draw()

        Y_INTERCEPT = WIDTH/2
        X_INTERCEPT = HEIGHT/2

        dt = 0.01
        AMP = 50

        total = 0
        theta = 0.01

        for sx in range(int(-WIDTH/2), int(WIDTH/2)):       
            x = sx * theta

            f0 = f(x)
            f1 = f(x + theta) 

            canvas.line([(sx + Y_INTERCEPT, f0 * AMP + Y_INTERCEPT), (sx + WIDTH/2, f1 * AMP + X_INTERCEPT)], fill=(255, 255, 255))

            # Derive it

            d0 = df(x, dt) 
            d1 = df(x+theta, dt)

            canvas.line([(sx + WIDTH/2, d0 * AMP + Y_INTERCEPT), (sx + WIDTH/2, d1 * AMP + Y_INTERCEPT)], fill=(255, 0, 0))

            # Integrate it

            i0 = F(x, dt)

            i1 = F(x+theta, dt) 

            canvas.line([(sx + WIDTH/2, i0 * AMP + Y_INTERCEPT), (sx + 1 + WIDTH/2, i1 * AMP + Y_INTERCEPT)], fill=(0, 255, 0))

def main():
    am_canvas = AM_Canvas(512, 512, (0, 0, 0))
    am_canvas.draw()
    am_canvas.show()
    am_canvas.save("Week0_Prep/image.png")

if __name__ == "__main__":
    main()