from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

class Shader(object):

    def __init__(self, vertex_source=None, fragment_source=None):
        self.program = glCreateProgram()

        if vertex_source:
            self.vertex_shader = self.create_shader(
                vertex_source, GL_VERTEX_SHADER)
            glAttachShader(self.program, self.vertex_shader)

        if fragment_source:
            self.fragment_shader = self.create_shader(
                fragment_source, GL_FRAGMENT_SHADER)
            glAttachShader(self.program, self.fragment_shader)

        glLinkProgram(self.program)
        message = self.get_program_log(self.program)
        if message:
            print('Shader: shader program message: %s' % message)
            exit()

    def create_shader(self, source, shadertype):
        shader = glCreateShader(shadertype)
        code = ""

        with open(source, 'r') as file:
            for line in file:
                code += line

        glShaderSource(shader, code)
        glCompileShader(shader)
        message = self.get_shader_log(shader)
        if message:
            print('Shader: shader message: %s' % message)
            exit()
        return shader

    def set_uniform_f(self, name, value):
        location = glGetUniformLocation(self.program, name)
        glUniform1f(location, value)

    def set_uniform_i(self, name, value):
        location = glGetUniformLocation(self.program, name)
        glUniform1i(location, value)

    def __setitem__(self, name, value):
        """pass a variable to the shader"""
        if isinstance(value, float):
            self.set_uniform_f(name, value)
        elif isinstance(value, int):
            self.set_uniform_i(name, value)
        else:
            raise TypeError('Only single floats and ints are supported so far')

    def use(self):
        '''Use the shader'''
        glUseProgram(self.program)

    def stop(self):
        '''Stop using the shader'''
        glUseProgram(0)

    def get_shader_log(self, shader):
        '''Return the shader log'''
        return self.get_log(shader, glGetShaderInfoLog)

    def get_program_log(self, shader):
        '''Return the program log'''
        return self.get_log(shader, glGetProgramInfoLog)

    def get_log(self, obj, func):
        value = func(obj)
        return value


shader = Shader("Shaders/v_shader.vert", "Shaders/f_shader.frag")