from math import *
import pygame


class AM_Torus():
    position=[0,0,0]
    max_radius=1
    min_radius=0.1
    color=[255, 255,255]

    def __init__(self, pos=[0,0,0], rmax=1, rmin=0.1, c=[255, 255, 255]):
        self.position=pos
        self.min_radius=rmin
        self.max_radius=rmax
        self.color = c


    def at(self, u, v):
        x0 = self.max_radius + self.min_radius * cos(2*pi*u)

        x = x0*cos(2*pi*v)
        y = x0*sin(2*pi*v)
        z = self.min_radius*sin(2*pi*u)

        return (x, y, z)

    def points(self, res=(64, 32)):
        pts = []

        u=0

        while u <= 1:
            v = 0
            while v <= 1:
                pt = self.at(u, v)
                pt = (
                    pt[0] + self.position[0],
                    pt[1] + self.position[1], 
                    pt[2] + self.position[2]
                )
                    
                pts.append(pt)
                v += 1/res[1]
            
            u += 1/res[0]

        return pts

    def draw(self, canvas, res=(64, 32), color=(255, 255, 255), wire=False, screen=None):
    
        if wire or screen is not None:
            u=0
            while u <= 1:
                v = 0
                while v <= 1:
                    pt0 = self.at(u, v)
                    pt1 = self.at(u + 1/res[0], v)
                    pt2 = self.at(u, v + 1/res[1])


                    pt0 = (
                        pt0[0] + self.position[0],
                        pt0[1] + self.position[1], 
                        pt0[2] + self.position[2]
                    )

                    pt1 = (
                        pt1[0] + self.position[0],
                        pt1[1] + self.position[1], 
                        pt1[2] + self.position[2]
                    )

                    pt2 = (
                        pt2[0] + self.position[0],
                        pt2[1] + self.position[1], 
                        pt2[2] + self.position[2]
                    )


                    z0 = pt0[1]
                    if z0 == 0:
                        z0 = 1

                    z1 = pt1[1]
                    if z1 == 0:
                        z1 = 1

                    z2 = pt2[1]
                    if z2 == 0:
                        z2 = 1

                    s0 = (
                        (pt0[0]/z0) * canvas.width/2 + canvas.width/2,
                        (pt0[2]/z0) * canvas.height/2 + canvas.height/2
                    )

                    s1 = (
                        (pt1[0]/z1) * canvas.width/2 + canvas.width/2,
                        (pt1[2]/z1) * canvas.height/2 + canvas.height/2
                    )

                    s2 = (
                        (pt2[0]/z2) * canvas.width/2 + canvas.width/2,
                        (pt2[2]/z2) * canvas.height/2 + canvas.height/2
                    )
                    
                    if screen is not None:
                        pygame.draw.lines(screen, self.color, False, [s1, s0, s2])
                    else:
                        canvas.canvas.line([s1, s0, s2], color)
                    v += 1/res[1]
            
                u += 1/res[0]

        else:
            pts = self.points(res=res)
    
            for pt in pts:
                z = pt[1]

                if z == 0:
                    z = 1

                s = (
                    (pt[0]/z) * canvas.width/2 + canvas.width/2,
                    (pt[2]/z) * canvas.height/2 + canvas.height/2
                )

                canvas.canvas.point(s, color)