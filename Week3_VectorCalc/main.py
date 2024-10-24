#!/usr/bin/env python
import AM_module as am 
from PIL import Image
from random import random
from math import *

def hit(ray, objs):
    final_color = (0, 0, 0)

    t = float("inf")
    color = (0, 0, 0)
    n = (0, 0, 0)
        
    for obj in objs:
        t_new, n_new, t_color = obj.hit(ray)

        if t_new > 0 and t_new < t:
            n = n_new
            t = t_new
            color = t_color

    #print(t)
    #print("COLOR:", color)


    return color
    
class AM_Canvas(am.AM_Canvas):
    def draw(self):
        objs = []
        for p in range(25):
            pos=(
                    (-0.5 + random()) * self.width/4, 
                    (-0.5 + random()) * self.height/4,
                    50 + random() * 25
                )

            r = random()*10


            sph = am.AM_Sphere(pos=pos, r=r, c=(int(random()*255), int(random()*255), int(random()*255)))

            objs.append(sph)


        #objs = [
        #    am.AM_Sphere(pos=(0, 0, 5), r=1,c=(int(random()*255), int(random()*255), int(random()*255))) 
        #]
    
        for y in range(0, self.height):
            for x in range(0, self.width):
                u = 2 * ((x / self.width) - 0.5)
                v = 2 * ((y / self.height) - 0.5)
                fov = 1

                direction = (u, v, fov)
                direction_length = sqrt(direction[0]**2 + direction[1]**2 + direction[2]**2)

                direction = (
                    direction[0]/direction_length,
                    direction[1]/direction_length,
                    direction[2]/direction_length
                )

                ray=[(0, 0, 0), direction]
                #Cd = (int(ray[1][0] * 255), int(ray[1][1]*255), int(ray[1][2]*255))

                Cd = (0, 0, 0)

                Cd = hit(ray, objs)

                self.image.putpixel((x, y), Cd)
                print(f"Pixel: {x}, {y} completed!")

        self.image = self.image.transpose(Image.FLIP_TOP_BOTTOM)

def main():
    am_canvas = AM_Canvas(256, 256, (0, 0, 0))
    am_canvas.draw()
    am_canvas.show()
    am_canvas.save("Week3_VectorCalc/image.png")

if __name__ == "__main__":
    main()