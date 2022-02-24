from enum import Enum

__all__ = [ 
    'PixelFormat',
    'Pos',
    'Size',
    'RangePP',
    'Range',
    'RangeF',
    'AreaPS',
    'Area',
    'ImageData',
    'SizeUnit',
    'FontStyle',
    'FontInfo',
    'FontData',
    'FontSource',
    'FontSourceRegister'
]

class PixelFormat(Enum):
    UNKNOWN = 0
    RGBA    = 1
    

class Pos:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def to_size(self):
        """
        Converts to UnderGUI.Size.
        
        :rtype: UnderGUI.Size
        """
        return Size(self.x, self.y)
        
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
        
    def __ne__(self, other):
        return self.x != other.x or self.y != other.y
    
    def __lt__(self, other):
        return self.x < other.x and self.y < other.y
        
    def __le__(self, other):
        return self.x <= other.x and self.y <= other.y
    
    def __gt__(self, other):
        return self.x > other.x and self.y > other.y
        
    def __ge__(self, other):
        return self.x >= other.x and self.y >= other.y
    
    def __mul__(self, other):
        if isinstance(other, Pos):
            return Pos(self.x * other.x, self.y * other.y)
        if isinstance(other, Size):
            return Pos(self.x * other.width, self.y * other.height)
        return Pos(self.x * other, self.y * other)
        
    def __truediv__(self, other):
        if isinstance(other, Pos):
            return Pos(self.x / other.x, self.y / other.y)
        if isinstance(other, Size):
            return Pos(self.x / other.width, self.y / other.height)
        return Pos(self.x / other, self.y / other)
        
    def __floordiv__(self, other):
        if isinstance(other, Pos):
            return Pos(self.x / other.x, self.y / other.y)
        if isinstance(other, Size):
            return Pos(self.x / other.width, self.y / other.height)
        return Pos(self.x / other, self.y / other)
        
    def __add__(self, other):
        if isinstance(other, Pos):
            return Pos(self.x + other.x, self.y + other.y)
        if isinstance(other, Size):
            return Pos(self.x + other.width, self.y + other.height)
        return Pos(self.x + other, self.y + other)
        
    def __sub__(self, other):
        if isinstance(other, Pos):
            return Pos(self.x - other.x, self.y - other.y)
        if isinstance(other, Size):
            return Pos(self.x - other.width, self.y - other.height)
        return Pos(self.x - other, self.y - other)

class Size:
    def __init__(self, width, height):
        self.width  = width
        self.height = height  
        
    def to_pos(self):
        """
        Converts to UnderGUI.Pos.
        
        :rtype: UnderGUI.Pos
        """
        return Pos(self.width, self.height)
        
    def __eq__(self, other):
        return self.width == other.width and self.height == other.height
        
    def __ne__(self, other):
        return self.width != other.width or self.height != other.height
    
    def __lt__(self, other):
        return self.width < other.width and self.height < other.height
        
    def __le__(self, other):
        return self.width <= other.width and self.height <= other.height
    
    def __gt__(self, other):
        return self.width > other.width and self.height > other.height
        
    def __ge__(self, other):
        return self.width >= other.width and self.height >= other.height
    
    def __mul__(self, other):
        if isinstance(other, Size):
            return Size(self.width * other.width, self.height * other.height)
        return Size(self.width * other, self.height * other)
        
    def __truediv__(self, other):
        if isinstance(other, Size):
            return Size(self.width / other.width, self.height / other.height)
        return Size(self.width / other, self.height / other)
        
    def __floordiv__(self, other):
        if isinstance(other, Size):
            return Size(self.width / other.width, self.height / other.height)
        return Size(self.width / other, self.height / other)
        
    def __add__(self, other):
        if isinstance(other, Size):
            return Size(self.width + other.width, self.height + other.height)
        return Size(self.width + other, self.height + other)
        
    def __sub__(self, other):
        if isinstance(other, Size):
            return Size(self.width - other.width, self.height - other.height)
        return Size(self.width - other, self.height - other)
        
class RangePP:
    """
    Range from begin position to end position.
    """
    def __init__(self, begin, end):
        """
        :param UnderGUI.Pos                        begin:
        :param UnderGUI.Pos                        end:
        """
        self.begin = begin
        self.end = end

    def to_area(self):
        """
        Converts to UnderGUI.Area.
        
        :rtype: UnderGUI.Area
        """
        return Area(self.begin.x, self.begin.y, self.end.x - self.begin.x, self.end.y - self.begin.y)
    
    def is_in(self, pos):
        """
        :param UnderGUI.Pos                        pos:
        :rtype: bool
        :return: True - if position is in range, False - otherwise.
        """
        return self.begin <= pos and pos < self.end
        
    def __eq__(self, other):
        return self.begin == other.begin and self.end == other.end
        
    def __ne__(self, other):
        return self.begin != other.begin or self.end != other.end
        
    def __mul__(self, other):
        if isinstance(other, RangePP):
            return RangePP(begin = self.begin * other.begin, end = self.end * other.end)
        return RangePP(begin = self.begin * other, end = self.end * other)
        
    def __truediv__(self, other):
        if isinstance(other, RangePP):
            return RangePP(begin = self.begin / other.begin, end = self.end / other.end)
        return RangePP(begin = self.begin / other, end = self.end / other)
        
    def __floordiv__(self, other):
        if isinstance(other, RangePP):
            return RangePP(begin = self.begin / other.begin, end = self.end / other.end)
        return RangePP(begin = self.begin / other, end = self.end / other)
        
    def __add__(self, other):
        if isinstance(other, RangePP):
            return RangePP(begin = self.begin + other.begin, end = self.end + other.end)
        return RangePP(begin = self.begin + other, end = self.end + other)
        
    def __sub__(self, other):
        if isinstance(other, RangePP):
            return RangePP(begin = self.begin - other.begin, end = self.end - other.end)
        return RangePP(begin = self.begin - other, end = self.end - other)
    
    
