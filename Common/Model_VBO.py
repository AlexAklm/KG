from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from OpenGL.arrays import vbo
from Tools.MatrixFunctions import *
from Tools.ColorFunctions import *
from Tools.ParseObj import ParseObj
from Common.Shader import Shader
from Common.VAO import VAO
import numpy as np

class Model:
    def __init__(self, pathToFile, pathToTexture=None):
        parser = ParseObj(pathToFile)

        self.vertex = np.array(parser.vertex, dtype=np.float32)
        self.faces = np.array(parser.faces, dtype=np.int32)
        self.normals = np.array(parser.normals, dtype=np.float32)
        self.uv = np.array(parser.uv, dtype=np.float32)
        self.shader = Shader('Shaders/v_shader.vert', 'Shaders/f_shader.frag')
        self.shader.use()
        self.set_vao()
        self.setPolygonMode(mode=GL_FILL)

        if pathToTexture:
            self.setTexture(pathToTexture)

    def render(self):
        self.vao.bind()
        glDrawElements(GL_TRIANGLES, len(self.faces), GL_UNSIGNED_INT, None)
        self.vao.unbind()

    def setTexture(self, path):
        texture = glGenTextures(1)
        glBindTexture(GL_TEXTURE_2D, texture)

        # Set the texture wrapping parameters
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
        # Set texture filtering parameters
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
        
        image = Image.open(path)
        image = image.transpose(Image.FLIP_TOP_BOTTOM)
        img_data = image.convert("RGBA").tobytes()
        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, image.width, image.height, 0, GL_RGBA, GL_UNSIGNED_BYTE, img_data)

    def set_vao(self):
        self.vao = VAO()
        self.vao.bind()
        self.vao.set_vbo("index", self.faces.ravel(), target=GL_ELEMENT_ARRAY_BUFFER)
        self.vao.set_vbo("vertex", self.vertex.ravel())
        self.vao.array_vbo['vertex'].set_pointer(0, 4, GL_FLOAT, 3)
        self.vao.unbind()
        
    def translate(self, pos):
        self.vertex = self.vertex @ translate(pos)
        self.set_vao()


    def rotate_x(self, angle):
        self.vertex = self.vertex @ rotate_x(angle)
        self.set_vao()

    def rotate_y(self, angle):
        self.vertex = self.vertex @ rotate_y(angle)
        self.set_vao()

    def rotate_z(self, angle):
        self.vertex = self.vertex @ rotate_z(angle)
        self.set_vao()

    def shear_xy(self, angle_x, angle_y):
        self.vertex = self.vertex @ shear_xy(angle_x, angle_y)
        self.set_vao()

    def shear_xz(self, angle_x, angle_z):
        self.vertex = self.vertex @ shear_xz(angle_x, angle_z)
        self.set_vao()

    def shear_yz(self, angle_y, angle_z):
        self.vertex = self.vertex @ shear_yz(angle_y, angle_z)
        self.set_vao()

    def scale(self, scale_factor):
        self.vertex = self.vertex @ scale(scale_factor)
        self.set_vao()
    
    def setColor(self, color):
        SetColor(color[0], color[1], color[2])

    def setPolygonMode(self, render_depth = GL_FRONT_AND_BACK, mode = GL_LINE):
        glPolygonMode(render_depth, mode)