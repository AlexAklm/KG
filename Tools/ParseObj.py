import numpy as np

class ParseObj:
    def __init__(self, pathToFile):
        self.vertex = []
        self.faces = []
        self.normals = []
        self.uv = []

        self.parse(pathToFile)

    
    def parse(self, pathToFile):
        with open(pathToFile, 'r') as file:
            for line in file:
                if line.startswith('v '):
                    self.vertex.append([float(i) for i in line.split()[1:]] + [1])
                if line.startswith('f '):
                    faces_ = line.split()[1:]
                    self.faces.append([[int(face_.split('/')[0]) - 1, int(face_.split('/')[1]) - 1, int(face_.split('/')[2]) - 1] for face_ in faces_])
                if line.startswith('vt '):
                    self.uv.append([float(i) for i in line.split()[1:]] + [1])
                if line.startswith('vn '):
                    self.normals.append([float(i) for i in line.split()[1:]] + [1])

        
        self.vertex = np.array(self.vertex)
        self.faces = np.array(self.faces)
        self.normals = np.array(self.normals)
        self.uv = np.array(self.uv, dtype=np.float32)
    
