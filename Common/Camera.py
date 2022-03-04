from Tools.MatrixFunctions import *
from math import cos, sin, tan

import numpy as np
import pygame as pg

class Camera:
    def __init__(self):
        self.moving_speed = 1
        self.rotation_speed = 0.015
        
        self.right      = np.array([1., 0., 0., 0.])
        self.up         = np.array([0., 1., 0., 0.])
        self.forward    = np.array([0., 0., 1., 0.])
        self.position   = np.array([0., 0., 0., 1.])

        self.target = np.array([0, 0, -1, 0], dtype='f')

    def Control(self):
        key = pg.key.get_pressed()
        if key[pg.K_a]:
            self.position += -self.right * self.moving_speed
        if key[pg.K_d]:
            self.position += self.right * self.moving_speed
        if key[pg.K_w]:
            self.position += -self.forward * self.moving_speed
        if key[pg.K_s]:
            self.position += self.forward * self.moving_speed
        if key[pg.K_SPACE]:
            self.position += self.up * self.moving_speed
        if key[pg.K_c]:
            self.position += -self.up * self.moving_speed

        if key[pg.K_LEFT]:
            self.Yaw(self.rotation_speed)
        if key[pg.K_RIGHT]:
            self.Yaw(-self.rotation_speed)
        if key[pg.K_UP]:
            self.Pitch(self.rotation_speed)
        if key[pg.K_DOWN]:
            self.Pitch(-self.rotation_speed)


        matrix = self.GetMatrixCamera()
        glMatrixMode(GL_MODELVIEW)
        #glUniformMatrix4fv(0, 1, GL_FALSE, matrix)  
        glLoadMatrixf(self.GetMatrixCamera())    


    def Pitch(self, angle):
        matrix = rotate_x(angle)
        self.right = self.right @ matrix
        self.up = self.up @ matrix
        self.forward = self.forward @ matrix

    
    def Yaw(self, angle):
        matrix = rotate_y(angle)
        self.right = self.right @ matrix
        self.up = self.up @ matrix
        self.forward = self.forward @ matrix

    
    def Roll(self, angle):
        matrix = rotate_z(angle)
        self.right = self.right @ matrix
        self.up = self.up @ matrix
        self.forward = self.forward @ matrix

    
    def translate_matrix(self):
        x, y, z, _ = self.position
        return np.array([
            [1, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 0, 1, 0],
            [-x, -y, -z, 1],
        ])

    
    def rotate_matrix(self):
        rx, ry, rz, _ = self.right
        ux, uy, uz, _ = self.up
        fx, fy, fz, _ = self.forward
        
        return np.array([
            [rx, ux, fx, 0],
            [ry, uy, fy, 0],
            [rz, uz, fz, 0],
            [0, 0, 0, 1],
        ])


    def GetMatrixCamera(self):
        return self.translate_matrix() @ self.rotate_matrix()

