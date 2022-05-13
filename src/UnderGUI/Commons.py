from enum import Enum

from .Exceptions import *

__all__ = [ 
    'PixelFormat',
    'Pos',
    'Size',
    'SpanPP',
    'Span',
    'SpanF',
    'SpanI',
    'AreaPS',
    'Area',
    'AreaI',
    'AreaF',
    'TextureData',
    'SizeUnit',
    'FontStyle',
    'FontInfo',
    'FontData',
    'FontSource',
    'FontSourceRegister',
    'GlyphCodeBlock',
    'GlyphCodeBlockGroup',
    'TextureGlyphInfo',
    'AnchorAxisX',
    'AnchorAxisY',
    'AnchorGroup',
    'make_anchor_group',
    'convert_sub_span_to_left_bottom_orientation',
    'convert_sub_span_to_left_bottom_orientation_in_area',
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
        
class Span:
    """
    Span from (x1, y1) to (x2, y2).

    :ivar auto                                x1:
    :ivar auto                                y1:
    :ivar auto                                x2:
    :ivar auto                                y2:
    """
    def __init__(self, x1, y1, x2, y2):
        """
        :param auto                                x1:
        :param auto                                y1:
        :param auto                                x2:
        :param auto                                y2:
        """
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def to_area(self):
        """
        Converts to Area.
        :rtype: UnderGUI.Area
        """
        return Area(self.x1, self.y1, self.x2 - self.x1, self.y2 - self.y1)
    
    def get_from_pos(self):
        """
        :rtype: UnderGUI.Pos
        :return: (x1, y1)
        """
        return Pos(self.x1, self.y1)
    
    def get_to_pos(self):
        """
        :rtype: UnderGUI.Pos
        :return: (x2, y2)
        """
        return Pos(self.x2, self.y2)
    
    def is_in(self, pos):
        """
        :param UnderGUI.Pos                        pos:
        :rtype: bool
        :return: True - if position is in span, False - otherwise.
        """
        return self.get_from_pos() <= pos and pos < self.get_to_pos()
    
    def to_span_i(self):
        """
        Converts to SpanI.
        :rtype: UnderGUI.SpanI
        """
        return SpanI(self.x1, self.y1, self.x2, self.y2)
    
    def to_span_f(self):
        """
        Converts to SpanF.
        :rtype: UnderGUI.SpanF
        """
        return SpanF(self.x1, self.y1, self.x2, self.y2)
    
    def to_tuple(self):
        """
        :rtype: tuple(auto, auto, auto, auto)
        """
        return (self.x1, self.y1, self.x2, self.y2)
    
    def to_dict(self):
        """
        :rtype: dict(str, float or int)
        """
        return {"x1" : self.x1, "y1" : self.y1, "x2" : self.x2, "y2" : self.y2}
    
    def normalize(self, width, height):
        """
        Divides span by size.
        
        :param int or float                       width:
        :param int or float                       height:
        """
        self.x1 /= width
        self.y1 /= height
        self.x2 /= width
        self.y2 /= height
        
    def normalize_s(self, size):
        """
        Divides span by size.
        
        :param UnderGUI.Size                      size:
        """
        self.normalize(size.widht, size.height)
    
    def get_normalized(self, width, height):
        """
        Divides span by size.
        
        :param int or float                       width:
        :param int or float                       height:
        :rtype: UnderGUI.Span
        :return: Span within space (width, height) described as fraction of (width, height).
        """
        return self / Size(width, height)
    
    def get_normalized_s(self, size):
        """
        Divides span by size.
        
        :param UnderGUI.Size                      size:
        :rtype: UnderGUI.Span
        :return: Span within space (size.width, size.height) described as fraction of (size.width, size.height).
        """
        return self.get_normalized(size.width, size.height)

    def flip_on_x_axis(self, height):
        """
        :param int or float                       height:
        """
        self.y1, self.y2 = height - self.y2, height - self.y1
        
    def flip_on_y_axis(self, width):
        """
        :param int or float                       height:
        """
        self.x1, self.x2 = width - self.x2, width - self.x1

    def __eq__(self, other):
        """
        :param UnderGUI.Span                      other:
        :rtype: bool
        """
        return self.get_from_pos() == other.get_from_pos() and self.get_to_pos() == other.get_to_pos()
        
    def __ne__(self, other):
        """
        :param UnderGUI.Span                      other:
        :rtype: bool
        """
        return self.get_from_pos() != other.get_from_pos() or self.get_to_pos() != other.get_to_pos()
        
    def __mul__(self, other):
        """
        :param UnderGUI.Span or int or float      other:
        :rtype: UnderGUI.Span 
        """
        if isinstance(other, Span):
            return Span(self.x1 * other.x1, self.y1 * other.y1, self.x2 * other.x2, self.y2 * other.y2)
        return Span(self.x1 * other, self.y1 * other, self.x2 * other, self.y2 * other)
        
    def __truediv__(self, other):
        """
        :param UnderGUI.Span UnderGUI.Size or int or float      other:
        :rtype: UnderGUI.Span 
        """
        if isinstance(other, Span):
            return Span(self.x1 / other.x1, self.y1 / other.y1, self.x2 / other.x2, self.y2 / other.y2)
        if isinstance(other, Size):
            return Span(self.x1 / other.width, self.y1 / other.height, self.x2 / other.width, self.y2 / other.height)
        return Span(self.x1 / other, self.y1 / other, self.x2 / other, self.y2 / other)
        
    def __floordiv__(self, other):
        """
        :param UnderGUI.Span UnderGUI.Size or int or float      other:
        :rtype: UnderGUI.Span 
        """
        if isinstance(other, Span):
            return Span(self.x1 / other.x1, self.y1 / other.y1, self.x2 / other.x2, self.y2 / other.y2)
        if isinstance(other, Size):
            return Span(self.x1 / other.width, self.y1 / other.height, self.x2 / other.width, self.y2 / other.height)
        return Span(self.x1 / other, self.y1 / other, self.x2 / other, self.y2 / other)
        
    def __add__(self, other):
        """
        :param UnderGUI.Span or int or float      other:
        :rtype: UnderGUI.Span 
        """
        if isinstance(other, Span):
            return Span(self.x1 + other.x1, self.y1 + other.y1, self.x2 + other.x2, self.y2 + other.y2)
        return Span(self.x1 + other, self.y1 + other, self.x2 + other, self.y2 + other)
        
    def __sub__(self, other):
        """
        :param UnderGUI.Span or int or float      other:
        :rtype: UnderGUI.Span 
        """
        if isinstance(other, Span):
            return Span(self.x1 - other.x1, self.y1 - other.y1, self.x2 - other.x2, self.y2 - other.y2)
        return Span(self.x1 - other, self.y1 - other, self.x2 - other, self.y2 - other)
    
class SpanPP(Span):
    """
    Span created from positions.
    """
    def __init__(self, from_pos, to_pos):
        """
        :param UnderGUI.Pos                        from_pos:
        :param UnderGUI.Pos                        to_pos:
        """
        super().__init__(from_pos.x, from_pos.y, to_pos.x, to_pos.y)
        
class SpanF(Span):
    """
    Span with values stored as floats.
    """
    def __init__(self, x1, y1, x2, y2):
        """
        :param float                               x1:
        :param float                               y1:
        :param float                               x2:
        :param float                               y2:
        """
        super().__init__(float(x1), float(y1), float(x2), float(y2))
        
    # overload
    def to_span_f(self):
        return self
        
class SpanI(Span):
    """
    Span with values stored as ints.
    """
    def __init__(self, x1, y1, x2, y2):
        """
        :param int                                 x1:
        :param int                                 y1:
        :param int                                 x2:
        :param int                                 y2:
        """
        super().__init__(int(x1), int(y1), int(x2), int(y2))
        
    # overload
    def to_span_i(self):
        return self
    
class Area:
    """
    Area beginning at location (x, y) with size of (width, height).

    :ivar auto                                x:
    :ivar auto                                y:
    :ivar auto                                width:
    :ivar auto                                height:
    """
    def __init__(self, x, y, width, height):
        """
        :param auto                                x:
        :param auto                                y:
        :param auto                                width:
        :param auto                                height:
        """
        self.x          = x
        self.y          = y
        self.width      = width
        self.height     = height
        
    def to_span(self):
        """
        Converts to UnderGUI.Span.
        
        :rtype: UnderGUI.Span
        """
        return Span(self.x, self.y, self.x + self.width, self.y + self.height)
    
    def is_in(self, pos):
        """
        :param UnderGUI.Pos                        pos:
        :rtype: bool
        :return: True - if position is in area, False - otherwise.
        """
        return self.to_span().is_in(pos)
    
    def set_pos(self, pos):
        """
        :param UnderGUI.Pos                        pos:
        """
        self.x = pos.x
        self.y = pos.y
    
    def get_pos(self):        
        """
        :rtype: UnderGUI.Pos 
        :return: (x, y) 
        """
        return Pos(self.x, self.y)
    
    def set_size(self, size):
        """
        :param UnderGUI.Size                       size:
        """
        self.width  = size.width
        self.height = size.height
    
    def get_size(self):        
        """
        :rtype: UnderGUI.Size  
        :return: (width, height) 
        """
        return Size(self.width, self.height)
    
    def to_tuple(self):
        """
        :rtype: tuple(auto, auto, auto, auto)
        """
        return (self.x, self.y, self.width, self.height)
    
    def to_dict(self):
        """
        :rtype: dict(str, float or int)
        """
        return {"x" : self.x, "y" : self.y, "width" : self.width, "height" : self.height}
    
    def __eq__(self, other):
        """
        :param UnderGUI.Area                       other:
        :rtype: bool
        """
        return self.get_pos() == other.get_pos() and self.get_size() == other.get_size()
    
    def __ne__(self, other):
        """
        :param UnderGUI.Area                       other:
        :rtype: bool
        """
        return self.get_pos() != other.get_pos() or self.get_size() != other.get_size()
    
    def __add__(self, other):
        """
        :param UnderGUI.Pos or UnderGUI.Size       other:
        :rtype: UnderGUI.Area
        :raises UnderGUI.Fail:
        """
        if isinstance(other, Pos):
            return Area(self.x + other.x, self.y + other.y, self.width, self.height)
        if isinstance(other, Size):
            return Area(self.x, self.y, self.width + other.width, self.height + other.height)
        raise Fail("UnderGUI: To UnderGUI.Area cannot be added anything other than UnderGUI.Pos or UnderGUI.Size.")
        
    def __sub__(self, other):
        """
        :param UnderGUI.Pos or UnderGUI.Size       other:
        :rtype: UnderGUI.Area
        :raises UnderGUI.Fail:
        """
        if isinstance(other, Pos):
            return Area(self.x - other.x, self.y- other.y, self.width, self.height)
        if isinstance(other, Size):
            return Area(self.x, self.y, self.width - other.width, self.height - other.height)
        raise Fail("UnderGUI: UnderGUI.Area cannot be subtracted by anything other than UnderGUI.Pos or UnderGUI.Size.")
    

class AreaF(Area):
    """
    Area with values stored as floats.
    """
    def __init__(self, x, y, width, height):
        """
        :param float                               x:
        :param float                               y:
        :param float                               width:
        :param float                               height:
        """
        super().__init__(float(x), float(y), float(width), float(height))


class AreaI(Area):
    """
    Area with values stored as ints.
    """
    def __init__(self, x, y, width, height):
        """
        :param int                                 x:
        :param int                                 y:
        :param int                                 width:
        :param int                                 height:
        """
        super().__init__(int(x), int(y), int(width), int(height))


class AreaPS(Area):
    """
    Area constructed from position and size.
    """
    def __init__(self, pos, size):
        """
        :param UnderGUI.Pos                        pos:
        :param UnderGUI.Size                       size:
        """
        super().__init__(pos.x, pos.y, size.width, size.height)


class TextureData:
    """
    :ivar bytes                                    data:
    :ivar UnderGUI.PixelFormat                     pixel_format:
    :ivar UnderGUI.Size                            size:
    """
    def __init__(self, data = None, pixel_format = PixelFormat.UNKNOWN, size = None):
        self.data           = data          if data else b''
        self.pixel_format   = pixel_format
        self.size           = size          if size else Size(0, 1)
    
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
        
class TextureGlyphInfo:
    """
    :ivar UnderGUI.SpanF                          glyph_span:
        Span where glyph is located in texture. Coordinate values are floats between 0 and 1 (normalized texture coordinates) with oringin at left-bottom.
    :ivar UnderGUI.Size                            size:
        Area where glyph is located in texture in pixels. Where coordinates system have origin at left-top.
    """
    def __init__(self, glyph_span, area):
        self.glyph_span    = glyph_span
        self.area           = area
        
        
class FontData:
    """
    :ivar UnderGUI.TextureData                     texture_data:
    :ivar dict(int, UnderGUI.TextureGlyphInfo)     texture_glyph_infos:
    :ivar int                                      max_glyph_height:
        In pixels.
    """
    def __init__(self, texture_data = None, texture_glyph_infos = None, max_glyph_height = 0):
        """
        :param UnderGUI.TextureData                    texture_data:
        :param dict(int, TextureGlyphInfo)             texture_glyph_infos:
        :param int                                     max_glyph_height:
            In pixels.
        """
        self.texture_data               = texture_data              if texture_data else TextureData()
        self.texture_glyph_infos        = texture_glyph_infos       if texture_glyph_infos else {}
        self.max_glyph_height           = max_glyph_height
        
        
        
        
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

class GlyphCodeBlock:
    """
    Represent subset set of characters (glyphs) from span: first to last (last is also included).
    :ivar int                                      first:
    :ivar int                                      last:
    """
    def __init__(self, first, last):
        self.first  = first
        self.last   = last

class GlyphCodeBlockGroup:
    """
    :ivar list(UnderGUI.GlyphCodeBlock)            blocks:
    """
    def __init__(self, *blocks):
        """
        :param UnderGUI.GlyphCodeBlock, ...            blocks:
        """
        self.blocks = [*blocks]
    
    def __add__(self, other):
        """
        :param UnderGUI.GlyphCodeBlockGroup            other:
        """
        combined = GlyphCodeBlockGroup()
        combined.blocks = self.blocks + other.blocks
        return combined

class AnchorAxisX(Enum):
    LEFT    = 0
    MIDDLE  = 1
    RIGHT   = 2
    
class AnchorAxisY(Enum):
    BOTTOM  = 0
    MIDDLE  = 1
    TOP     = 2
    
class AnchorGroup:
    """
    :ivar UnderGUI.AnchorAxisX                     x1_anchor:
    :ivar UnderGUI.AnchorAxisY                     y1_anchor:
    :ivar UnderGUI.AnchorAxisX                     x2_anchor:
    :ivar UnderGUI.AnchorAxisY                     y2_anchor:
    """
    def __init__(self, x1_anchor, y1_anchor, x2_anchor, y2_anchor):
        """
        :param UnderGUI.AnchorAxisX                    x1_anchor:
        :param UnderGUI.AnchorAxisY                    y1_anchor:
        :param UnderGUI.AnchorAxisX                    x2_anchor:
        :param UnderGUI.AnchorAxisY                    y2_anchor:
        """
        self.x1_anchor = x1_anchor
        self.y1_anchor = y1_anchor
        self.x2_anchor = x2_anchor
        self.y2_anchor = y2_anchor
        
    def to_str(self):
        """
        :rtype: str
        """
        def anchor_x_to_str(anchor):
            return {
                AnchorAxisX.LEFT    : "L",
                AnchorAxisX.MIDDLE  : "M",
                AnchorAxisX.RIGHT   : "R",
            }[anchor]
            
        def anchor_y_to_str(anchor):
            return {
                AnchorAxisY.BOTTOM  : "B",
                AnchorAxisY.MIDDLE  : "M",
                AnchorAxisY.TOP     : "T",
            }[anchor]
            
        return anchor_x_to_str(self.x1_anchor) + anchor_y_to_str(self.y1_anchor) + anchor_x_to_str(self.x2_anchor) + anchor_y_to_str(self.y2_anchor)
    
def make_anchor_group(anchor_string):
    """
    :param str                                    anchor_string: 
        Format "<X><Y><X><Y>" where:
        <X>
            L    - Left
            M    - Middle
            R    - Right
        <Y>
            B    - Bottom
            M    - Middle
            T    - Top
        
        Default string is "LBLB". anchor_string can have 0-4 characters. If 3 or few characters given then corresponding missing character are same as default.
            
        Examples:
        "LBTR"     - Left-Bottom Top-Right
        "LBLB"     - Left-Bottom Left-Bottom
        "LB"       - Left-Bottom Left-Bottom
        ""         - Left-Bottom Left-Bottom
    :rtype: UnderGUI.AnchorGroup
    """
    def char_to_anchor_x(c):
        return {
            "L" : AnchorAxisX.LEFT,
            "M" : AnchorAxisX.MIDDLE,
            "R" : AnchorAxisX.RIGHT,
        }.get(c, AnchorAxisX.LEFT)
        
    def char_to_anchor_y(c):
        return {
            "B" : AnchorAxisY.BOTTOM,
            "M" : AnchorAxisY.MIDDLE,
            "T" : AnchorAxisY.TOP,
        }.get(c, AnchorAxisY.BOTTOM)
    
    group = AnchorGroup(AnchorAxisX.LEFT, AnchorAxisY.BOTTOM, AnchorAxisX.LEFT, AnchorAxisY.BOTTOM)
    
    if len(anchor_string) == 0:
        return group
    group.x1_anchor = char_to_anchor_x(anchor_string[0])
    
    if len(anchor_string) == 1:
        return group
    group.y1_anchor = char_to_anchor_y(anchor_string[1])
    
    if len(anchor_string) == 2:
        return group
    group.x2_anchor = char_to_anchor_x(anchor_string[2])
    
    if len(anchor_string) == 3:
        return group
    group.y2_anchor = char_to_anchor_y(anchor_string[3])
    
    return group
    
def convert_sub_span_to_left_bottom_orientation(base_span, sub_span, anchor_group):
    """
    :param UnderGUI.Span                           base_span:
    :param UnderGUI.Span                           sub_span:
    :param UnderGUI.AnchorGroup                    anchor_group:
        Anchor group of sub_span towards base_span.
    :rtype UnderGUI.Span:
    """
    base_area = base_span.to_area()
    return convert_sub_span_to_left_bottom_orientation_in_area(base_area, sub_span, anchor_group)
    
def convert_sub_span_to_left_bottom_orientation_in_area(base_area, sub_span, anchor_group):
    """
    :param UnderGUI.Area                           base_area:
    :param UnderGUI.Span                           sub_span:
    :param UnderGUI.AnchorGroup                    anchor_group:
        Anchor group of sub_span towards base_area.
    :rtype UnderGUI.Span:
    """
    solved_span = Span(0, 0, 0, 0)
    
    if anchor_group.x1_anchor == AnchorAxisX.LEFT:
        solved_span.x1 = sub_span.x1 + base_area.x
    elif anchor_group.x1_anchor == AnchorAxisX.MIDDLE:
        solved_span.x1 = base_area.width / 2.0 + sub_span.x1 + base_area.x
    elif anchor_group.x1_anchor == AnchorAxisX.RIGHT:
        solved_span.x1 = base_area.width + sub_span.x1 + base_area.x
    
    if anchor_group.x2_anchor == AnchorAxisX.LEFT:
        solved_span.x2 = sub_span.x2 + base_area.x
    elif anchor_group.x2_anchor == AnchorAxisX.MIDDLE:
        solved_span.x2 = base_area.width / 2.0 + sub_span.x2 + base_area.x
    elif anchor_group.x2_anchor == AnchorAxisX.RIGHT:
        solved_span.x2 = base_area.width + sub_span.x2 + base_area.x
        
    if anchor_group.y1_anchor == AnchorAxisY.BOTTOM:
        solved_span.y1 = sub_span.y1 + base_area.y
    elif anchor_group.y1_anchor == AnchorAxisY.MIDDLE:
        solved_span.y1 = base_area.height / 2.0 + sub_span.y1 + base_area.y
    elif anchor_group.y1_anchor == AnchorAxisY.TOP:
        solved_span.y1 = base_area.height + sub_span.y1 + base_area.y
        
    if anchor_group.y2_anchor == AnchorAxisY.BOTTOM:
        solved_span.y2 = sub_span.y2 + base_area.y
    elif anchor_group.y2_anchor == AnchorAxisY.MIDDLE:
        solved_span.y2 = base_area.height / 2.0 + sub_span.y2 + base_area.y
    elif anchor_group.y2_anchor == AnchorAxisY.TOP:
        solved_span.y2 = base_area.height + sub_span.y2 + base_area.y
        
    return solved_span
    
    