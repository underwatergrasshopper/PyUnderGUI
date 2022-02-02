import PIL.Image
import PIL

from .Exceptions import *
from .Commons import *

__all__ = [
    'get_proper_image_conversion_mode',
    'load_image_and_convert_to_rgba'
]

def get_proper_image_conversion_mode(image):
    """
    :param PIL.Image                               image:
    :rtype: str
    :return: One of formats to which image can be converted, by PIL.Image.tobytes with raw converter. Either "RGBA" or "RGBX".
    """
    if image.mode in ["RGB", "BGR"]:
        return "RGBX"
    return "RGBA"

def load_image_and_convert_to_rgba(image_url):
    """
    :param str                                     image_url:
    :rtype: Under.GUI.ImageData
    """
    image_data = ImageData()

    try:
        image = PIL.Image.open(image_url)
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