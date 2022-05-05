from .Commons       import *
from .FontFetcher   import *
from .Color         import *

from ._Private      import *

__all__ = [
    'Font'
]

class Font:
    """
    :ivar UnderGUI.FontFetcher                     _font_fetcher_ref:
    :ivar UnderGUI.FontInfo                        _font_info:
    """
    def __init__(self, font_fetcher_ref, font_info):
        """
        :param UnderGUI.FontFetcher                font_fetcher_ref:
        :param UnderGUI.FontInfo                   font_info:
        """
        self._font_fetcher_ref  = font_fetcher_ref
        self._texture           = Texture()
        self._font_data         = FontData()
 
        self.create(font_info)
        
    def create(self, font_info):
        """
        :param UnderGUI.FontInfo                   font_info:
        :raises UnderGUI.Fail:
        """
        self._font_info = font_info
        
        self._font_fetcher_ref.fetch(font_info)
        self._font_data = self._font_fetcher_ref.get_font_data()
        
        self._texture.create_from_td(self._font_data.texture_data)
        
    def draw_text(self, x, y, text, tint = ColorF(1, 1, 1, 1)):
        """
        Draws the text at position (x, y). Where (x, y) is location of left-bottom corner of first drawed glyph of the text.
        :param int                                 x:
        :param int                                 y:
        :param str                                 text:
        :param UnderGUI.Color                      tint:
            Color of drawed text.
        """
        n = x
        for glyph in text:
            code = ord(glyph)
            
            info = self._font_data.texture_glyph_infos[code]
            self._texture.draw(Area(n, y, info.area.width, info.area.height).to_range(), info.glyph_range, tint)

            n += info.area.width
    
    def get_text_size(self, text):
        """
        :param str                                 text:
        :rtype Size:
        :return: Size of text in pixels.
        """
        height  = 0
        width   = 0
        
        if text != "":
            for glyph in text:
                code = ord(glyph)
                
                size = self._font_data.texture_glyph_infos[code].area.get_size()
                
                height = max(height, size.height)
                width += size.width
            
        return Size(width, height)
    
    def get_max_glyph_height(self):
        return self._font_data.max_glyph_height
            
    def get_split_ix(self, text, length):
        """
        :param str                                 text:
        :param int                                 length:
            In pixels.
        :rtype int:
        :return: Index of place in given text where it's width in pixels is bigger than given lengt.
        """
        width = 0
        if text != "":
            for ix in range(0, len(text)):
                glyph = text[ix]          
                code = ord(glyph)
                
                width += self._font_data.texture_glyph_infos[code].area.get_size().width
                if width > length:
                    return ix
            return len(text) - 1
        return 0
    
    
        
        
        
        