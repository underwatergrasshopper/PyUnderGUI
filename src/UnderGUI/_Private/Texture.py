from OpenGL.GL              import *
from OpenGL.GLU             import *

from UnderGUI.Color         import *
from UnderGUI.Commons       import *
from UnderGUI.Exceptions    import *
from UnderGUI.Utility       import *

__all__ = ['Texture']

class Texture:
    """            
    :ivar int                                      _width:
    :ivar int                                      _height:
    :ivar int                                      _tex_obj_id:
    :ivar bool                                     _is_created:
    """
    def __init__(self):
        self._width         = 0
        self._height        = 0
        self._tex_obj_id = 0

        self._is_created    = False

    def __del__(self):
        if self._tex_obj_id:
            glDeleteTextures(self._tex_obj_id)
        

    def load(self, image_url):
        """
        Creates texture from loaded image.
        
        :param str                                 image_url:
        :raises UnderGUI.Fail:
        """
        try:
            texture_data = load_image_and_convert_to_rgba(image_url)
        except Fail as exception:
            raise exception
        else:
            self.create(texture_data.data, texture_data.pixel_format, texture_data.size.width, texture_data.size.height) 

    def create_from_td(self, texture_data):
        """
        Creates texture from texture data.
        
        :param UnderGUI.TextureData                texture_data:                       
        :raises UnderGUI.Fail:
        """
        self.create(texture_data.data, texture_data.pixel_format, texture_data.size.width, texture_data.size.height)
        
    def create(self, data, pixel_format, width, height):
        """
        Creates texture from texture data.
        
        :param bytes                               data:                       
            Pixels of an image. Four bytes per pixel if pixel_format is PixelFormat.RGBA. 
            Order of color channels is RGBA.
        :param UnderGUI.PixelFormat                pixel_format:
        :param int                                 width:
        :param int                                 height:
        :raises UnderGUI.Fail:
        """
        self.destroy()
        if pixel_format == PixelFormat.UNKNOWN:
            raise Fail("UnderGUI: Unknown pixel format.")
        elif width == 0:
            raise Fail("UnderGUI: Width is 0.")
        elif height == 0:
            raise Fail("UnderGUI: Height is 0.")
        else:
            try:
                self._bare_create(data, pixel_format, width, height)
            except Fail as exception:
                raise exception
            else:
                self._width      = width
                self._height     = height
                self._is_created = True

    def destroy(self):
        if self._is_created:
            self.__del__()
        self.__init__()
        
    def is_created(self):
        """:rtype: bool"""
        return self._is_created
        
    def get_width(self):
        """:rtype: int"""
        return self._width
        
    def get_height(self):
        """:rtype: int"""
        return self._height
        
    def draw(self, view_span, texture_span, tint = ColorF(1, 1, 1)):
        """
        Draws fragment of texture into region in window client area.
        By default, span is corresponding to (left, bottom, right, top).
        
        :param UnderGUI.Span                      view_span:                 
            Coordinates of region in window client area. 
        :param UnderGUI.Span                      texture_span:  
            Coordinates of region in texture. Coordinates are normalized to span from 0.0 to 1.0.
            Max span is Span(0, 0, 1, 1).
        :param                                     tint:                                                           
            Modulates color of drawn texture fragment.
        :type                                      tint: 
            UnderGUI.ColorF or UnderGUI.ColorB or UnderGUI.ColorI
        :raises UnderGUI.Fail:
        """
        glBindTexture(GL_TEXTURE_2D, self._tex_obj_id)

        tint = tint.to_color_f()
        glColor4f(tint.r, tint.g, tint.b, tint.a)
        
        glBegin(GL_TRIANGLE_STRIP)
        
        glTexCoord2f(   texture_span.x1,   texture_span.y1)
        glVertex2f(     view_span.x1,      view_span.y1)
        
        glTexCoord2f(   texture_span.x2,   texture_span.y1)
        glVertex2f(     view_span.x2,      view_span.y1)
        
        glTexCoord2f(   texture_span.x1,   texture_span.y2)
        glVertex2f(     view_span.x1,      view_span.y2)
        
        glTexCoord2f(   texture_span.x2,   texture_span.y2)
        glVertex2f(     view_span.x2,      view_span.y2)
        
        glEnd()
        
        glBindTexture(GL_TEXTURE_2D, 0)
        
    def draw_from_pixel_span(self, view_span, texture_span, tint = ColorF(1, 1, 1)):
        """
        Draws fragment of texture into region in window client area.
        By default, Span is corresponding to (left, bottom, right, top).
        
        :param UnderGUI.Span                      view_span:               
            Coordinates of region in window client area. 
        :param UnderGUI.Span                      texture_span:             
            Coordinates of region in texture. Coordinates are in pixels.
            Max span is Span(0, 0, texture_width, texture_heigh).
        :param                                     tint:                                                           
            Modulates color of drawn texture fragment.
        :type                                      tint: 
            UnderGUI.ColorF or UnderGUI.ColorB or UnderGUI.ColorI
        :raises UnderGUI.Fail:
        """
        self.draw(view_span, texture_span / Size(self._width, self._height), tint)
    
    def _bare_create(self, data, pixel_format, width, height):
        """
        Only creates texture from image data, using specific api under hood. 
        
        :param bytes                               data:           
            Pixels of texture. Four bytes per pixel if pixel_format is PixelFormat.RGBA. 
            Order of color channels: RGBA.
        :param UnderGUI.PixelFormat                pixel_format:
        :param int                                 width:
        :param int                                 height:
        :raises UnderGUI.Fail:
        """
        if pixel_format == PixelFormat.RGBA:
            self._create_opengl_texture(data, GL_RGBA, width, height)
        else:
            raise Fail("UnderGUI: Unsupported pixel format: '%s'." % (pixel_format.name))
        
    def _create_opengl_texture(self, data, internal_format, width, height):
        """
        :param bytes                               data:
        :param int                                 internal_format: 
            Expected values: GL_RGBA.
        :param int                                 width:
        :param int                                 height:
        :raises UnderGUI.Fail:
        """
        self._tex_obj_id = glGenTextures(1)
        
        if self._tex_obj_id == 0:
            raise Fail("UnderGUI: Can not create OpenGL texture object id.")
        else:
            glBindTexture(GL_TEXTURE_2D, self._tex_obj_id)
            
            glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
            glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
            
            glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
            glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)

            glTexImage2D(GL_TEXTURE_2D, 0, internal_format, width, height, 0, GL_RGBA, GL_UNSIGNED_BYTE, data)
            
            glBindTexture(GL_TEXTURE_2D, 0)