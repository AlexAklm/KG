from Common.Model_VBO import *

class Scene:
    def init(self, path):
        self.model = Model(path)

    def draw(self):
        self.model.render()

