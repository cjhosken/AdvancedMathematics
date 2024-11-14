#!/usr/bin/env python
from random import random, seed
from math import *
import pygame
import numpy as np
import sys
pygame.init()


def randomF():
    return (random() - 0.5) * 2

def sphere(pos, radius, shader, name=str(random())) -> dict:
    return {
        "name": name,
        "position": pos,
        "radius": radius,
        "shader": shader,
        "type": "prim"
    }

def light(pos, color, brightness) -> dict:
    return {
        "position": pos,
        "color": color,
        "brightness": brightness,
        "type":"light"
    }

def create_scene():

    scene = []

    for i in range(12):

        shader = {
            "color": (random() * 255.0, random() * 255.0, random() * 255.0),
            "ambient": (0.0, 0.0, 0.0),
            "diffuse": 0.0,
            "specular": 1,
            "roughness": 0.1 
        }

        scene.append(
            sphere((randomF() * 7.0, randomF() * 7.0, random() * 5.0 + 15.0), random() * 2.5, shader)
        )

    light_num = 3

    for i in range(light_num):
        scene.append(
            light((randomF() * 25.0, random() * 25.0 + 25, randomF() * 25.0), (255, 255, 255), random() * 50/light_num)
        )


    return scene

def get_lights(scene):
    lights = []
    
    for obj in scene:
        if obj["type"] == "light":
            lights.append(obj)
    
    return lights

def hit_object(obj, ray):
    empty_hit = {
            "obj":None,
            "t":float("inf") 
        }

    ray_origin = np.array(ray[0])
    ray_direction = np.array(ray[1])

    L = np.subtract(np.array(obj["position"]), ray_origin)

    tca = np.dot(L, ray_direction)

    L_squared = np.dot(L, L)

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
        if obj["type"] == "prim":
            hit_obj = hit_object(obj, ray)

            if hit_obj["t"] > 0 and hit_obj["t"] < hit["t"]:
                hit = hit_obj

    return hit

def shade_hit(hit, ray, scene):
    obj = hit["obj"]
    t = hit["t"]
    shader = obj["shader"]
    lights = get_lights(scene)

    out_Cd = np.array([0.0, 0.0, 0.0])

    P = np.add(np.array(ray[0]), t * np.array(ray[1]))
    N = np.subtract(P, obj["position"])
    N /= np.linalg.norm(N)
    

    for light in lights:
        L = np.array(light["position"]) - P
        light_ray = (np.array(light["position"]), -L / np.linalg.norm(L))

        block_hit = hit_scene(scene, light_ray)

        if (block_hit["obj"] is not None):
            if (block_hit["obj"] != obj):
                continue


        incidentLight = np.array(light["color"]) * light["brightness"]/np.dot(L, L)

        L /= np.linalg.norm(L)
        H = np.add(N, L)/2
        H /= np.linalg.norm(H)

        reflectivity = max(np.dot(N, H), 0)**(1/shader["roughness"]) * np.array(shader["color"])

        reflectedLight = incidentLight * reflectivity * shader["specular"]
        diffuseLight = np.dot(N, L) * shader["diffuse"] * np.array(shader["color"])

        out_Cd += reflectedLight + diffuseLight
    
    out_Cd += np.array(shader["ambient"])

    out_Cd = np.clip(out_Cd, a_min=0, a_max=255.0)

    return (int(out_Cd[0]), int(out_Cd[1]), int(out_Cd[2]))

def main():
    width = 512
    height = 512
    background = (0, 0, 0)
    canvas = pygame.display.set_mode((width,height))

    objs = []
    scene = create_scene()

    running = True

    canvas.fill(background)

    for y in range(0, height):
        for x in range(0, width):
            u = 2 * ((x / width) - 0.5)
            v = 2 * (((height - y) / height) - 0.5)
            fov = 1

            direction = np.array([u, v, fov])
            direction /= np.linalg.norm(direction)

            ray=[np.array([0, 0, 0]), direction]

            hit = hit_scene(scene, ray)

            Cd = background

            if hit["obj"] is not None:
                Cd = shade_hit(hit, ray, scene)

            canvas.set_at((x, y), Cd)

        print(f"{y/height * 100}% completed!")

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.update()
    
    pygame.quit()


if __name__ == "__main__":
    main()