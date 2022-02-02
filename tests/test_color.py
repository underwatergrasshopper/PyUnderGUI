import math

from TestKit import *

from UnderGUI.Color import *

__all__ = ['test_color']

def test_color():
    ### ColorF ###
    c = ColorF(1, 0.5, 0.75, 0.25).to_color_i()
    assert c.r == 255 and c.g == 127 and c.b == 191 and c.a == 63
    c = ColorF(1, 0.5, 0.75, 0.25).to_color_f()
    assert math.isclose(c.r, 1.0, abs_tol=0.01) and math.isclose(c.g, 0.5, abs_tol=0.01) and math.isclose(c.b, 0.75, abs_tol=0.01) and math.isclose(c.a, 0.25, abs_tol=0.01)
    c = ColorF(1, 0.5, 0.75, 0.25).to_color_b()
    assert c.r == b'\xFF' and c.g == b'\x7F' and c.b == b'\xBF' and c.a ==b'\x3F'
    
    ### ColorI ###
    c = ColorI(255, 127, 191, 63).to_color_i()
    assert c.r == 255 and c.g == 127 and c.b == 191 and c.a == 63
    c = ColorI(255, 127, 191, 63).to_color_f()
    assert math.isclose(c.r, 1.0, abs_tol=0.01) and math.isclose(c.g, 0.5, abs_tol=0.01) and math.isclose(c.b, 0.75, abs_tol=0.01) and math.isclose(c.a, 0.25, abs_tol=0.01)
    c = ColorI(255, 127, 191, 63).to_color_b()
    assert c.r == b'\xFF' and c.g == b'\x7F' and c.b == b'\xBF' and c.a ==b'\x3F'
    
    ### ColorB ###
    c = ColorB(b'\xFF', b'\x7F', b'\xBF', b'\x3F').to_color_i()
    assert c.r == 255 and c.g == 127 and c.b == 191 and c.a == 63
    c = ColorB(b'\xFF', b'\x7F', b'\xBF', b'\x3F').to_color_f()
    assert math.isclose(c.r, 1.0, abs_tol=0.01) and math.isclose(c.g, 0.5, abs_tol=0.01) and math.isclose(c.b, 0.75, abs_tol=0.01) and math.isclose(c.a, 0.25, abs_tol=0.01)
    c = ColorB(b'\xFF', b'\x7F', b'\xBF', b'\x3F').to_color_b()
    assert c.r == b'\xFF' and c.g == b'\x7F' and c.b == b'\xBF' and c.a ==b'\x3F'
    
    c = ColorB(b'\xFF\x7F\xBF', a = b'\x3F')
    assert c.r == b'\xFF' and c.g == b'\x7F' and c.b == b'\xBF' and c.a ==b'\x3F'
    
    c = ColorB(b'\xFF\x7F\xBF\x3F')
    assert c.r == b'\xFF' and c.g == b'\x7F' and c.b == b'\xBF' and c.a ==b'\x3F'
    
    # immediate tests
    #print(int.from_bytes(b'\xff', "little"))
    #print((255).to_bytes(1, byteorder='little'))

if __name__ == "__main__":
    run_test(test_color)
