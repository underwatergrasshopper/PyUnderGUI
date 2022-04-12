from .Font          import *
from .Commons       import *
from .Color         import *
from .Exceptions    import *
from copy           import copy

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
           
    def draw(self, text, font = None):
        """
        :param str                                 text:
        :param UnderGUI.Font                       font:
            Optional. If None then font provided at creation of TextDrawer is used.
        :raises UnderGUI.Fail: No font provided, either by draw function or at creation of TextDrawer object.
        """
        if not font:
            font = self._default_font_ref
            
        if not font:
            raise Fail("UnderGUI: Font not provided.")
        
        text = text.replace("\t", " " * self._tab_size)
        lines = text.split("\n")
        
        pos = self._pos
        for line in lines:
            self._pos = copy(pos)

            font.draw_text(self._pos.x, self._pos.y, line, self._tint)
            
            size = font.get_text_size(line) if len(line) else Size(0, font.get_text_size("X").height)
            self._pos.x += size.width
            pos = Pos(self._origin.x, self._pos.y - size.height)
