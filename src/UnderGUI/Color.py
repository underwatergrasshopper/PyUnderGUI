__all__ = [ 
    'Color',
    'ColorF',
    'ColorI',
    'ColorB'
]

class Color:
    """
    Interface.
    """
    def __init__(self, r, g, b, a):
        self.r = r
        self.g = g
        self.b = b
        self.a = a
        
    # to override
    def to_color_f(self):
        """
        Converts to ColorF.
        
        :rtype: UnderGUI.ColorF
        """
        pass
        
    # to override
    def to_color_i(self):
        """
        Converts to ColorI.
        
        :rtype: UnderGUI.ColorI
        """
        pass
    
    # to override
    def to_color_b(self):
        """
        Converts to ColorB.
        
        :rtype: UnderGUI.ColorB
        """
        pass
    
class ColorF(Color):
    """
    Color with each channel as float.
    """
    
    def __init__(self, r, g, b, a = 1.0):
        """
        :param float                               r: 
            Red channel. Valid value range is from 0.0 to 1.0.
        :param float                               g: 
            Green channel. Valid value range is from 0.0 to 1.0.
        :param float                               b: 
            Blue channel. Valid value range is from 0.0 to 1.0.
        :param float, optional                     a: 
            Alpha channel. Valid value range is from 0.0 to 1.0.
        """
        super().__init__(float(r), float(g), float(b), float(a))
        
    # overrides
    def to_color_f(self):
        return self
        
    # overrides
    def to_color_i(self):
        return ColorI(int(self.r * 255), int(self.g * 255), int(self.b * 255), int(self.a * 255))
    
    # overrides
    def to_color_b(self):
        return self.to_color_i().to_color_b()
        

class ColorI(Color):
    """
    Color with each channel as int.
    """
    def __init__(self, r, g, b, a = 255):
        """
        :param int                                 r: 
            Red channel. Valid value range is from 0 to 255.
        :param int                                 g: 
            Green channel. Valid value range is from 0 to 255.
        :param int                                 b: 
            Blue channel. Valid value range is from 0 to 255.
        :param int, optional                       a: 
            Alpha channel. Valid value range is from 0 to 255.
        """
        super().__init__(int(r), int(g), int(b), int(a))

    # overrides
    def to_color_f(self):
        return ColorF(self.r / 255.0, self.g / 255.0, self.b / 255.0, self.a / 255.0)
    
    # overrides
    def to_color_i(self):
        return self
    
    # overrides
    def to_color_b(self):
        return ColorB(self.r.to_bytes(1, byteorder='little'),  self.g.to_bytes(1, byteorder='little'),  self.b.to_bytes(1, byteorder='little'),  self.a.to_bytes(1, byteorder='little')) 
     
class ColorB(Color):
    """
    Color with each channel as bytes.
    """
    def __init__(self, r, g = None, b = None, a = b'\xFF'):
        """
        :param bytes                               r: 
            If size of r is one byte, then contains Red channel.
            If size of r is three bytes, then contains Red, Green and Blue channel.
            If size of r is four bytes, then contains Red, Green, Blue and Alpha channel.
        :param bytes, optional                     g: 
            Green channel.
        :param bytes, optional                     b: 
            Blue channel.
        :param bytes, optional                     a: 
            Alpha channel.
        """
        if len(r) == 3:
            super().__init__(r[0:1], r[1:2], r[2:3], a)
        elif len(r) == 4:
            super().__init__(r[0:1], r[1:2], r[2:3], r[3:4])
        else:
            super().__init__(r, g, b, a)
        
    # overrides
    def to_color_f(self):
        return self.to_color_i().to_color_f()

    # overrides
    def to_color_i(self):
        return ColorI(int.from_bytes(self.r, "little"),  int.from_bytes(self.g, "little"),  int.from_bytes(self.b, "little"),  int.from_bytes(self.a, "little"))
    
    # overrides
    def to_color_b(self):
        return self
    
    
    