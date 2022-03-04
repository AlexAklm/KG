from Common.Model import *
from Common.Scene import Scene

class Alex8(Scene):
    def init(self):
        self.model = Model('./Models/Cube.obj', 'Models/59367_open3dmodel.com/textures/tiles.png')
        self.model.scale(10)