from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from math import pi, cos, sin
from Tools.ColorFunctions import SetBackgroundColor, SetColor


def draw(Width, Height):
    SetBackgroundColor(255,192,203)
    glMatrixMode(GL_MODELVIEW) #переходим к манипулированию самими объектами

    objects = [Sphere, Tetrahedron, Torus, Cube, Cilindre] #объекты 
    countObjects = len(objects) #кол-во объектов

    
    for i in range(countObjects): #проходим по каждому объекту
        glPushMatrix() #Для того чтобы трогать только объект, а не всё пространство в целом - сохраняем состояние пространства на данный момент
        R = Height / 30 #Радиус
        x = R * cos(i * 2 * pi / countObjects) #параметрическое уравнение окружности (тебе надо по заданию расставить объекты по окружности с радиусом заданным)
        y = R * sin(i * 2 * pi / countObjects)
        glTranslatef(x, y, 0) #сдвигаем наш объект на позицию
        glRotatef(30, 1, 1, 0) #поворачиваем объект
        SetColor(219,112,147) 
        objects[i]() #Рисуем объект
        SetColor(219,112,147)
        glPopMatrix() #Возвращаем состояние пространства, но сдивг фигуры остается 


def Sphere():
    glutSolidSphere(5, 100, 10)  #solid object
    glColor(0, 0, 0, 0) # color carcas
    glutWireSphere(5, 10, 10) # carcas

def Tetrahedron():
    glScalef(5, 5, 5)
    glutSolidTetrahedron()
    SetColor(0, 0, 0)
    glutWireTetrahedron()

def Cilindre():
    glScalef(5, 10, 5) 
    n = 100
    h = 2 * pi / n
    angles = [i * h for i in range(n + 1)]
    points = [(cos(angle), sin(angle)) for angle in angles]
    
    #Нижний круг
    glBegin(GL_TRIANGLES)
    for i in range(1, len(points), 2):
        glVertex3f(0, 0, 0)
        glVertex3f(points[i - 1][0], 0, points[i - 1][1])
        glVertex3f(points[i][0], 0, points[i][1])
    glEnd()

    #Верхний круг
    glBegin(GL_TRIANGLES)
    for i in range(1, len(points), 2):
        glVertex3f(0, 1, 0)
        glVertex3f(points[i - 1][0], 1, points[i - 1][1])
        glVertex3f(points[i][0], 1, points[i][1])
    glEnd()

    #Сторона цилиндра
    glBegin(GL_TRIANGLE_STRIP)
    for i in range(len(points)):
        glVertex3f(points[i][0], 0 if i % 2 == 0 else 1, points[i][1])
    glEnd()

    glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
    SetColor(0, 0, 0)

    glBegin(GL_POLYGON)
    for point in points:
        glVertex3f(point[0], 0, point[1])
    glEnd()

    glBegin(GL_POLYGON)
    for point in points:
        glVertex3f(point[0], 1, point[1])
    glEnd()

    glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)


def Cube():
    glutSolidCube(5)
    glColor(0, 0, 0, 0)
    glutWireCube(5)

def Torus():
    glutSolidTorus(5, 10, 10, 10)
    glColor(0, 0, 0, 0)
    glutWireTorus(5, 10, 10, 10)