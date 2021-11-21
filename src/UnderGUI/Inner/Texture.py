from enum import Enum

from UnderGUI.Utility import *
        
class PixelFormat(Enum):
    Unknown = 0
    RGBA    = 1

class Texture:
    def __init__(self):
        self._width         = 0
        self._height        = 0

        self._err_msg       = ""
        self._is_created    = False

    def __del__(self):
        pass

        
    # Creates texture form loaded image.
    # image_url     (is str)
    # If fails then error message is stored. Call get_err_msg() to get stored error message. 
    def load(self, image_url):
        self.clear_error()
        
        image_info = load_image_and_convert_to_rgba(image_url)
        
        if image_info.err_msg:
            self._register_err_msg(image_info.err_msg)
        else:
            self.create(image_info.data, PixelFormat.RGBA, image_info.width, image_info.height) 
            
            if image_info.err_msg:
                self._register_err_msg("From '%s'." % (image_url))
            
            
    # data          (is bytes)
    # pixel_format  (is PixelFormat)
    # width         (is int)
    # height        (is int)
    # If fails then error message is registered. Call is_error() to check if error occurred. Call get_err_msg() to get registered error message. 
    def create(self, data, pixel_format, width, height):
        self.destroy()
        if pixel_format == PixelFormat.Unknown:
            self._register_err_msg("Unknown pixel format.")
        elif width == 0 or height == 0:
            self._register_err_msg("Width or height is 0.")
        else:
            self._bare_create(data, pixel_format, width, height)
            if self.is_ok():
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
    # This method must be overrode to do that. By default Range in OpenGL will be corresponding to (left, bottom, right, top).
    def draw(self, view_range, texture_range):
        pass
        
    # client_range          (is Range) Range in coordinates space of window client area.
    # texture_range         (is Range) Range in pixels, in coordinates space of texture, where boundaries are (0, 0, texture_width, texture_height).
    # By default Range in OpenGL will be corresponding to (left, bottom, right, top).
    def draw_from_pixel_range(self, view_range, texture_range):
        self.draw(view_range, texture_range / Range(self._width, self._height, self._width, self._height))

    
    def clear_error(self):
        self._err_msg = ""
        
    # Returns (str) error message.
    def get_err_msg(self):
        return self._err_msg
        
    # Returns True if any error message is registered.
    def is_error(self):
        return self._err_msg != ""

    # Returns True if no error message is registered.
    def is_ok(self):
        return self._err_msg == ""
        
       
       
    def _register_err_msg(self, err_msg):
        if self._err_msg != "":
            self._err_msg += " "
            
        self._err_msg += err_msg 
    
    # Creates texture in specific API. This method must be overrode to do that.
    def _bare_create(self, data, pixel_format, width, height):
        self._register_err_msg("Method Texture._bare_create is not overrode.")
    