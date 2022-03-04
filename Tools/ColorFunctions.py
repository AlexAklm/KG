from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

def SetColor(colors):
    if colors[0] < 0 or colors[0] > 255 or colors[1] < 0 or colors[1] > 255 or colors[2] < 0 or colors[2] > 255 or colors[3] < 0 or colors[3] > 1:
        print("Value exit from range ")

    r, g, b = colors[0] / 255, colors[1] / 255, colors[2] / 255
    glColor(r, g, b, colors[3])

def SetBackgroundColor(colors):
    if colors[0] < 0 or colors[0] > 255 or colors[1] < 0 or colors[1] > 255 or colors[2] < 0 or colors[2] > 255 or colors[3] < 0 or colors[3] > 1:
        print("Value exit from range ")

    r, g, b = colors[0] / 255, colors[1] / 255, colors[2] / 255
    glClearColor(r, g, b, colors[3])