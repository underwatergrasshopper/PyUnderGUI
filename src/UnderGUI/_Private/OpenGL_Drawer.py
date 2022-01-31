from OpenGL.GL import *

from .Drawer import *

__all__ = ['OpenGL_Drawer']

class OpenGL_Drawer(Drawer):
    def __init__(self):
        pass
        
    def fill_view(self, color):
        glClearColor(color.r, color.g, color.b, color.a)
        glClear(GL_COLOR_BUFFER_BIT)
