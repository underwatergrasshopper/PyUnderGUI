import TestKit

from UnderGUI.Utility import *
from UnderGUI.Inner.OpenGL_Texture import *

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

import PIL
from PIL import Image

################################################################################

WIDTH = 800
HEIGHT = 600

g_texture = None

################################################################################

def create():
    global g_texture
    
    ### Setting-Up OpenGL  ###

    glEnable(GL_CULL_FACE)
    
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
    
    glEnable(GL_TEXTURE_2D)
    
    glClearColor(0, 0, 0.5, 1)
    
    #### Tests ###
    
    g_texture = OpenGL_Texture()
    assert g_texture.get_width() == 0, g_texture.get_width()
    assert g_texture.get_height() == 0, g_texture.get_height()
    assert g_texture.is_created() == False
    assert g_texture.is_ok() == True
    assert g_texture.is_error() == False
    assert g_texture.get_err_msg() == "", g_texture.get_err_msg()
    
    g_texture.load("textures/wrong.bmp")
    assert g_texture.get_width() == 0, g_texture.get_width()
    assert g_texture.get_height() == 0, g_texture.get_height()
    assert g_texture.is_created() == False
    assert g_texture.is_ok() == False
    assert g_texture.is_error() == True
    assert g_texture.get_err_msg() == "Cannot identify format or open 'textures/wrong.bmp' file.", g_texture.get_err_msg()

    g_texture.clear_error()
    assert g_texture.get_err_msg() == "", g_texture.get_err_msg()

    g_texture.load("textures/not_exist.png")
    assert g_texture.get_width() == 0, g_texture.get_width()
    assert g_texture.get_height() == 0, g_texture.get_height()
    assert g_texture.is_created() == False
    assert g_texture.is_ok() == False
    assert g_texture.is_error() == True
    assert g_texture.get_err_msg() == "Cannot find 'textures/not_exist.png' file.", g_texture.get_err_msg()

    g_texture.load("textures/image.png")
    assert g_texture.is_created() == True
    assert g_texture.get_width() == 6, g_texture.get_width()
    assert g_texture.get_height() == 4, g_texture.get_height()
    assert g_texture.is_created() == True
    assert g_texture.is_ok() == True
    assert g_texture.is_error() == False
    assert g_texture.get_err_msg() == "", g_texture.get_err_msg()
  
    g_texture.destroy()
    assert g_texture.get_width() == 0, g_texture.get_width()
    assert g_texture.get_height() == 0, g_texture.get_height()
    assert g_texture.is_created() == False
    assert g_texture.is_ok() == True
    assert g_texture.is_error() == False
    assert g_texture.get_err_msg() == "", g_texture.get_err_msg()
 
    g_texture.load("textures/image_alpha.png")
    assert g_texture.is_created() == True
    assert g_texture.get_width() == 6, g_texture.get_width()
    assert g_texture.get_height() == 4, g_texture.get_height()
    assert g_texture.is_created() == True
    assert g_texture.is_ok() == True
    assert g_texture.is_error() == False
    assert g_texture.get_err_msg() == "", g_texture.get_err_msg()
    
def destroy():
    global g_texture
    
    # del g_texture # Cannot be done here. Glut destroys opengl rendering context before this.


def display():
    glClear(GL_COLOR_BUFFER_BIT)

    glBegin(GL_TRIANGLE_STRIP)
    
    glTexCoord2f(0, 0)
    glVertex2f(-0.5, -0.5)
    
    glTexCoord2f(1, 0)
    glVertex2f(0.5, -0.5)
    
    glTexCoord2f(0, 1)
    glVertex2f(-0.5, 0.5)
    
    glTexCoord2f(1, 1)
    glVertex2f(0.5, 0.5)
    
    glEnd()

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