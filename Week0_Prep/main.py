#!/usr/bin/env python
from PIL import Image, ImageDraw
import AM_module.AM_Canvas as am 

class AM_Canvas(am.AM_Canvas):
    def draw(self):
        super().draw()
        self.canvas.line(((100,100),(200,100),(200,200),(100,200),(100,100)),(0,255,0))
        self.canvas.point((150,150),(255,0,255))

def main():
    am_canvas = AM_Canvas(512, 512, (0, 0, 0))
    am_canvas.draw()
    am_canvas.show()
    am_canvas.save("Week0_Prep/image.png")

if __name__ == "__main__":
    main()