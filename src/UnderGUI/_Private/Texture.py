from UnderGUI.Color         import *
from UnderGUI.Commons       import *
from UnderGUI.Exceptions    import *
from UnderGUI.Utility       import *

__all__ = ['Texture']

class Texture:
    def __init__(self):
        self._width         = 0
        self._height        = 0

        self._is_created    = False

    def __del__(self):
        """
        :abstractmethod:
        """
        pass

    def load(self, image_url):
        """
        Creates texture from image file.
        
        :param str      image_url:
        :raises: UnderGUI.Fail
        """
        try:
            image_data = load_image_and_convert_to_rgba(image_url)
        except Fail as exception:
            raise exception
        else:
            self.create(image_data.data, PixelFormat.RGBA, image_data.width, image_data.height) 

    def create(self, data, pixel_format, width, height):
        """Creates texture from image data.
        
        :param bytes                    data:           Contains pixels of image. Four bytes per pixel if pixel_format is PixelFormat.RGBA. Order of color channels: RGBA.
        :param UnderGUI.PixelFormat     pixel_format:
        :param int                      width:
        :param int                      height:
        :raises: UnderGUI.Fail
        """
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
        
    def draw(self, view_range, texture_range, tint = ColorF(1, 1, 1)):
        """
        Draws fragment of texture into region in window client area.
        By default Range is corresponding to (left, bottom, right, top).
        Must be overrode.
        
        :abstractmethod:
        :param UnderGUI.Range       view_range:         Region in window client area. In normalized coordinates from range 0.0 to 1.0 for each. Max span is Range(0, 0, 1, 1).
        :param UnderGUI.Range       texture_range:      Fragment of texture. In normalized coordinates from range 0.0 to 1.0 for each. Max span is Range(0, 0, 1, 1).
        :param tint:                                    Modulates color of drawn texture fragment.
        :type tint: ColorF or ColorB or ColorI
        :raises: UnderGUI.Fail
        """
        pass
        
    def draw_from_pixel_range(self, view_range, texture_range, tint = ColorF(1, 1, 1)):
        """
        Draws fragment of texture into region in window client area.
        By default Range is corresponding to (left, bottom, right, top).
        
        :param UnderGUI.Range       view_range:         Region in window client area. In pixels. Max span is Range(0, 0, window_client_width, window_client_heigh).
        :param UnderGUI.Range       texture_range:      Fragment of texture. In pixels. Max span is Range(0, 0, texture_width, texture_heigh).
        :param tint:                                    Modulates color of drawn texture fragment.
        :type tint: ColorF or ColorB or ColorI
        :raises: UnderGUI.Fail
        """
        self.draw(view_range, texture_range / Range(self._width, self._height, self._width, self._height), tint)
    
    def _bare_create(self, data, pixel_format, width, height):
        """
        Only creates texture from image data, using specific api under hood. 
        Must be overrode.
        
        :abstractmethod:
        :param bytes                    data:           Contains pixels of image. Four bytes per pixel if pixel_format is PixelFormat.RGBA. Order of color channels: RGBA.
        :param UnderGUI.PixelFormat     pixel_format:
        :param int                      width:
        :param int                      height:
        :raises: UnderGUI.Fail
        """
        raise Fail("Method Texture._bare_create is not overrode.")