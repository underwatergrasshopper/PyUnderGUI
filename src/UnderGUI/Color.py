__all__ = [ 
    'Color',
    'ColorF',
    'ColorI',
    'ColorB'
]

# Interface for color.
class Color:
    # Converts to ColorF.
    def to_color_f(self):
        pass
        
    # Converts to ColorI.
    def to_color_i(self):
        pass
    
    # Converts to ColorB.
    def to_color_b(self):
        pass
    
# Color with each channel in range (0, 1) as float.
class ColorF(Color):
    def __init__(self, r, g, b, a = 1.0):
        self.r = r
        self.g = g
        self.b = b
        self.a = a
        
    # Converts to ColorF.
    def to_color_f(self):
        return self
        
    # Converts to ColorI.
    def to_color_i(self):
        return ColorI(int(self.r * 255), int(self.g * 255), int(self.b * 255), int(self.a * 255))
    
    # Converts to ColorB.
    def to_color_b(self):
        return self.to_color_i().to_color_b()
        
# Color with each channel in range (0, 255) as int.   
class ColorI(Color):
    def __init__(self, r, g, b, a = 255):
        self.r = r
        self.g = g
        self.b = b
        self.a = a

    # Converts to ColorF.
    def to_color_f(self):
        return ColorF(self.r / 255.0, self.g / 255.0, self.b / 255.0, self.a / 255.0)
    
    # Converts to ColorI.
    def to_color_i(self):
        return self
    
    # Converts to ColorB.
    def to_color_b(self):
        return ColorB(self.r.to_bytes(1, byteorder='little'),  self.g.to_bytes(1, byteorder='little'),  self.b.to_bytes(1, byteorder='little'),  self.a.to_bytes(1, byteorder='little')) 
    
# Color with each channel in range (0, 255) as bytes.   
class ColorB(Color):
    # r         (is bytes) Red channel (one byte); or Red, Green, Blue channel (three bytes); or Red, Green, Blue and Alpha channel (four bytes) of color.
    # g         (is bytes) Green channel (one byte).
    # b         (is bytes) Blue channel (one byte).
    # a         (is bytes) Alpha channel (one byte).
    def __init__(self, r, g = None, b = None, a = b'\xFF'):
        if len(r) == 3:
            self.r = r[0:1]
            self.g = r[1:2]
            self.b = r[2:3]
            self.a = a
        elif len(r) == 4:
            self.r = r[0:1]
            self.g = r[1:2]
            self.b = r[2:3]
            self.a = r[3:4]
        else:
            self.r = r
            self.g = g
            self.b = b
            self.a = a
        
    # Converts to ColorF.
    def to_color_f(self):
        return self.to_color_i().to_color_f()

    # Converts to ColorI.
    def to_color_i(self):
        return ColorI(int.from_bytes(self.r, "little"),  int.from_bytes(self.g, "little"),  int.from_bytes(self.b, "little"),  int.from_bytes(self.a, "little"))
    
    # Converts to ColorB.
    def to_color_b(self):
        return self
    
    
    