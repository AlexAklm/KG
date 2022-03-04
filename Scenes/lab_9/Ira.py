from Common.Model import *
from Common.Const import Colors
from Tools.ColorFunctions import *


def draw(Width, Height):
    SetBackgroundColor(Colors.GREEN)

    delphi = Model('./Models/11792_pendant_v2_l3.obj')
    delphi.setPolygonMode(mode=GL_FILL)
    delphi.rotate_x(-90)
    delphi.rotate_y(90)
    SetColor(Colors.BLUE)
    delphi.render()

    delphi_shape = Model('./Models/11792_pendant_v2_l3.obj')
    delphi_shape.setPolygonMode()
    delphi_shape.rotate_x(-90)
    delphi_shape.rotate_y(90)
    SetColor(Colors.BLACK)
    delphi_shape.render()

    SetColor(Colors.BLUE)


