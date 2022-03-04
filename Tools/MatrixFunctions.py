from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

from math import sin, cos, tan

import numpy as np


def Rotate(angle, axis):
    glRotatef(angle, axis[0], axis[1], axis[2])


def Translate(offset):
    glTranslatef(offset[0], offset[1], offset[2])


def Scale(scaling):
    glScalef(scaling[0], scaling[1], scaling[2])


def translate(pos):
    tx, ty, tz, _ = pos
    return np.array([
        [1, 0, 0, tx],
        [0, 1, 0, ty],
        [0, 0, 1, tz],
        [0, 0, 0, 1]
    ])


def rotate_x(a):
    return np.array([
        [1, 0, 0, 0],
        [0, cos(a), sin(a), 0],
        [0, -sin(a), cos(a), 0],
        [0, 0, 0, 1]
    ])


def rotate_y(a):
    return np.array([
        [cos(a), 0, -sin(a), 0],
        [0, 1, 0, 0],
        [sin(a), 0, cos(a), 0],
        [0, 0, 0, 1]
    ])


def rotate_z(a):
    return np.array([
        [cos(a), sin(a), 0, 0],
        [-sin(a), cos(a), 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1]
    ])


def scale(n):
    return np.array([
        [n, 0, 0, 0],
        [0, n, 0, 0],
        [0, 0, n, 0],
        [0, 0, 0, 1]
    ])


def shear_xy(angle_x, angle_y):
    ctg_theta = cos(angle_x) / sin(angle_x) 
    ctg_phi = cos(angle_y) / sin(angle_y) 
    return np.array([
        [1, 0, -ctg_theta, 0],
        [0, 1, -ctg_phi, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1]
    ])


def shear_xz(angle_x, angle_z):
    ctg_theta = cos(angle_x) / sin(angle_x) 
    ctg_phi = cos(angle_z) / sin(angle_z) 
    return np.array([
        [1, -ctg_theta, 0, 0],
        [0, 1, 0, 0],
        [0, -ctg_phi, 1, 0],
        [0, 0, 0, 1]
    ])


def shear_yz(angle_y, angle_z):
    ctg_theta = cos(angle_y) / sin(angle_y) 
    ctg_phi = cos(angle_z) / sin(angle_z) 
    return np.array([
        [1, 0, 0, 0],
        [-ctg_theta, 1, 0, 0],
        [-ctg_phi, 0, 1, 0],
        [0, 0, 0, 1]
    ])