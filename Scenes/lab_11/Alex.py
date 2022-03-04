from Common.Model import *
from Common.Scene import Scene

class Alex11(Scene):
    def init(self):
        glTranslatef(0, 0, -10)

    def draw(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glPushMatrix()

        self.read_texture('Models/59367_open3dmodel.com/textures/tiles.png')
        qobj = gluNewQuadric()
        gluQuadricTexture(qobj, GL_TRUE)
        glEnable(GL_TEXTURE_2D)
        gluSphere(qobj, 1, 50, 50)
        gluDeleteQuadric(qobj)
        glDisable(GL_TEXTURE_2D)

        color = [1.0, 0.0, 0.0, 1.0]
        glMaterialfv(GL_FRONT, GL_DIFFUSE, color)
        glTranslatef(-2, 0, 0)
        glutSolidSphere(1, 100, 20)

        color = [0.0, 1.0, 0.0, 1.0]
        glMaterialfv(GL_FRONT, GL_DIFFUSE, color)
        glTranslatef(4, 0, 0)
        glutSolidSphere(1, 100, 20)
        glPopMatrix()
    
    def read_texture(self, filename):
        img = Image.open(filename)
        img_data = np.array(list(img.getdata()), np.int8)
        textID  = glGenTextures(1)
        glBindTexture(GL_TEXTURE_2D, textID)
        glPixelStorei(GL_UNPACK_ALIGNMENT, 1)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
        glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL)
        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, img.size[0], img.size[1], 0, GL_RGB, GL_UNSIGNED_BYTE, img_data)