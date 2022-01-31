# Set of useful classes and functions for UnderGUI.

from enum import Enum

__all__ = [ 
    'PixelFormat',
    'Pos',
    'Range',
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
        return Pos(self.x * other, self.y * other)
        
    def __truediv__(self, other):
        if isinstance(other, Pos):
            return Pos(self.x / other.x, self.y / other.y)
        return Pos(self.x / other, self.y / other)
        
    def __floordiv__(self, other):
        if isinstance(other, Pos):
            return Pos(self.x / other.x, self.y / other.y)
        return Pos(self.x / other, self.y / other)
        
    def __add__(self, other):
        if isinstance(other, Pos):
            return Pos(self.x + other.x, self.y + other.y)
        return Pos(self.x + other, self.y + other)
        
    def __sub__(self, other):
        if isinstance(other, Pos):
            return Pos(self.x - other.x, self.y - other.y)
        return Pos(self.x - other, self.y - other)
        
# Range from point (x1, y1) to point (x2, y2).
class Range:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        
    # Converts Range to Area.
    def to_area(self):
        return Area(self.x1, self.y1, self.x2 - self.x1, self.y2 - self.y1)
    
    # Checks if position is inside range.
    # pos         (UnderGUI.Pos) Position.
    # Returns     (bool) true - if pos is inside range; false - otherwise.  
    def is_in(self, pos):
        return Pos(self.x1, self.y1) <= pos and pos < Pos(self.x2, self.y2)
        
    def __eq__(self, other):
        return self.x1 == other.x1 and self.y1 == other.y1 and self.x2 == other.x2 and self.y2 == other.y2
        
    def __ne__(self, other):
        return self.x1 != other.x1 or self.y1 != other.y1 or self.x2 != other.x2 or self.y2 != other.y2
        
    def __mul__(self, other):
        if isinstance(other, Range):
            return Range(self.x1 * other.x1, self.y1 * other.y1, self.x2 * other.x2, self.y2 * other.y2)
        return Range(self.x1 * other, self.y1 * other, self.x2 * other, self.y2 * other)
        
    def __truediv__(self, other):
        if isinstance(other, Range):
            return Range(self.x1 / other.x1, self.y1 / other.y1, self.x2 / other.x2, self.y2 / other.y2)
        return Range(self.x1 / other, self.y1 / other, self.x2 / other, self.y2 / other)
        
    def __floordiv__(self, other):
        if isinstance(other, Range):
            return Range(self.x1 / other.x1, self.y1 / other.y1, self.x2 / other.x2, self.y2 / other.y2)
        return Range(self.x1 / other, self.y1 / other, self.x2 / other, self.y2 / other)
        
    def __add__(self, other):
        if isinstance(other, Range):
            return Range(self.x1 + other.x1, self.y1 + other.y1, self.x2 + other.x2, self.y2 + other.y2)
        return Range(self.x1 + other, self.y1 + other, self.x2 + other, self.y2 + other)
        
    def __sub__(self, other):
        if isinstance(other, Range):
            return Range(self.x1 - other.x1, self.y1 - other.y1, self.x2 - other.x2, self.y2 - other.y2)
        return Range(self.x1 - other, self.y1 - other, self.x2 - other, self.y2 - other)
    
class Area:
    def __init__(self, x, y, width, height):
        self.x      = x
        self.y      = y
        self.width  = width
        self.height = height
        
    # Converts Area to Range.
    def to_range(self):
        return Range(self.x, self.y, self.x + self.width, self.y + self.height)
    
    # Checks if position is inside area.
    # pos         (UnderGUI.Pos) Position.
    # Returns     (bool) true - if pos is inside area; false - otherwise.  
    def is_in(self, pos):
        return self.to_range().is_in(pos)
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.width == other.width and self.height == other.height

class ImageData:
    def __init__(self, data = None, width = 0, height = 0):
        self.data       = data      if data else b''    # bytes
        self.width      = width
        self.height     = height
    
