import TestKit

from UnderGUI import *
from UnderGUI._Private import *

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

################################################################################

WIDTH       = 800
HEIGHT      = 600

g_texture   = None
g_shunter   = None
g_drawer    = None

################################################################################

def create():
    global g_texture, g_shunter, g_drawer
    
    g_shunter   = Shunter()
    g_drawer    = Drawer()
    
    g_texture   = Texture()  
    assert g_texture.get_width() == 0, g_texture.get_width()
    assert g_texture.get_height() == 0, g_texture.get_height()
    assert g_texture.is_created() == False
    
    
    try:
        g_texture.load("textures/wrong.bmp")
    except Fail as exception:
        assert str(exception) == "Cannot identify format or open 'textures/wrong.bmp' file.", str(exception)
    else:
        assert False, "Expected exception."
    assert g_texture.get_width() == 0, g_texture.get_width()
    assert g_texture.get_height() == 0, g_texture.get_height()
    assert g_texture.is_created() == False



    try:
        g_texture.load("textures/not_exist.png")
    except Fail as exception:
        assert str(exception) == "Cannot find 'textures/not_exist.png' file.", str(exception)
    else:
        assert False, "Expected exception."
    assert g_texture.get_width() == 0, g_texture.get_width()
    assert g_texture.get_height() == 0, g_texture.get_height()
    assert g_texture.is_created() == False

    g_texture.load("textures/image.png")
    assert g_texture.is_created() == True, g_texture.get_err_msg() 
    assert g_texture.get_width() == 6, g_texture.get_width()
    assert g_texture.get_height() == 4, g_texture.get_height()
    assert g_texture.is_created() == True
  
    g_texture.destroy()
    assert g_texture.get_width() == 0, g_texture.get_width()
    assert g_texture.get_height() == 0, g_texture.get_height()
    assert g_texture.is_created() == False
 
    g_texture.load("textures/image_alpha.png")
    assert g_texture.is_created() == True
    assert g_texture.get_width() == 6, g_texture.get_width()
    assert g_texture.get_height() == 4, g_texture.get_height()
    assert g_texture.is_created() == True
    
def destroy():
    global g_texture, g_shunter, g_drawer
    
    # del g_texture # Cannot be done here. Glut destroys opengl rendering context before this.


def display():
    global g_texture, g_shunter, g_drawer
    
    g_drawer.fill_view(ColorF(0, 0, 0.5))
    g_shunter.setup_texture_draw()

    g_texture.draw(Range(-1, -1, 0, 0), Range(0, 0, 1, 1))
    g_texture.draw(Range(0, 0, 1, 1), Range(1.0 / 6, 0.25, 5.0 / 6, 0.75))
    
    g_texture.draw_from_pixel_range(Range(-1, 0, 0, 1), Range(0, 0, 6, 4), ColorF(0, 1, 1))
    g_texture.draw_from_pixel_range(Range(0, -1, 1, 0), Range(1, 1, 5, 3))
    
    # g_texture.draw_from_pixel_range(Range(-0.5, -0.5, 0.5, 0.5), Range(0, 0, 6, 4))
    # g_texture.draw_from_pixel_range(Range(-0.5, -0.5, 0.5, 0.5), Range(2, 2, 6, 4))
    # g_texture.draw_from_pixel_range(Range(-0.5, -0.5, 0.5, 0.5), Range(0, 0, 2, 4))

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