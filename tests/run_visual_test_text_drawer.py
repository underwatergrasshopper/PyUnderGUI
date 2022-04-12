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
    shunter       = None
    font_fetcher  = None
    font          = None
    big_font      = None
    text_drawer   = None
g = Global()

################################################################################

def create():
    global g
    
    g.shunter   = Shunter()
    
    g.font_fetcher = FontFetcher()
    g.font_fetcher.add_font_source("Courier New", FontSource(normal_url = "cour.ttf", bold_url = "courbd.ttf", italic_url = "couri.ttf", bold_and_italic_url = "courbi.ttf"))
    g.font_fetcher.set_font_texture_minimal_size(Size(512, 512))
    g.font_fetcher.add_glyph_block_group(UnicodeBlockGroup.EUROPE)

    g.font      = Font(g.font_fetcher, FontInfo("Courier New", 16, size_unit = SizeUnit.PIXEL))
    g.big_font  = Font(g.font_fetcher, FontInfo("Courier New", 32, style = FontStyle.BOLD))
    
    g.text_drawer = TextDrawer(g.font)
    
    g.shunter.setup_window_client_area(Size(WIDTH, HEIGHT))
    
def destroy():
    global g


def display():
    global g

    g.shunter.setup_draw(ColorF(0, 0, 0.5))
    
    g.text_drawer.set_position(Pos(10, 300))
    g.text_drawer.set_tint(ColorF(0.7, 0.5, 0.5))
    g.text_drawer.draw("First line.\n\tSecond line.\nThird line.")
    g.text_drawer.draw("\nFourth line.", font = g.big_font)
    g.text_drawer.draw("\nSome ")
    g.text_drawer.draw("mixed", font = g.big_font)
    g.text_drawer.draw(" text.")
    
    g.text_drawer.set_position(Pos(300, 200))
    g.text_drawer.set_tint(ColorF(0.5, 0.7, 0.5))
    g.text_drawer.draw("First line.\n\tSecond line.\nThird line.")
    
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