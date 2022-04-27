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
    is_redraw     = False
    shunter       = None
    font_fetcher  = None
    font          = None
    font2         = None
    big_font      = None
    text_drawer   = None
    framed_text   = None
    scroll_test_framed_text   = None
g = Global()

################################################################################

def create():
    global g
    
    g.shunter = Shunter()
    
    g.font_fetcher = FontFetcher()
    g.font_fetcher.add_font_source("Courier New", FontSource(normal_url = "cour.ttf", bold_url = "courbd.ttf", italic_url = "couri.ttf", bold_and_italic_url = "courbi.ttf"))
    g.font_fetcher.add_font_source("Arial", FontSource(normal_url = "arial.ttf", bold_url = "arialbd.ttf", italic_url = "ariali.ttf", bold_and_italic_url = "arialbi.ttf"))
    g.font_fetcher.set_font_texture_minimal_size(Size(512, 512))
    g.font_fetcher.add_glyph_block_group(UnicodeBlockGroup.EUROPE)

    g.font      = Font(g.font_fetcher, FontInfo("Courier New", 16, size_unit = SizeUnit.PIXEL))
    g.font2     = Font(g.font_fetcher, FontInfo("Arial", 16, size_unit = SizeUnit.PIXEL))
    g.big_font  = Font(g.font_fetcher, FontInfo("Courier New", 32, style = FontStyle.BOLD))
    
    g.text_drawer = TextDrawer(g.font)
    
    g.shunter.setup_window_client_area(Size(WIDTH, HEIGHT))
    
    g.framed_text = FramedText(
        area = Area(0, 0, 0, 0), 
        text = "This is some real text for wrapping and other stuff.\nAnd another line with very-much-long-word.\n\t*Option 1.\n\t*Option 2.",
        font = g.font,
        tint = ColorF(1, 1, 1),
        background_color = ColorF(0, 0, 0, 0.2)
    )
    
    g.scroll_test_framed_text = FramedText(
        area = Area(0, 0, 0, 0), 
        text = "This is some real text for wrapping and other stuff.\nAnd another line with very-much-long-word.\n\t*Option 1.\n\t*Option 2.",
        font = g.font,
        tint = ColorF(1, 1, 1),
        background_color = ColorF(0, 0, 0, 0.2),
        is_restrict_draw_area = False
    )
    
    
def destroy():
    global g


def display():
    global g

    g.shunter.setup_draw(ColorF(0, 0, 0.5))

    g.framed_text.set_area(Area(10, 200, 150, 300))
    g.framed_text.draw()
    
    g.framed_text.set_pos(Pos(210, 200))
    g.framed_text.set_size(Size(200, 300))
    g.framed_text.draw()

    g.scroll_test_framed_text.set_area(Area(510, 200, 100, 150))
    g.scroll_test_framed_text.draw()

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
    
    # print(button, state, x, y) # debug
    wheel_direction = get_mouse_wheel_direction(button, state)
    # print(wheel_direction) # debug
    g.scroll_test_framed_text.scroll_text(20 * wheel_direction)
    
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