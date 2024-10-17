from math import *


class AM_Sphere():
    position=[0,0,0]
    radius=1
    color=(255,255,255)

    def __init__(self, pos=[0,0,0], r=1, c=(255,255,255)):
        self.position=pos
        self.radius=r
        self.color=c


    def at(self, u, v):
        rp = self.radius*cos(pi*(v-0.5))

        x = rp*cos(2*pi*u)
        y = rp*sin(2*pi*u)
        z = self.radius*sin(pi*(v-0.5))

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

    def draw(self, canvas, res=(64, 32), color=(255, 255, 255), wire=False):
    
        if wire:
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


    def hit(self, ray):
        # Ray origin and direction
        ray_origin = ray[0]
        ray_direction = ray[1]

        # Vector from ray origin to sphere center (L)
        L = (
            self.position[0] - ray_origin[0], 
            self.position[1] - ray_origin[1], 
            self.position[2] - ray_origin[2]
        )

        # tca is the projection of L onto the ray direction
        tca = (
            L[0] * ray_direction[0] + 
            L[1] * ray_direction[1] + 
            L[2] * ray_direction[2]
        )

        #print(tca)

        # l_squared is the square of the length of L
        l_squared = (
            L[0]**2 + 
            L[1]**2 + 
            L[2]**2
        )

        # d_squared is the squared distance from the closest approach
        d_squared = l_squared - tca**2

        # Check if the ray misses the sphere
        if d_squared > self.radius**2:
            return -1, (0, 0, 0)

        # thc is the distance from the closest approach to the intersection points
        thc = sqrt(self.radius**2 - d_squared)

        # t0 and t1 are the distances to the intersection points along the ray
        t0 = tca - thc
        t1 = tca + thc

        # Ensure that t0 and t1 are positive and select the closest valid intersection
        if t0 > 0:
            t = t0
        elif t1 > 0:
            t = t1
        else:
            return -1, (0, 0, 0)  # No valid intersection

        #print(t)

        # Return the intersection distance and color

        P = (
            ray_origin[0] + ray_direction[0] * t,
            ray_origin[1] + ray_direction[1] * t,
            ray_origin[2] + ray_direction[2] * t
        )

        N = (
            P[0] - self.position[0],
            P[1] - self.position[1],
            P[2] - self.position[2]
        )

        N_length = sqrt(N[0]**2 + N[1]**2 + N[2]**2)

        N = (
            N[0]/N_length,
            N[1]/N_length,
            N[2]/N_length
        )

        light = (2, 2, -2)

        light_length = sqrt(light[0]**2 + light[1]**2 + light[2]**2)

        light = (
            light[0]/light_length,
            light[1]/light_length,
            light[2]/light_length
        )

        illum = (
            N[0] * light[0] +
            N[1] * light[1] +
            N[2] * light[2]
        )

        draw_color = (
            int(self.color[0] * illum),
            int(self.color[1] * illum),
            int(self.color[2] * illum)
        )

        return t, draw_color
