from OpenGL.GL import *

__all__ = ['Drawer']

class Drawer:
    """
    Draws to window client area.
    """
    def fill_view(self, color):
        """
        Fills window client area with color.
        
        :param                                     color:
        :type                                      color: 
            UnderGUI.ColorF or UnderGUI.ColorI or UnderGUI.ColorB
        """
        glClearColor(color.r, color.g, color.b, color.a)
        glClear(GL_COLOR_BUFFER_BIT)

