import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

from Common.Enums import *
from Common.Camera import *

from Scenes.lab_8.Alex import Alex8
from Scenes.lab_11.Alex import Alex11
from Scenes.lab_11.Ilona import Lab_11


class App:
    def __init__(self, sizeX, sizeY, title, scene):
        self.Width = sizeX
        self.Height = sizeY
        self.Title = title
        self.Scene = scene()

        self.Camera = Camera()
        self.FPS_CLOCK = pygame.time.Clock()

        glutInit(sys.argv)
        glLight(GL_LIGHT0, GL_POSITION,  (5, 5, 5, 1))
        glLightfv(GL_LIGHT0, GL_AMBIENT, (0, 0, 0, 1))
        glLightfv(GL_LIGHT0, GL_DIFFUSE, (1, 1, 1, 1))
        glEnable(GL_DEPTH_TEST) 

        pygame.init()
        pygame.display.set_mode((self.Width, self.Height), DOUBLEBUF | OPENGL)
        pygame.display.set_caption(self.Title)
    
    def SetProjectionMode(self, mode, **args):
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        if mode == ProjectionMode.ORTHO:
            glOrtho(args['xMin'], args['xMax'], args['yMin'], args['yMax'], args['zMin'], args['zMax'])
        elif mode == ProjectionMode.PERSPECTIVE:
            gluPerspective(args['fovy'], args['aspect'], args['near'], args['far']);


    def run(self):
        self.Scene.init()
        glTranslatef(0,0,-1)
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()


            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

            glEnable(GL_LIGHTING)
            glEnable(GL_LIGHT0)
            glEnable(GL_COLOR_MATERIAL)
            glEnable(GL_TEXTURE_2D)
            glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE )

            self.Scene.draw()
            self.Camera.Control()

            glDisable(GL_TEXTURE_2D)
            glDisable(GL_LIGHT0)
            glDisable(GL_LIGHTING)
            glDisable(GL_COLOR_MATERIAL)

            pygame.display.flip()
            self.FPS_CLOCK.tick(60)


if __name__ == "__main__":
    app = App(800, 600, "App", Lab_11)
    #app.SetProjectionMode(ProjectionMode.ORTHO, xMin=-40, xMax=40, yMin=-30, yMax=30, zMin=-1000, zMax=1000)
    app.SetProjectionMode(ProjectionMode.PERSPECTIVE, fovy=45, aspect=4/3, near=-50, far=0)
    app.run()