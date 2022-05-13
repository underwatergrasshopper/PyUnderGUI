import TestKit

from UnderGUI import *
from UnderGUI._Private import *

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

################################################################################

WIDTH           = 800
HEIGHT          = 600

class Global:
    is_redraw       = False
    shunter         = None
    window          = None
    widget          = None
g = Global()


class TextWidget(Widget):
    def __init__(self, parent, span_or_area, color, anchor_group = None, window = None):
        super().__init__(parent, span_or_area, anchor_group = anchor_group, window = window)
        self._color = color.to_color_f()
        
    # overridden
    def _draw(self):
        fill_span(self.get_global_span(), self._color)

################################################################################

def create():
    global g
    
    g.shunter = Shunter()
    g.shunter.setup_window_client_area(Size(WIDTH, HEIGHT))
    
    g.window = Window("Some Name", Size(WIDTH, HEIGHT))
    widget1 = TextWidget(g.window.get_root_widget(), Area(200, 200, 190, 300), ColorF(1, 0, 0))
    TextWidget(widget1, Area(10, 10, 50, 140), ColorF(1, 1, 0))
    TextWidget(widget1, Area(70, 10, 50, 140), ColorF(1, 1, 0))
    widget2 = TextWidget(widget1, Area(130, 10, 50, 140), ColorF(1, 1, 0))
    TextWidget(widget2, Area(10, 20, 35, 50), ColorF(0, 1, 0))

    TextWidget(g.window.get_root_widget(), Area(10, 10, 50, 50), ColorF(0, 1, 1), make_anchor_group("LBLB"))
    TextWidget(g.window.get_root_widget(), Area(10, -60, 50, 50), ColorF(0, 1, 1), make_anchor_group("LTLT"))
    TextWidget(g.window.get_root_widget(), Area(-60, -60, 50, 50), ColorF(0, 1, 1), make_anchor_group("RTRT"))
    TextWidget(g.window.get_root_widget(), Area(-60, 10, 50, 50), ColorF(0, 1, 1), make_anchor_group("RBRB"))
    
    

def destroy():
    global g


def display():
    global g

    g.shunter.setup_draw(ColorF(0, 0, 0.5), is_culling_face = False)
    
    g.window.draw()


    glutSwapBuffers()

def do_on_idle():
    global g
    if g.is_redraw:
        display()
        g.is_redraw = False

def do_on_mouse(button, state, x, y):
    global g
    
    def get_mouse_wheel_direction(button, state):
        if button == 3 and state == GLUT_DOWN:
            return -1
        elif button == 4 and state == GLUT_DOWN:
            return 1
        return 0
    
    # ...
    
    g.is_redraw = True
    
################################################################################

if __name__ == "__main__":
    glutInit()
    glutInitDisplayMode(GLUT_RGBA)
    glutInitWindowSize(WIDTH, HEIGHT)

    x = int((glutGet(GLUT_SCREEN_WIDTH) - WIDTH) / 2)
    y = int((glutGet(GLUT_SCREEN_HEIGHT) - HEIGHT) / 2)

    glutInitWindowPosition(x, y)
    
    window = glutCreateWindow(b"OpenGL Window")
    glutDisplayFunc(display)
    glutIdleFunc(do_on_idle) 
    glutMouseFunc(do_on_mouse)
    
    glutSetOption(GLUT_ACTION_ON_WINDOW_CLOSE, GLUT_ACTION_CONTINUE_EXECUTION)

    create()
    glutMainLoop()
    destroy()