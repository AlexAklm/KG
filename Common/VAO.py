from OpenGL.GL import *
from Common.VBO import VBO

import numpy as np

class VAO:
    def __init__(self):
        self.vertex_array = glGenVertexArrays(1)
        self.array_vbo = {}
    
    def set_vbo(self, key, data, target=GL_ARRAY_BUFFER, mode=GL_DYNAMIC_DRAW):
        vbo = VBO(data, target, mode)
        vbo.bind()

        self.array_vbo[key] = vbo

    def bind(self):
        glBindVertexArray(self.vertex_array)

    
    def unbind(self):
        glBindVertexArray(0)

    