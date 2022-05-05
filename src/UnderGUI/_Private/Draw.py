from OpenGL.GL import *

from UnderGUI.Color import *

__all__ = [
    'fill_area',
    'fill_range',
    'restrict_draw_to_area',
    'restrict_draw_to_window_client_area'
]

def fill_area(area, color):
    """
    :param UnderGUI.Area                       area:                 
        Area in window client region. 
    :param UnderGUI.Color                      color:                                                           
        Color of the fill.
    """
    fill_range(area.to_range(), color)

def fill_range(pos_range, color):
    """
    :param UnderGUI.Range                      pos_range:                 
        Range in window client region. 
    :param UnderGUI.Color                      color:                                                           
        Color of the fill.
    """
    color = color.to_color_f()
    
    glColor4f(color.r, color.g, color.b, color.a)
    
    glBegin(GL_TRIANGLE_STRIP)
    glVertex2f(pos_range.x1, pos_range.y1)
    glVertex2f(pos_range.x2, pos_range.y1)
    glVertex2f(pos_range.x1, pos_range.y2)
    glVertex2f(pos_range.x2, pos_range.y2)
    glEnd()

def restrict_draw_to_area(area):
    """
    :param UnderGUI.Area                       area:                 
        The only area in window client region, what will be allowed to draw into. 
    """
    glEnable(GL_SCISSOR_TEST)
    glScissor(area.x, area.y, area.width, area.height)
    
def restrict_draw_to_window_client_area():
    glDisable(GL_SCISSOR_TEST)
    