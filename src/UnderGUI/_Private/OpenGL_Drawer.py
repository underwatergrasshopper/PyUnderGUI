from OpenGL.GL import *

from .Drawer import *

__all__ = ['OpenGL_Drawer']

class OpenGL_Drawer(Drawer):
    # overrides
    def fill_view(self, color):
        glClearColor(color.r, color.g, color.b, color.a)
        glClear(GL_COLOR_BUFFER_BIT)
