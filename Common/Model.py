from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from Tools.MatrixFunctions import *
from Tools.ColorFunctions import *
from Tools.ParseObj import ParseObj
from Common.Shader import Shader
from PIL import Image as Image
import numpy as np

class Model:
    def __init__(self, pathToFile, pathToTexture=None):
        parser = ParseObj(pathToFile)

        self.vertex = parser.vertex
        self.faces = parser.faces
        self.normals = parser.normals
        self.uv = parser.uv

        self.setPolygonMode(mode=GL_FILL)

        if pathToTexture:
            self.setTexture(pathToTexture)

    def setColor(self, color):
        SetColor(color[0], color[1], color[2])

    def setTexture(self, path):
        textID  = glGenTextures(1)
        glBindTexture(GL_TEXTURE_2D, textID)
        
        img = Image.open(path)
        img_data = np.array(list(img.getdata()), np.int8)
        textID = glGenTextures(1)
        glPixelStorei(GL_UNPACK_ALIGNMENT, 1)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR_MIPMAP_LINEAR)
        glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL)
        gluBuild2DMipmaps(GL_TEXTURE_2D, GL_RGB, img.size[0], img.size[1], GL_RGB, GL_UNSIGNED_BYTE, img_data)

    def setPolygonMode(self, render_depth = GL_FRONT_AND_BACK, mode = GL_LINE):
        glPolygonMode(render_depth, mode)

    def render(self):
        for face in self.faces:
            face = face.transpose()
            verticies = self.vertex[face[0]]
            uv = self.uv[face[1]]
            normal = self.normals[face[2]]
            glBegin(GL_POLYGON)

            for norm, coord_uv, vertex in zip(normal, uv, verticies):
                glNormal3f(norm[0], norm[1], norm[2])
                glTexCoord2f(coord_uv[0], coord_uv[1])
                glVertex3f(vertex[0], vertex[1], vertex[2])
            glEnd()

        
    def translate(self, pos):
        self.vertex = self.vertex @ translate(pos)

    def rotate_x(self, angle):
        self.vertex = self.vertex @ rotate_x(angle)

    def rotate_y(self, angle):
        self.vertex = self.vertex @ rotate_y(angle)

    def rotate_z(self, angle):
        self.vertex = self.vertex @ rotate_z(angle)

    def shear_xy(self, angle_x, angle_y):
        self.vertex = self.vertex @ shear_xy(angle_x, angle_y)

    def shear_xz(self, angle_x, angle_z):
        self.vertex = self.vertex @ shear_xz(angle_x, angle_z)

    def shear_yz(self, angle_y, angle_z):
        self.vertex = self.vertex @ shear_yz(angle_y, angle_z)

    def scale(self, scale_factor):
        self.vertex = self.vertex @ scale(scale_factor)