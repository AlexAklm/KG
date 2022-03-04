from Common.Model import *
from Tools.ColorFunctions import *


def draw(Width, Height, PathToFile):
    SetBackgroundColor(0, 255, 0)
    cube = Model(PathToFile)
    cube.scale(10)
    cube.setPolygonMode(mode=GL_FILL)
    cube.setColor([255,255,0])
    cube.shear_xy(45, 10)
    cube.render()

    cube_collider = Model(PathToFile)
    cube_collider.scale(10)
    cube_collider.setPolygonMode(mode=GL_LINE)
    cube_collider.setColor([0, 0, 0])
    cube_collider.shear_xy(45, 10)
    cube_collider.render()

    cube_collider.setColor([255, 255, 0])
