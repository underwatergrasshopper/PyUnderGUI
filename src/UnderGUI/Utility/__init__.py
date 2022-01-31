# Set of usefull classes and functions for UnderGUI.

import PIL
from PIL import Image

from UnderGUI.Exception import *


# Range form point (x1, y1) to point (x2, y2).
class Range:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        
    def __eq__(self, other):
        return self.x1 == other.x1 and self.y1 == other.y1 and self.x2 == other.x2 and self.y2 == other.y2
        
    def __ne__(self, other):
        return self.x1 != other.x1 or self.y1 != other.y1 or self.x2 != other.x2 or self.y2 != other.y2
        
    def __mul__(self, other):
        if isinstance(other, Range):
            return Range(self.x1 * other.x1, self.y1 * other.y1, self.x2 * other.x2, self.y2 * other.y2)
        return Range(self.x1 * other, self.y1 * other, self.x2 * other, self.y2 * other)
        
    def __truediv__(self, other):
        if isinstance(other, Range):
            return Range(self.x1 / other.x1, self.y1 / other.y1, self.x2 / other.x2, self.y2 / other.y2)
        return Range(self.x1 / other, self.y1 / other, self.x2 / other, self.y2 / other)
        
    def __floordiv__(self, other):
        if isinstance(other, Range):
            return Range(self.x1 / other.x1, self.y1 / other.y1, self.x2 / other.x2, self.y2 / other.y2)
        return Range(self.x1 / other, self.y1 / other, self.x2 / other, self.y2 / other)
        
    def __add__(self, other):
        if isinstance(other, Range):
            return Range(self.x1 + other.x1, self.y1 + other.y1, self.x2 + other.x2, self.y2 + other.y2)
        return Range(self.x1 + other, self.y1 + other, self.x2 + other, self.y2 + other)
        
    def __sub__(self, other):
        if isinstance(other, Range):
            return Range(self.x1 - other.x1, self.y1 - other.y1, self.x2 - other.x2, self.y2 - other.y2)
        return Range(self.x1 - other, self.y1 - other, self.x2 - other, self.y2 - other)

class ImageData:
    def __init__(self, data = None, width = 0, height = 0):
        self.data       = data      if data else b''    # bytes
        self.width      = width
        self.height     = height
    
class Color:
    def __init__(self, r, g, b, a = 1):
        self.r = r
        self.g = g
        self.b = b
        self.a = a

# Chooses RGBA or RGBX pixel format (if conversion to RGBA is not acceptable for PIL.Image.tobytes raw converter).
# image     (is PIL.Image)
# Returns   (str) 
def get_proper_image_conversion_mode(image):
    if image.mode in ["RGB", "BGR"]:
        return "RGBX"
    return "RGBA"

# Loads image and converts it to RGBA format.
# image_url         (is str)
# Returns           (ImageData)
# Raises            UnderGUI.Exceptions.Fail
def load_image_and_convert_to_rgba(image_url):
    image_data = ImageData()

    try:
        image = Image.open(image_url)
    except FileNotFoundError as exception:
        raise Fail("Cannot find '%s' file." % (image_url)) from exception 
    except PIL.UnidentifiedImageError as exception:
        raise Fail("Cannot identify format or open '%s' file." % (image_url)) from exception
    except Exception as exception:
        raise Fail("Cannot load '%s' file. %s" % (image_url, str(exception))) from exception 
    else:
        try:
            # ("raw", raw_mode, stride, orientation)
            data = image.tobytes("raw", get_proper_image_conversion_mode(image), 0, -1)
            
        except Exception as exception:
            raise Fail("Cannot convert '%s' file to raw pixels. %s" % (image_url, str(exception))) from exception 
        else:
            image_data = ImageData(data, image.width, image.height)

    return image_data