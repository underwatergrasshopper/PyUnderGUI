from OpenGL.GL import *
from OpenGL.GLU import *

from UnderGUI.Utility import *
from UnderGUI.Inner.Texture import *
  
class OpenGL_Texture(Texture):
    def __init__(self):
        super().__init__()
        
        self._tex_obj_id = 0
        
    def __del__(self):
        if self._tex_obj_id:
            glDeleteTextures(self._tex_obj_id)
        
        super().__del__()

    def draw(self, view_range, texture_range):
        glBindTexture(GL_TEXTURE_2D, self._tex_obj_id)
        
        glBegin(GL_TRIANGLE_STRIP)
        
        glTexCoord2f(   texture_range.x1,   texture_range.y1)
        glVertex2f(     view_range.x1,      view_range.y1)
        
        glTexCoord2f(   texture_range.x2,   texture_range.y1)
        glVertex2f(     view_range.x2,      view_range.y1)
        
        glTexCoord2f(   texture_range.x1,   texture_range.y2)
        glVertex2f(     view_range.x1,      view_range.y2)
        
        glTexCoord2f(   texture_range.x2,   texture_range.y2)
        glVertex2f(     view_range.x2,      view_range.y2)
        
        glEnd()

    def _bare_create(self, data, pixel_format, width, height):
        if pixel_format == PixelFormat.RGBA:
            self._create_opengl_texture(data, GL_RGBA, width, height)
        else:
            self._register_err_msg("Unsupported '%s' pixel format." % (pixel_format.name))
           
    def _create_opengl_texture(self, data, opengl_texture_format, width, height):
        self._tex_obj_id = glGenTextures(1)
        
        if self._tex_obj_id == 0:
            self._register_err_msg("Can not create OpenGL texture object id.")
        else:
            glBindTexture(GL_TEXTURE_2D, self._tex_obj_id)
            
            glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
            glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
            
            glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
            glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)

            glTexImage2D(GL_TEXTURE_2D, 0, opengl_texture_format, width, height, 0, GL_RGBA, GL_UNSIGNED_BYTE, data)
   
