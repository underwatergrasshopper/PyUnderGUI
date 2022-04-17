from OpenGL.GL import *

from UnderGUI.Color import *

__all__ = ['fill_area']

def fill_area(area, color):
    """
    :param UnderGUI.Area                       area:                 
        Area in window client region. 
    :param UnderGUI.Color                      color:                                                           
        Color of the fill.
    """
    view_range  = area.to_range()
    color       = color.to_color_f()
    
    glColor4f(color.r, color.g, color.b, color.a)
    
    glBegin(GL_TRIANGLE_STRIP)
    glVertex2f(view_range.x1, view_range.y1)
    glVertex2f(view_range.x2, view_range.y1)
    glVertex2f(view_range.x1, view_range.y2)
    glVertex2f(view_range.x2, view_range.y2)
    glEnd()
    
    