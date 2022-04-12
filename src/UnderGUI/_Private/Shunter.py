from OpenGL.GL import *

__all__ = ['Shunter']

class Shunter: 
    """
    Setups under-hood environment before and after specific actions.
    """
    def setup_for_texture_draw(self):
        glEnable(GL_CULL_FACE)
        
        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
        
        glEnable(GL_TEXTURE_2D)