from OpenGL.GL import *

__all__ = ['Shunter']

class Shunter: 
    """
    Setups under-hood environment before and after specific actions.
    """
    
    def setup_window_client_area(self, size):
        """
        Setups for 2D drawing. Coordinates origin is at left-bottom corner of window client area.
        :param UnderGUI.Size                       size:
            Size of window client area.
        """
        glMatrixMode(GL_PROJECTION);
        glLoadIdentity();
        glOrtho(0, size.width, 0, size.height, -1, 1);
        
    def setup_draw(self, background_color = None, is_culling_face = True):
        """
        :param UnderGUI.Color or None              background_color:
            Color of window client area. If None then no changes to color of window client area.
        """
        if is_culling_face:
            glEnable(GL_CULL_FACE)
        else:
            glDisable(GL_CULL_FACE)
        
        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
        
        glEnable(GL_TEXTURE_2D)
        
        if background_color:
            background_color = background_color.to_color_f()
            glClearColor(background_color.r, background_color.g, background_color.b, background_color.a)
            glClear(GL_COLOR_BUFFER_BIT)
        
        glMatrixMode(GL_MODELVIEW);
