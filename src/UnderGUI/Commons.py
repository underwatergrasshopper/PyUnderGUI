# Set of useful classes and functions for UnderGUI.

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
    
# Position. 
class Pos:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def to_size(self):
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
        
# Range from point (x1, y1) to point (x2, y2).
class RangePP:
    def __init__(self, begin, end):
        self.begin = begin
        self.end = end

    # Converts Range to Area.
    def to_area(self):
        return Area(self.begin.x, self.begin.y, self.end.x - self.begin.x, self.end.y - self.begin.y)
    
    # Checks if position is inside range.
    # pos         (UnderGUI.Pos) Position.
    # Returns     (bool) true - if pos is inside range; false - otherwise.  
    def is_in(self, pos):
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
        
    # Converts Area to Range.
    def to_range(self):
        return RangePP(self.pos, self.pos + self.size)
    
    # Checks if position is inside area.
    # pos         (UnderGUI.Pos) Position.
    # Returns     (bool) true - if pos is inside area; false - otherwise.  
    def is_in(self, pos):
        return self.to_range().is_in(pos)
    
    def __eq__(self, other):
        return self.pos == other.pos and self.size == other.size
    
    def __ne__(self, other):
        return self.pos != other.pos or self.size != other.size
    
class Area(AreaPS):
    def __init__(self, x, y, width, height):
        super().__init__(Pos(x, y), Size(width, height))

class ImageData:
    def __init__(self, data = None, width = 0, height = 0):
        self.data           = data          if data else b'' # bytes
        self.width          = width
        self.height         = height
    
