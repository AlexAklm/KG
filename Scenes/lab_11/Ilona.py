from Common.Model import *
from Common.Scene import Scene

class Lab_11(Scene):
    def init(self):
        self.model = Model('Models/Venus_v1_L3.123c5f86bd5e-26c0-4e50-bae1-911256cb7689/13901_Venus_v1_l3.obj', 'Models/Venus_v1_L3.123c5f86bd5e-26c0-4e50-bae1-911256cb7689/Venus_diff.jpg')
        self.model.rotate_x(90)
        self.model.scale(1/1500)

    def draw(self):
        self.model.render()