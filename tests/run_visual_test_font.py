import TestKit

from UnderGUI import *
from UnderGUI._Private import *

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

################################################################################

WIDTH           = 800
HEIGHT          = 600

g_shunter       = None
g_drawer        = None
g_font_fetcher  = None
g_font          = None
g_big_font      = None

################################################################################

def create():
    global g_font_fetcher, g_shunter, g_drawer, g_font, g_big_font
    
    g_shunter   = create_shunter()
    g_drawer    = create_drawer()
    
    g_font_fetcher = FontFetcher()
    g_font_fetcher.add_font_source("Courier New", FontSource(normal_url = "cour.ttf", bold_url = "courbd.ttf", italic_url = "couri.ttf", bold_and_italic_url = "courbi.ttf"))
    g_font_fetcher.set_font_texture_minimal_size(Size(512, 512))
    g_font_fetcher.add_glyph_block_group(UnicodeBlockGroup.EUROPE)

    g_font      = Font(g_font_fetcher, FontInfo("Courier New", 16, size_unit = SizeUnit.PIXEL))
    g_big_font  = Font(g_font_fetcher, FontInfo("Courier New", 32, style = FontStyle.BOLD))
    
    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();
    glOrtho(0, WIDTH, 0, HEIGHT, -1, 1);
    glMatrixMode(GL_MODELVIEW);
    
    
def destroy():
    global g_font_fetcher, g_shunter, g_drawer, g_font, g_big_font


def display():
    global g_font_fetcher, g_shunter, g_drawer, g_font, g_big_font
    
    g_drawer.fill_view(ColorF(0, 0, 0.5))
    g_shunter.setup_for_texture_draw()
    
    g_font.draw_text(0, 0, "Some interesting text. \u011B")
    g_big_font.draw_text(100, 100, "Much more bigger text. \u011B", ColorF(1, 0.2, 0.2, 1))

    glutSwapBuffers()

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
    # glutIdleFunc(display) # generates high cpu load
    glutSetOption(GLUT_ACTION_ON_WINDOW_CLOSE, GLUT_ACTION_CONTINUE_EXECUTION)
    
    create()
    glutMainLoop()
    destroy()