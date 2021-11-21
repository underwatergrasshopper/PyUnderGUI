# Set of usefull classes and functions for UnderGUI.

import PIL
from PIL import Image

# Range form point (x1, y1) to point (x2, y2).
class Range:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

class ImageInfo:
    def __init__(self, data = None, width = 0, height = 0, err_msg = None):
        self.data       = data      if data else b''    # bytes
        self.width      = width
        self.height     = height
        self.err_msg    = err_msg   if err_msg else ""  # str
    

# Loads image and converts it to RGBA format.
# image_url         (is str).
# Returns ImageInfo object. 
# If ImageInfo.err_msg contains message (is not "") then loading image failed.
def load_image_and_convert_to_rgba(image_url):
    image_info = ImageInfo()

    try:
        image = Image.open(image_url)
        
    except FileNotFoundError:
        image_info.err_msg = "Cannot find '%s' file." % (image_url)
    except PIL.UnidentifiedImageError:
        image_info.err_msg = "Cannot identify format or open '%s' file." % (image_url)
    except Exception as exception:
        image_info.err_msg = str(exception)
    else:
        raw_mode = "RGBA"
        if image.mode in ["RGB", "BGR"]:
            raw_mode = "RGBX"
            
        try:
            # ("raw", raw_mode, stride, orientation)
            data = image.tobytes("raw", raw_mode, 0, -1)
            
        except Exception as exception:
            image_info.err_msg = str(exception)
        else:
            image_info = ImageInfo(data, image.width, image.height)

    return image_info