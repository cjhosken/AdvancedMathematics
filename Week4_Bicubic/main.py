#!/usr/bin/env python
from PIL import Image
from random import random
from math import *
import pygame
pygame.init()


def bezier(t, pt0, pt1, pt2):
    return [
        (1 - t)**2  * pt0[0] + 2*(1-t)*t * pt1[0] + t**2 * pt2[0],
        (1 - t)**2  * pt0[1] + 2*(1-t)*t * pt1[1] + t**2 * pt2[1]
    ]

def main():
    width = 512
    height = 512
    background = (0, 0, 0)

    canvas = pygame.display.set_mode((width,height)) 

    control_points = []

    for pt in range(0, 4):
        x = int(random() * width)
        y = int(random() * height)
        control_points.append({
            "pos": [x, y],
            "radius": 7,
            "dragging": False
        })

    running = True

    while running:
        canvas.fill(background)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                for pt in control_points:
                    # Check if the mouse click is inside the circle
                    dx = mouse_x - pt["pos"][0]
                    dy = mouse_y - pt["pos"][1]
                    if dx * dx + dy * dy <= pt["radius"] ** 2:
                        pt["dragging"] = True
                        break
            elif event.type == pygame.MOUSEBUTTONUP:
                for pt in control_points:
                    pt["dragging"] = False
            elif event.type == pygame.MOUSEMOTION:
                mouse_x, mouse_y = event.pos
                for pt in control_points:
                    if pt["dragging"]:
                        # Update the position of the circle to follow the mouse
                        pt["pos"] = [mouse_x, mouse_y]
        

        for pt in control_points:
            pygame.draw.circle(canvas, (255, 255, 255), pt["pos"], pt["radius"], 2)

        
        for ptx in range(len(control_points) - 1):
            pt0 = control_points[ptx]
            pt1 = control_points[ptx + 1]
            pygame.draw.line(canvas, (120, 120, 120), pt0["pos"], pt1["pos"], 1)

        step_size = 0.01

        t = step_size
        while t <= 1.0:
            pt0 = control_points[0]["pos"]
            pt1 = control_points[1]["pos"]
            pt2 = control_points[2]["pos"]
            pt3 = control_points[3]["pos"]

            bezier_pt1 = bezier(t, pt0, pt1, pt2)
            bezier_pt2 = bezier(t, pt1, pt2, pt3)

            bezier_last_pt1 = bezier(t - step_size, pt0, pt1, pt2)
            bezier_last_pt2 = bezier(t - step_size, pt1, pt2, pt3)

            pygame.draw.line(canvas, (255, 255, 255), bezier_last_pt1, bezier_pt1, 2)
            pygame.draw.line(canvas, (255, 255, 255), bezier_last_pt2, bezier_pt2, 2)

            cubic_pt = [
                (1 - t) * bezier_pt1[0] + t * bezier_pt2[0],
                (1 - t) * bezier_pt1[1] + t * bezier_pt2[1],
            ]

            cubic_last_pt = [
                (1 - t) * bezier_last_pt1[0] + t * bezier_last_pt2[0],
                (1 - t) * bezier_last_pt1[1] + t * bezier_last_pt2[1],
            ]

            pygame.draw.line(canvas, (255, 0, 0), cubic_last_pt, cubic_pt, 2)


            t += 0.01

        
        
        pygame.display.update()


if __name__ == "__main__":
    main()