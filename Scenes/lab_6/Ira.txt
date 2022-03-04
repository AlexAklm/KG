from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from math import pi, cos, sin
from Tools.ColorFunctions import SetBackgroundColor, SetColor


def draw(Width, Height):
    SetBackgroundColor(255,255,51) #фон окна
    glMatrixMode(GL_MODELVIEW) #переходим к манипулированию самими объектами

    objects = [Cone, Octahedron, Teapot, Cilindre] #объекты 
    points = [
        (0, Height / 30, 0),
        (Width / 40, 0, 0),
        (0, -Height / 30, 0),
        (-Width / 40, 0, 0)
    ] #Твои точки по заданию
    for i in range(len(objects)):
        glPushMatrix() #Для того чтобы трогать только объект, а не всё пространство в целом - сохраняем состояние пространства на данный момент
        x = points[i][0]
        y = points[i][1]
        glTranslatef(x, y, 0) #Сдвигаем на наши точки
        glRotatef(30, 1, 1, 0) #Поворачиваем для лучшего вида
        SetColor(50,205,50)
        objects[i]() #Рисуем объект
        SetColor(50,205,50)
        glPopMatrix()#Возвращаем состояние пространства, но сдивг фигуры остается 

#Я даумаю ты догадаешься что эти функции рисуют нужные тебе объекты
def Cone():
    glutSolidCone(10, 15, 10, 10) #solid object
    glColor(0,0,0,0) # color carcas
    glutWireCone(10, 15, 10, 10) # carcas

def Teapot():
    glutSolidTeapot(2.5)
    SetColor(0, 0, 0)
    glutWireTeapot(2.5)

def Octahedron():
    glScalef(5, 5, 5)
    glutSolidOctahedron()
    glColor(0,0,0,0)
    glutWireOctahedron()

def Cilindre():
    glRotatef(90, 0, 0, 1)
    glScalef(5, 10, 5) #Я изначально строю цилиндр с основаниями радиуса 1 и высотой 1. Здесь мы просто масштабируем как нам надо
    n = 100 #Так как круга тоже нет в примитивах мы его рисуем сами, я взял идею что круг - это многоугольник с большим кол-вом углов
    h = 2 * pi / n
    angles = [i * h for i in range(n + 1)]
    points = [(cos(angle), sin(angle)) for angle in angles]
    
    #Нижний круг
    glBegin(GL_POLYGON)
    for point in points:
        glVertex3f(point[0], 0, point[1])
    glEnd()

    #Верхний круг
    glBegin(GL_POLYGON)
    for point in points:
        glVertex3f(point[0], 1, point[1])
    glEnd()

    glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)
    #Сторона цилиндра
    glBegin(GL_POLYGON)
    for point in points:
        glVertex3f(point[0], 0, point[1])
        glVertex3f(point[0], 1, point[1])        
    glEnd()

    glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
    SetColor(0, 0, 0)

    #Нижний круг
    glBegin(GL_POLYGON)
    for point in points:
        glVertex3f(point[0], 0, point[1])
    glEnd()

    #Верхний круг
    glBegin(GL_POLYGON)
    for point in points:
        glVertex3f(point[0], 1, point[1])
    glEnd()


    glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)
