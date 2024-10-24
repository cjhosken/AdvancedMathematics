#!/usr/bin/env python
import AM_module as am 
from PIL import Image
from random import random
from math import *

def addP(a, b) -> tuple:
    return (a[0]+b[0], a[1]+b[1], a[2]+b[2])

def subP(a, b) -> tuple:
    return (a[0]-b[0], a[1]-b[1], a[2]-b[2])

def dot(a, b) -> tuple:
    return a[0]*b[0] + a[1]*b[1] + a[2]*b[2]

def multFP(a, b) -> tuple:
    return (a*b[0], a*b[1], a*b[2])

def normalize(n) -> tuple:
    length = sqrt(dot(n, n))

    return (n[0] / length, n[1]/length, n[2]/length)
    

def sphere(pos, radius, color) -> dict:
    return {
        "position": pos,
        "radius": radius,
        "color": color
    }

def create_scene():

    scene = []

    scene.append(
        sphere((0, 0, 50), 10, (255, 0, 0))
    )

    return scene


def hit_object(obj, ray):
    empty_hit = {
            "obj":None,
            "t":float("inf") 
        }

    ray_origin = ray[0]
    ray_direction = ray[1]

    L = subP(obj["position"], ray_origin)

    tca = dot(L, ray_direction)

    L_squared = dot(L, L)

    d_squared = L_squared - tca**2


    if d_squared > obj["radius"]**2:
        return empty_hit

    thc = sqrt(obj["radius"]**2 - d_squared)

    t0 = tca - thc
    t1 = tca + thc

    if t0 > 0:
        t = t0
    elif t1 > 0:
        t = t1
    else:
        return empty_hit

    return {
        "obj": obj,
        "t": t
        }


def hit_scene(scene, ray):
    hit = {
        "obj":None,
        "t":float("inf") 
    }

    for obj in scene:
        hit_obj = hit_object(obj, ray)

        if hit_obj["t"] > 0 and hit_obj["t"] < hit["t"]:
            hit = hit_obj

    return hit

def shade_hit(hit, ray):
    obj = hit["obj"]
    t = hit["t"]
    Cd = obj["color"]
    
    P = addP(ray[0], multFP(t,ray[1]))
    N = subP(P, obj["position"])

    N = normalize(N)

    light = normalize((2, 2, -2))

    illum = dot(N, light)

    Cd = multFP(illum, Cd)

    return (int(Cd[0]), int(Cd[1]), int(Cd[2]))

def main():
    width = 256
    height = 256
    background = (0, 0, 0)

    image=Image.new("RGB",(256, 256), (0, 0, 0))
    scene = create_scene()


    for y in range(0, height):
            for x in range(0, width):
                u = 2 * ((x / width) - 0.5)
                v = 2 * ((y / height) - 0.5)
                fov = 1

                direction = (u, v, fov)
                direction_length = sqrt(direction[0]**2 + direction[1]**2 + direction[2]**2)

                direction = (
                    direction[0]/direction_length,
                    direction[1]/direction_length,
                    direction[2]/direction_length
                )

                ray=[(0, 0, 0), direction]

                hit = hit_scene(scene, ray)

                Cd = background

                if hit["obj"] is not None:
                    Cd = shade_hit(hit, ray)

                image.putpixel((x, y), Cd)
                print(f"Pixel: {x}, {y} completed!")

    image = image.transpose(Image.FLIP_TOP_BOTTOM)

    image.save("Week3_VectorCalc/image.png")
    image.show()


if __name__ == "__main__":
    main()