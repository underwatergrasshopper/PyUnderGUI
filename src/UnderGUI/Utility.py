import PIL.Image
import PIL

from .Exceptions import *
from .Commons import *

__all__ = [
    'convert_size_in_points_to_size_in_pixels',
    'get_proper_image_conversion_mode',
    'load_image_and_convert_to_rgba',
    'get_image_data_and_convert_to_rgba'
]


def convert_size_in_points_to_size_in_pixels(size):
    """
    6pt = 8px = 0.5em
    7pt = 9px = 0.55em
    7.5pt = 10px = 0.625em
    8pt = 11px = 0.7em
    9pt = 12px = 0.75em
    10pt = 13px = 0.8em
    10.5pt = 14px = 0.875em
    11pt = 15px = 0.95em
    12pt = 16px = 1em
    13pt = 17px = 1.05em
    13.5pt = 18px = 1.125em
    14pt = 19px = 1.2em
    14.5pt = 20px = 1.25em
    15pt = 21px = 1.3em
    16pt = 22px = 1.4em
    17pt = 23px = 1.45em 
    18pt = 24px = 1.5em 
    20pt = 26px = 1.6em 
    22pt = 29px = 1.8em 
    24pt = 32px = 2em
    26pt = 35px = 2.2em 
    27pt = 36px = 2.25em 
    28pt = 37px = 2.3em
    29pt = 38px = 2.35em
    30pt = 40px = 2.45em
    32pt = 42px = 2.55em
    34pt = 45px = 2.75em
    36pt = 48px = 3em
    
    :param int                                     size:
        Size in points.
    :rtype: int
    :return: Size in pixels.
    """
    return int(size * 4 / 3)

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
    :raises UnderGUI.Fail:
    """
    image_data = ImageData()

    try:
        image = PIL.Image.open(image_url)
    except FileNotFoundError as exception:
        raise Fail("UnderGUI: Cannot find '%s' file." % (image_url)) from exception 
    except PIL.UnidentifiedImageError as exception:
        raise Fail("UnderGUI: Cannot identify format or open '%s' file." % (image_url)) from exception
    except Exception as exception:
        raise Fail("UnderGUI: Cannot load '%s' file. %s" % (image_url, str(exception))) from exception 
    else:
        return get_image_data_and_convert_to_rgba(image)

    return image_data


def get_image_data_and_convert_to_rgba(image):
    """
    :param PIL.Image                               image:
    :rtype: UnderGUI.ImageData
    :raises UnderGUI.Fail:
    """
    try:
        # ("raw", raw_mode, stride, orientation)
        data = image.tobytes("raw", get_proper_image_conversion_mode(image), 0, -1)
        
    except Exception as exception:
        raise Fail("UnderGUI: Cannot convert image to raw pixels. %s" % (str(exception))) from exception 
    else:
        return ImageData(data, PixelFormat.RGBA, Size(image.width, image.height))
