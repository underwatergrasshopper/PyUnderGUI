from enum import Enum

from UnderGUI.Utility import *
from UnderGUI.Exception import *

__all__ = ['PixelFormat', 'Texture']

class PixelFormat(Enum):
    UNKNOWN = 0
    RGBA    = 1

class Texture:
    def __init__(self):
        self._width         = 0
        self._height        = 0

        self._is_created    = False

    def __del__(self):
        pass

        
    # Creates texture form loaded image.
    # image_url     (is str)
    # Raises: UnderGUI.Exceptions.Fail. 
    def load(self, image_url):
        try:
            image_data = load_image_and_convert_to_rgba(image_url)
        except Fail as exception:
            raise exception
        else:
            self.create(image_data.data, PixelFormat.RGBA, image_data.width, image_data.height) 
            
            
    # data          (is bytes)
    # pixel_format  (is PixelFormat)
    # width         (is int)
    # height        (is int)
    # Raises: UnderGUI.Exceptions.Fail. 
    def create(self, data, pixel_format, width, height):
        self.destroy()
        if pixel_format == PixelFormat.UNKNOWN:
            raise Fail("Unknown pixel format.")
        elif width == 0:
            raise Fail("Width is 0.")
        elif height == 0:
            raise Fail("Height is 0.")
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
        return self._is_created
        
        
    def get_width(self):
        return self._width
        
    def get_height(self):
        return self._height
        
        
    # client_range          (is Range) Range in coordinates space of window client area.
    # texture_range         (is Range) Range in coordinates space of texture, where boundaries are (0, 0, 1, 1).
    # tint                  (is Color) Tint color for texture. 
    # This method must be overrode to do that. By default Range in OpenGL will be corresponding to (left, bottom, right, top).
    def draw(self, view_range, texture_range, tint = Color(1, 1, 1)):
        pass
        
    # client_range          (is Range) Range in coordinates space of window client area.
    # texture_range         (is Range) Range in pixels, in coordinates space of texture, where boundaries are (0, 0, texture_width, texture_height).
    # tint                  (is Color) Tint color for texture. 
    # By default Range in OpenGL will be corresponding to (left, bottom, right, top).
    def draw_from_pixel_range(self, view_range, texture_range, tint = Color(1, 1, 1)):
        self.draw(view_range, texture_range / Range(self._width, self._height, self._width, self._height), tint)
    
    # Creates texture in specific API. This method must be overrode to do that.
    # Raises                UnderGUI.Exceptions.Fail
    def _bare_create(self, data, pixel_format, width, height):
        raise Fail("Method Texture._bare_create is not overrode.")
    