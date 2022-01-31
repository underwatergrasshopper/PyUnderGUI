import PIL.Image
import PIL

from .Exceptions import *
from .Commons import *

__all__ = [
    'get_proper_image_conversion_mode',
    'load_image_and_convert_to_rgba'
]

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