class Range(RangePP):
    def __init__(self, x1, y1, x2, y2):
        super().__init__(Pos(x1, y1), Pos(x2, y2))
        
class RangeF(Range):
    """
    Range in floats.
    """
    def __init__(self, x1, y1, x2, y2):
        super().__init__(float(x1), float(y1), float(x2), float(y2))
        
class AreaPS:
    def __init__(self, pos, size):
        self.pos    = pos
        self.size   = size
        
    def to_range(self):
        """
        Converts to UnderGUI.Range.
        
        :rtype: UnderGUI.Range
        """
        return RangePP(self.pos, self.pos + self.size)
    
    def is_in(self, pos):
        """
        :param UnderGUI.Pos                        pos:
        :rtype: bool
        :return: True - if position is in area, False - otherwise.
        """
        return self.to_range().is_in(pos)
    
    def __eq__(self, other):
        return self.pos == other.pos and self.size == other.size
    
    def __ne__(self, other):
        return self.pos != other.pos or self.size != other.size
    
class Area(AreaPS):
    def __init__(self, x, y, width, height):
        super().__init__(Pos(x, y), Size(width, height))

class ImageData:
    """
    :ivar bytes                                    data:
    :ivar int                                      width:
    :ivar int                                      height:
    """
    def __init__(self, data = None, width = 0, height = 0):
        self.data           = data          if data else b'' # bytes
        self.width          = width
        self.height         = height
    
class SizeUnit(Enum): 
    POINT           = 0
    PIXEL           = 1

class FontStyle(Enum):
    NORMAL          = 0
    BOLD            = 1
    ITALIC          = 2
    BOLD_AND_ITALIC = 3

class FontInfo:
    """
    :ivar str                                      name:
    :ivar int                                      size:
    :ivar UnderGUI.FontStyle                       style:
    :ivar UnderGUI.SizeUnit                        size_unit:
    """
    def __init__(self, name, size = 16, style = FontStyle.NORMAL, size_unit = SizeUnit.PIXEL):
        self.name       = name
        self.size       = size
        self.style      = style
        
        self.size_unit  = size_unit
        
class FontData:
    """
    :ivar bytes                                    data:
    :ivar UnderGUI.PixelFormat                     pixel_format:
    :ivar UnderGUI.Size                            size:
    :ivar dict(int, RangeF)                        glyph_texture_locations:
    """
    def __init__(self, data = None, pixel_format = PixelFormat.RGBA, size = None, glyph_texture_locations = None):
        """
        :param bytes                                   data:
            Pixels of font texture.
        :param UnderGUI.PixelFormat                    pixel_format:
        :param UnderGUI.Size                           size:
            Size of font texture.
        :param dict(int, RangeF)                       glyph_texture_locations:
            Maps glyph code to location in font texture. Range values are in normalized coordinates, from 0 to 1.
        """
        self.data                       = data if data else b''
        self.pixel_format               = pixel_format
        self.size                       = size if size else Size(0, 1)
        
        self.glyph_texture_locations    = glyph_texture_locations if glyph_texture_locations else {}
        
class FontSource:
    """
    :ivar str                                      normal_url:
    :ivar str                                      bold_url:
    :ivar str                                      italic_url:
    :ivar str                                      bold_and_italic_url:
    """
    def __init__(self, normal_url, bold_url, italic_url, bold_and_italic_url):
        self.normal_url          = normal_url
        self.bold_url            = bold_url
        self.italic_url          = italic_url
        self.bold_and_italic_url = bold_and_italic_url
    

class FontSourceRegister:
    """
    :ivar dict(str, FontSource)                    _register:
        Maps name of the font to its source locations.
    """
    def __init__(self):
        self._register = {}
        
    def add(self, font_name, font_source):  
        """
        :param str                                     font_name:
        :param FontSource                              font_source:
        """
        self._register[font_name] = font_source
        
    def get(self, font_name, font_style):
        """
        :param str                                     font_name:
        :param FontStyle                               font_style:
        """
        if font_name not in self._register:
            return ""
        else:
            font_source = self._register[font_name]

            return {
                FontStyle.NORMAL            : font_source.normal_url,
                FontStyle.BOLD              : font_source.bold_url,
                FontStyle.ITALIC            : font_source.italic_url,
                FontStyle.BOLD_AND_ITALIC   : font_source.bold_and_italic_url,
            }.get(font_style, "")



