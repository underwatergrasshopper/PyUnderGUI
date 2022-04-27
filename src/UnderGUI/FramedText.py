from .Commons           import *
from .TextDrawer        import *
from .Font              import *
from .Color             import *
from ._Private.Draw     import *

from enum import Enum

__all__ = ['FramedText', 'ScrollUnit']

class ScrollUnit:
    PIXEL   = 0,
    PERCENT = 1,
    GLYPH   = 2

class FramedText:
    """
    :ivar UnderGUI.Area                            _area:
    :ivar str                                      _text:
    """
    def __init__(self, area, text, font, tint = ColorF(1, 1, 1, 1), background_color = ColorF(0, 0, 0, 0), is_restrict_draw_area = True):
        """
        :param UnderGUI.Area                       area:
        :param str                                 text:
        """
        self.set_area(area)
        self.set_text(text)
        self._font              = font
        self._tint              = tint
        self._background_color  = background_color
        self._text_drawer       = TextDrawer(font)
        
        self._text_pos          = Pos(0, 0)
        self._text_height       = 0
        self._scroll            = 0
        self._scroll_unit       = ScrollUnit.PIXEL
        self._offset_y          = 0
        self._is_restrict_draw_area = is_restrict_draw_area

    def set_area(self, area):
        """
        :param UnderGUI.Area                       area:
        """
        self._area = area
        
    def set_pos(self, pos):
        """
        :param UnderGUI.Pos                        pos:
        """
        self._area.set_pos(pos)
        
    def set_size(self, size):
        """
        :param UnderGUI.Pos                        pos:
        """
        self._area.set_size(size)
        
    def get_area(self):
        """
        :rtype UnderGUI.Area:
        """
        return self._area
        
    def set_text(self, text):
        """
        :param str                                 text:
        """
        self._text = text
        
    def append_text(self, text):
        """
        :param str                                 text:
        """
        self._text += text
        
    def get_text(self):
        """
        :rtype str:
        """
        return self._text
    
    def set_is_restrict_draw_area(self, is_restrict_draw_area):
        """
        :param bool                                text:
        """
        self._is_restrict_draw_area = is_restrict_draw_area
        
    def get_is_restrict_draw_area(self):
        """
        :rtype bool:
        """
        return self._is_restrict_draw_area
    
    def scroll_text(self, scroll):
        self._offset_y += scroll
    
    def update(self):
        self._text_height       = self._text_drawer.get_text_block_size(self._text, max_line_lenght = self._area.width).height
        glyph_height            = self._font.get_text_size("X").height

        # combine height of the text in pixels, which is outside of text frame
        outside_text_height     = self._text_height - self._area.height if self._text_height > self._area.height else 0
        
        self._offset_y          = max(min(self._offset_y, outside_text_height), 0)
            
        self._text_pos          = Pos(
            self._area.x, 
            self._area.y + self._area.height - glyph_height + self._offset_y
        )
        
    def draw(self, is_update = True):
        if is_update:
            self.update()
        
        fill_area(self._area, self._background_color)
        
        self._text_drawer.set_position(self._text_pos)
        self._text_drawer.set_tint(self._tint)
        
        if self._is_restrict_draw_area:
            restrict_draw_to_area(self._area)
            
        self._text_drawer.draw(self._text, max_line_lenght = self._area.width)
        
        if self._is_restrict_draw_area:
            restrict_draw_to_window_client_area()
        
    
        