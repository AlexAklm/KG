from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from math import pi, cos, sin, fabs
from Tools.ColorFunctions import SetBackgroundColor, SetColor

t = 0
base_min, base_max = 0, 10
sign = 1

def draw(Width, Height):
    global t, sign

    SetBackgroundColor([255,255,51, 1]) #фон окна
    glMatrixMode(GL_PROJECTION) #переходим к манипулированию самими объектами

    glRotatef(1, 0, 1, 1)

    glMatrixMode(GL_MODELVIEW)
    if fabs(t) >= 1:
        sign *= -1
    t += sign * 0.01

    base = base_min * t + (1 - t) * base_max

    glRotatef(-90, 1, 0, 0)
    glutSolidCone(base, 15, 10, 10) 
    glColor(0,0,0,0) 
    glutWireCone(base, 15, 10, 10)
    glColor(0, 255, 0, 1)