from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from Common.Const import Colors
from math import pi, cos, sin
from Tools.ColorFunctions import SetBackgroundColor, SetColor
from Tools.MatrixFunctions import Rotate



def draw(Width, Height):
    SetBackgroundColor(Colors.WHITE)

    glMatrixMode(GL_PROJECTION)
    glRotatef(1, 0, 0, 1)
    objects = [WireSphere, Teapot, Icosahedron, WireConus, Cube]
    for i in range(len(objects)):
        glPushMatrix()
        glTranslatef(Height / 25 * cos(i * 2 * pi / 5), Height / 25 * sin(i * 2 * pi / 5), 0)
        glRotatef(30, 1, 1, 0)
        glColor(1, 0, 0, 0)
        objects[i]()
        glColor(1, 0, 0, 0)
        glPopMatrix()


def WireSphere():
    glutSolidSphere(5, 100, 10)
    SetColor(Colors.BLACK)
    glutWireSphere(5, 50, 10)
    

def Teapot():
    glutSolidTeapot(2.5)
    SetColor(Colors.BLACK)
    glutWireTeapot(2.5)
    

def Icosahedron():
    glScalef(5, 5, 5)
    glutSolidIcosahedron()
    SetColor(Colors.BLACK)
    glutWireIcosahedron()

def WireConus():
    glScale(5, 5, 5)
    n = 100
    step = 2 * pi / n
    h = 1
    similarityСoefficient = 2
    angles = [step * i for i in range(n + 1)]
    
    glBegin(GL_POLYGON)
    for angle in angles:
        x = cos(angle)
        z = sin(angle)
        glVertex3f(x, 0, z)
    glEnd()

    glBegin(GL_POLYGON)
    for angle in angles:
        x = 1 / similarityСoefficient * cos(angle)
        z = 1 / similarityСoefficient * sin(angle)
        glVertex3f(x, h, z)
    glEnd()

    glBegin(GL_POLYGON)
    for angle in angles:
        x0 = cos(angle)
        z0 = sin(angle)

        x1 = 1 / similarityСoefficient * cos(angle)
        z1 = 1 / similarityСoefficient * sin(angle)
        glVertex3f(x0, 0, z0)
        glVertex3f(x1, h, z1)
    glEnd()


    glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
    SetColor(Colors.BLACK)

    glBegin(GL_POLYGON)
    for angle in angles:
        x = cos(angle)
        z = sin(angle)
        glVertex3f(x, 0, z)
    glEnd()

    glBegin(GL_POLYGON)
    for angle in angles:
        x = 1 / similarityСoefficient * cos(angle)
        z = 1 / similarityСoefficient * sin(angle)
        glVertex3f(x, h, z)
    glEnd()

    SetColor(Colors.RED)
    glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)


def Cube():
    glutSolidCube(2)
    SetColor(Colors.RED)
    glutWireCube(2)