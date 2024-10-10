#!/usr/bin/env python
import AM_module as am 
from PIL import Image
from math import *
from random import *
import pygame
pygame.init()

class AM_Canvas(am.AM_Canvas):
    def draw(self):
        super().draw()

        objs = []
        for p in range(10):
            pos=(
                    (-0.5 + random()) * self.width/2, 
                    250 + random() * 250, 
                    (-0.5 + random())*self.height/2
                )

            r = random()*50


            sph = am.AM_Sphere(pos=pos, r=r)

            objs.append(sph)

        for p in range(10):
            pos=(
                    (-0.5 + random()) * self.width/2, 
                    250 + random() * 250, 
                    (-0.5 + random())*self.height/2
                )

            r = random()*10
            h = random() * 50


            cyl = am.AM_Cylinder(pos=pos, r=r, h=h)

            objs.append(cyl)

        for p in range(10):
            pos=(
                    (-0.5 + random()) * self.width/2, 
                    250 + random() * 250, 
                    (-0.5 + random())*self.height/2
                )

            r = random()*10
            h = random() * 25


            con = am.AM_Cone(pos=pos, r=r, h=h)

            objs.append(con)

        for p in range(10):
            pos=(
                    (-0.5 + random()) * self.width/2, 
                    250 + random() * 250, 
                    (-0.5 + random())*self.height/2
                )

            
            rmin = random()*5
            rmax = rmin + random()*25


            con = am.AM_Torus(pos=pos, rmin=rmin, rmax=rmax)

            objs.append(con)


        for obj in objs:
            Cd = int(random()*255), int(random()*255), int(random()*255)
            obj.draw(self, res=(64, 32), color=Cd, wire=True)


        self.image = self.image.transpose(Image.FLIP_TOP_BOTTOM)



def main():
    am_canvas = AM_Canvas(1024, 1024, (0, 0, 0))

    if (True):
        screen = pygame.display.set_mode([am_canvas.width, am_canvas.height])
        running = True

        objs = []
        for p in range(10):
            pos=[
                    (-0.5 + random()) * am_canvas.width/2, 
                    250 + random() * 250, 
                    (-0.5 + random())*am_canvas.height/2
            ]

            r = random()*50

            Cd = int(random()*255), int(random()*255), int(random()*255)


            sph = am.AM_Sphere(pos=pos, r=r, c=Cd)

            objs.append(sph)

        for p in range(10):
            pos=[
                    (-0.5 + random()) * am_canvas.width/2, 
                    250 + random() * 250, 
                    (-0.5 + random())*am_canvas.height/2
            ]

            r = random()*10
            h = random() * 50

            Cd = int(random()*255), int(random()*255), int(random()*255)


            cyl = am.AM_Cylinder(pos=pos, r=r, h=h, c=Cd)

            objs.append(cyl)

        for p in range(10):
            pos=[
                    (-0.5 + random()) * am_canvas.width/2, 
                    250 + random() * 250, 
                    (-0.5 + random())*am_canvas.height/2
            ]

            r = random()*10
            h = random() * 25


            con = am.AM_Cone(pos=pos, r=r, h=h)

            objs.append(con)

        for p in range(10):
            pos=[
                    (-0.5 + random()) * am_canvas.width/2, 
                    250 + random() * 250, 
                    (-0.5 + random())*am_canvas.height/2
            ]

            
            rmin = random()*5
            rmax = rmin + random()*25

            Cd = int(random()*255), int(random()*255), int(random()*255)

            con = am.AM_Torus(pos=pos, rmin=rmin, rmax=rmax, c=Cd)

            objs.append(con)


        x_offset = 0
        y_offset = 0
        z_offset = 0
        while running:
            # Did the user click the window close button?
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            keys = pygame.key.get_pressed()

            if keys[pygame.K_LEFT]: # We can check if a key is pressed like this
                x_offset += 10
            if keys[pygame.K_RIGHT]:
                x_offset -= 10
                
            if keys[pygame.K_UP]:
                y_offset -= 10
            if keys[pygame.K_DOWN]:
                y_offset += 10

            if keys[pygame.K_LSHIFT]:
                z_offset -= 10
            if keys[pygame.K_SPACE]:
                z_offset += 10

            # Fill the background with black
            screen.fill((0, 0, 0))

            for obj in objs:
                obj.position[0] += x_offset
                obj.position[1] += y_offset
                obj.position[2] += z_offset
                obj.draw(am_canvas, res=(64, 32), color=Cd, wire=True, screen=screen)

            # Flip the display
            pygame.display.update()
            pygame.display.flip()

            x_offset = 0
            y_offset = 0
            z_offset = 0

        pygame.quit()

    else:
        am_canvas.draw()
        am_canvas.show()
        am_canvas.save("Week2_Rays/image.png")

if __name__ == "__main__":
    main()