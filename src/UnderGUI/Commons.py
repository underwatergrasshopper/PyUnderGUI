from enum import Enum

__all__ = [ 
    'PixelFormat',
    'Pos',
    'Size',
    'RangePP',
    'Range',
    'AreaPS',
    'Area',
    'ImageData'
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
    
