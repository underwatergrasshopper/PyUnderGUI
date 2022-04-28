from .Font          import *
from .Commons       import *
from .Color         import *
from .Exceptions    import *

from copy           import copy
import re

__all__ = ['TextDrawer']

class TextDrawer:
    """
    :ivar UnderGUI.Font                            _default_font_ref:
    :ivar UnderGUI.Pos                             _origin:
    :ivar UnderGUI.Color                           _tint:
    :ivar int                                      _tab_size:
    """
    def __init__(self, default_font_ref = None):
        """
        :param UnderGUI.Font                       default_font_ref:
            Optional.
        """
        self._default_font_ref  = default_font_ref
        self._tint              = ColorF(1, 1, 1)
        self._tab_size          = 4
        
        self.set_position(Pos(0, 0))
    
    def set_position(self, pos):
        """
        :param UnderGUI.Pos                        pos:
        """
        self._origin    = pos
        self._pos       = pos
        
    def set_tint(self, tint):
        """
        :param UnderGUI.Color                      tint:
        """
        self._tint = tint
        
    def set_tab_size(self, size):
        """
        :param int                                 size:
            Number of spaces in tabulation.
        """
        self._tab_size = size
    
    def get_text_block_size(self, text, font = None, max_line_lenght = 0):
        """
        Formats text into multiple line text block when lines length is above max_line_lenght and returns size in pixels of text block.
        :param str                                 text:
        :param UnderGUI.Font                       font:
            Optional. If None then font provided at creation of TextDrawer is used.
        :param int                                 max_line_lenght:
            Optional. Maximal length in pixels of text line. Ignored when value is less than 1.
        :rtype Size:
        :return: Size of text block in pixels.
        :raises UnderGUI.Fail: No font provided, either by draw function or at creation of TextDrawer object.
        """
        if not font:
            font = self._default_font_ref
            
        if not font:
            raise Fail("UnderGUI: Font not provided.")
        
        lines = self._make_raw_lines(text, font, max_line_lenght)
        
        width = 0
        for line in lines:
            width = max(width, font.get_text_size(line).width)

        return Size(width, font.get_max_glyph_height() * len(lines))
        
           
    def draw(self, text, font = None, max_line_lenght = 0):
        """
        Drawstext into window client area. If max_line_lenght is greater than 0, 
        then wrap lines of text at max_line_lenght, by moving excess of text from one line to another.
        
        Moving excess of the text from one line to next line works at two levels.
        1. Moves excess of words from a line to the next line, where there is more than one word in the line.
        2. Moves excess of letters from a line to the next line, where there is only one word in the line.
        :param str                                 text:
        :param UnderGUI.Font                       font:
            Optional. If None then font provided at creation of TextDrawer is used.
        :param int                                 max_line_lenght:
            Optional. Maximal length in pixels of text line. 
        :raises UnderGUI.Fail: When no font provided, either by draw function or at creation of TextDrawer object.
        """
        if not font:
            font = self._default_font_ref
            
        if not font:
            raise Fail("UnderGUI: Font not provided.")
        
        lines = self._make_raw_lines(text, font, max_line_lenght)
        
        pos = self._pos
        for line in lines:
            self._pos = copy(pos)

            font.draw_text(self._pos.x, self._pos.y, line, self._tint)
            
            size = font.get_text_size(line) if len(line) else Size(0, font.get_max_glyph_height())
            self._pos.x += size.width
            pos = Pos(self._origin.x, self._pos.y - size.height)
            
    def _make_raw_lines(self, text, font, max_line_lenght):
        """
        :param str                                 text:
        :param UnderGUI.Font                       font:
        :param int                                 max_line_lenght:
        """
        text = text.replace("\t", " " * self._tab_size)
        lines = text.split("\n")
        return self._wrap_text_lines(lines, font, max_line_lenght)
        
    def _wrap_text_lines(self, lines, font, max_line_lenght):
        """
        :param str                                 text:
        :param UnderGUI.Font                       font:
        :param int                                 max_line_lenght:
        """
        lines = copy(lines)
        
        if max_line_lenght > 0:
            ix = 0
            while ix < len(lines):
                line = lines[ix]
                
                if len(line) > 1 and font.get_text_size(line).width > max_line_lenght:
                    lines[ix] = ""
                    lines.insert(ix, "")
                    
                    words = re.findall(r'[^ ]*[ ]*', line)
                    
                    line_length = 0 # in pixels
                    for word in words:
                        line_length += font.get_text_size(word).width
                        if line_length <= max_line_lenght:
                            lines[ix] += word
                        else:
                            if len(lines[ix]) == 0: 
                                # splits first word from current line (between current and next line) when it doesn't fit in current line
                                split_ix = max(1, font.get_split_ix(word, max_line_lenght))
                                lines[ix] += word[:split_ix]
                                lines[ix + 1] += word[split_ix:]
                            else:
                                lines[ix + 1] += word
                ix += 1
        return lines
            
