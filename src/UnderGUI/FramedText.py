from .Commons           import *
from .TextDrawer        import *
from .Font              import *
from .Color             import *
from ._Private.Draw     import *

from enum import Enum

__all__ = [
    'FramedText', 
    'ScrollUnit',
    'ScrollPlace',
]

class ScrollUnit(Enum):
    PIXEL           = 0,
    LINE            = 1,
    OUTSIDE_TEXT    = 2
    
class ScrollPlace(Enum):
    BEGIN           = 0,
    END             = 1

class FramedText:
    """
    :ivar UnderGUI.Area                            _area:
        In pixels.
    :ivar str                                      _text:
    :ivar UnderGUI.Font                            _font:
    :ivar UnderGUI.Color                           _tint:
        Tint of the text.
    :ivar UnderGUI.Color                           _background_color:
    :ivar UnderGUI.TextDrawer                      _text_drawer:
    :ivar UnderGUI.Pos                             _text_pos:
    :ivar int                                      _text_height:
    :ivar int                                      _glyph_height:
    :ivar int                                      _outside_text_height:
    :ivar int                                      _offset_y:
    :ivar bool                                     _is_restrict_draw_to_area:
    :ivar bool                                     _is_updatea_sheduled:
    """
    def __init__(self, area, text, font, tint = ColorF(1, 1, 1, 1), background_color = ColorF(0, 0, 0, 0), is_restrict_draw_to_area = True):
        """
        :param UnderGUI.Area                       area:
            In pixels.
        :param str                                 text:
        :param UnderGUI.Font                       font:
        :param UnderGUI.Color                      tint:
            Tint of the text.
        :param UnderGUI.Color                      background_color:
        :param bool                                is_restrict_draw_to_area:
        """
        self.set_area(area)
        self.set_text(text)
        self._font                      = font
        self._tint                      = tint
        self._background_color          = background_color
        self._text_drawer               = TextDrawer(font)
        
        self._text_pos                  = Pos(0, 0)
        self._text_height               = 0
        
        self._glyph_height              = 0
        self._outside_text_height       = 0
        self._offset_y                  = 0
        
        self._is_restrict_draw_to_area  = is_restrict_draw_to_area
        
        self._shedule_update()

    def set_area(self, area):
        """
        :param UnderGUI.Area                       area:
        """
        self._area = area
        self._shedule_update()
        
    def set_pos(self, pos):
        """
        :param UnderGUI.Pos                        pos:
        """
        self._area.set_pos(pos)
        self._shedule_update()
        
    def set_size(self, size):
        """
        :param UnderGUI.Pos                        pos:
        """
        self._area.set_size(size)
        self._shedule_update()
        
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
        self._shedule_update()
        
    def append_text(self, text):
        """
        :param str                                 text:
        """
        self._text += text
        self._shedule_update()
        
    def get_text(self):
        """
        :rtype str:
        """
        return self._text
    
    def set_is_restrict_draw_to_area(self, is_restrict_draw_to_area):
        """
        :param bool                                text:
        """
        self._is_restrict_draw_to_area = is_restrict_draw_to_area
        
    def get_is_restrict_draw_to_area(self):
        """
        :rtype bool:
        """
        return self._is_restrict_draw_to_area
    
    def scroll_text_by(self, offset_y, unit = ScrollUnit.PIXEL):
        """
        Scrolls text up or down by offset_y.
        :param int or float                        offset:
            Negative value refers to movement of text up.
            Positive value refers to movement of text down.
            
            When unit is ScrollUnit.PIXEL:
                Offset counted in pixels.
            When unit is ScrollUnit.LINE:
                Offset counted in lines.
            When unit is ScrollUnit.OUTSIDE_TEXT:
                Offset counted in 'text which is outside of frame';
                Accepted range of values is from -1.0 to 1.0;
                For example: value -0.25 moves text up by 25% of height in pixels of text which is outside of frame.
        :param UnderGUI.ScrollUnit                 unit:
        """
        self._update_if_sheduled()
        
        if unit == ScrollUnit.PIXEL:
            self._offset_y += offset_y
        elif unit == ScrollUnit.OUTSIDE_TEXT:
            ratio = min(max(offset_y, -1.0), 1.0)
            self._offset_y += self._outside_text_height * ratio
        elif unit == ScrollUnit.LINE:
            self._offset_y += self._glyph_height * offset_y
            
        self._shedule_update()
            
    def scroll_text_to(self, place):
        """
        Scrolls text to the beginning of text or to the end of text.
        :param UnderGUI.ScrollPlace                place:
        """
        self._update_if_sheduled()
        if place == ScrollPlace.BEGIN:
            self._offset_y = 0
        elif place == ScrollPlace.END:
            self._offset_y = self._outside_text_height
            
        self._shedule_update()

    def force_update(self):
        self._update()
        self._is_updatea_sheduled = False
        
    def draw(self):
        self._update_if_sheduled()
        
        fill_area(self._area, self._background_color)
        
        self._text_drawer.set_position(self._text_pos)
        self._text_drawer.set_tint(self._tint)
        
        if self._is_restrict_draw_to_area:
            restrict_draw_to_area(self._area)
            
        self._text_drawer.draw(self._text, max_line_lenght = self._area.width)
        
        if self._is_restrict_draw_to_area:
            restrict_draw_to_window_client_area()
         
    def _update(self):
        self._text_height           = self._text_drawer.get_text_block_size(self._text, max_line_lenght = self._area.width).height
        self._glyph_height          = self._font.get_max_glyph_height()

        # height of the text (in pixels), which is outside of text frame
        self._outside_text_height   = self._text_height - self._area.height if self._text_height > self._area.height else 0
        self._offset_y              = min(max(self._offset_y, 0), self._outside_text_height)
        
        self._text_pos              = Pos(
            self._area.x, 
            self._area.y + self._area.height - self._glyph_height + self._offset_y
        )
            
    def _update_if_sheduled(self):
        if self._is_updatea_sheduled:
            self._update()
            self._is_updatea_sheduled = False
            
    def _shedule_update(self):
        self._is_updatea_sheduled = True 
        
        


