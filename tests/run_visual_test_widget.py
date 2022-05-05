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

################################################################################

def create():
    global g
    
    g.shunter = Shunter()
    g.shunter.setup_window_client_area(Size(WIDTH, HEIGHT))
    
    g.window = Window("Some Name", Size(WIDTH, HEIGHT))
    g.widget = Widget(None, Area(100, 100, 200, 300), window = g.window)
    

    
def destroy():
    global g


def display():
    global g

    g.shunter.setup_draw(ColorF(0, 0, 0.5))
    
    g.widget.draw()


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