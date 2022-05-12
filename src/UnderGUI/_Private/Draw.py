from OpenGL.GL import *

from UnderGUI.Color import *
from UnderGUI.Commons import *

__all__ = [
    'fill_area',
    'fill_span',
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
    fill_span(area.to_span(), color)

def fill_span(span, color):
    """
    :param UnderGUI.span                       span:                 
        span in window client region. 
    :param UnderGUI.Color                      color:                                                           
        Color of the fill.
    """
    color = color.to_color_f()
    
    glColor4f(color.r, color.g, color.b, color.a)
    
    glBegin(GL_TRIANGLE_STRIP)
    glVertex2f(span.x1, span.y1)
    glVertex2f(span.x2, span.y1)
    glVertex2f(span.x1, span.y2)
    glVertex2f(span.x2, span.y2)
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
    