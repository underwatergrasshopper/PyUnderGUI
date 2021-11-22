from UnderGUI.Inner.Shunter import *

from OpenGL.GL import *

class OpenGL_Shunter(Shunter):
    def __init__(self):
        pass
        
    def setup_texture_draw(self):
        glEnable(GL_CULL_FACE)
        
        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
        
        glEnable(GL_TEXTURE_2D)