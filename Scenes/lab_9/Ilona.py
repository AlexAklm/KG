from Common.Model import *
from Common.Const import Colors
from Tools.ColorFunctions import *


def draw(Width, Height):
    SetBackgroundColor(Colors.PINK)
    cat = Model('./Models/cat.obj')
    cat.scale(10)
    cat.setPolygonMode(mode=GL_FILL)
    SetColor(Colors.REDS)
    cat.render()

    cat_collider = Model('./Models/cat.obj')
    cat_collider.scale(10)
    cat_collider.setPolygonMode(mode=GL_LINE)
    SetColor(Colors.BLACK)
    cat_collider.render()
    SetColor(Colors.REDS)
