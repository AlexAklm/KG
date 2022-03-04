from OpenGL.GL import *

import numpy as np

class VBO:
    def __init__(self, data, target=GL_ARRAY_BUFFER, mode=GL_DYNAMIC_DRAW):
        self.data = data
        self.size_data = data.nbytes
        self.target = target
        self.mode = mode
        self.buffer = glGenBuffers(1)
        self.is_bind = False

        self.bind()
        glBufferData(self.target, self.size_data, self.data, self.mode)
        self.unbind()


    def set_pointer(self, location, vec_size, item_type, step):
        if not self.is_bind:
            print("Буффер не был забинден")
            exit()

        glEnableVertexAttribArray(location)
        glVertexAttribPointer(location, vec_size, item_type, GL_FALSE, step * self.data.itemsize, ctypes.c_void_p(0))
        

    def bind(self):
        self.is_bind = True
        glBindBuffer(self.target, self.buffer)

    def unbind(self):
        self.is_bind = False
        glBindBuffer(self.target, 0)

    def __enter__(self):
        self.bind()

    def __exit__(self):
        self.unbind()
