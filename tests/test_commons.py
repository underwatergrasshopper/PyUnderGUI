import math
from TestKit import *
from UnderGUI.Commons import *

__all__ = ['test_commons']

def test_commons():
    ### Pos ###
    pos = Pos(1, 2)
    assert pos.x == 1 and pos.y == 2
    
    assert Pos(1, 2) == Pos(1, 2)
    assert (Pos(1, 2) == Pos(1, 3)) == False
    assert (Pos(1, 2) == Pos(5, 2)) == False
    assert (Pos(1, 2) == Pos(2, 1)) == False

    assert (Pos(1, 2) != Pos(1, 2)) == False
    assert Pos(1, 2) != Pos(1, 3)
    assert Pos(1, 2) != Pos(5, 2)
    assert Pos(1, 2) != Pos(2, 1)
    
    assert Pos(2, 3) * Pos(10, 100) == Pos(20, 300)
    assert Pos(20, 300) / Pos(10, 100) == Pos(2, 3)
    assert Pos(40, 50) + Pos(1, 2) == Pos(41, 52)
    assert Pos(40, 50) - Pos(1, 2) == Pos(39, 48)

    assert Pos(20, 30) / 10 == Pos(2, 3)
    assert Pos(2, 3) * 10 == Pos(20, 30)
    assert Pos(40, 50) + 2 == Pos(42, 52)
    assert Pos(40, 50) - 2 == Pos(38, 48)
      
    assert (Pos(2, 5) < Pos(3, 6)) == True
    assert (Pos(2, 5) < Pos(2, 6)) == False
    assert (Pos(2, 5) < Pos(3, 5)) == False
    assert (Pos(2, 5) < Pos(2, 5)) == False
    assert (Pos(2, 5) < Pos(1, 5)) == False
    assert (Pos(2, 5) < Pos(2, 4)) == False
    assert (Pos(2, 5) < Pos(1, 4)) == False
    
    assert (Pos(2, 5) <= Pos(3, 6)) == True
    assert (Pos(2, 5) <= Pos(2, 6)) == True
    assert (Pos(2, 5) <= Pos(3, 5)) == True
    assert (Pos(2, 5) <= Pos(2, 5)) == True
    assert (Pos(2, 5) <= Pos(1, 5)) == False
    assert (Pos(2, 5) <= Pos(2, 4)) == False
    assert (Pos(2, 5) <= Pos(1, 4)) == False
    
    assert (Pos(3, 6) > Pos(2, 5)) == True
    assert (Pos(3, 6) > Pos(3, 5)) == False
    assert (Pos(3, 6) > Pos(2, 6)) == False
    assert (Pos(3, 6) > Pos(3, 6)) == False
    assert (Pos(3, 6) > Pos(3, 7)) == False
    assert (Pos(3, 6) > Pos(4, 6)) == False
    assert (Pos(3, 6) > Pos(4, 7)) == False
    
    assert (Pos(3, 6) >= Pos(2, 5)) == True
    assert (Pos(3, 6) >= Pos(3, 5)) == True
    assert (Pos(3, 6) >= Pos(2, 6)) == True
    assert (Pos(3, 6) >= Pos(3, 6)) == True
    assert (Pos(3, 6) >= Pos(3, 7)) == False
    assert (Pos(3, 6) >= Pos(4, 6)) == False
    assert (Pos(3, 6) >= Pos(4, 7)) == False
    
    ### Size ###
    size = Size(1, 2)
    assert size.width == 1 and size.height == 2
    
    assert Size(1, 2) == Size(1, 2)
    assert (Size(1, 2) == Size(1, 3)) == False
    assert (Size(1, 2) == Size(5, 2)) == False
    assert (Size(1, 2) == Size(2, 1)) == False

    assert (Size(1, 2) != Size(1, 2)) == False
    assert Size(1, 2) != Size(1, 3)
    assert Size(1, 2) != Size(5, 2)
    assert Size(1, 2) != Size(2, 1)
    
    assert Size(2, 3) * Size(10, 100) == Size(20, 300)
    assert Size(20, 300) / Size(10, 100) == Size(2, 3)
    assert Size(40, 50) + Size(1, 2) == Size(41, 52)
    assert Size(40, 50) - Size(1, 2) == Size(39, 48)

    assert Size(20, 30) / 10 == Size(2, 3)
    assert Size(2, 3) * 10 == Size(20, 30)
    assert Size(40, 50) + 2 == Size(42, 52)
    assert Size(40, 50) - 2 == Size(38, 48)
      
    assert (Size(2, 5) < Size(3, 6)) == True
    assert (Size(2, 5) < Size(2, 6)) == False
    assert (Size(2, 5) < Size(3, 5)) == False
    assert (Size(2, 5) < Size(2, 5)) == False
    assert (Size(2, 5) < Size(1, 5)) == False
    assert (Size(2, 5) < Size(2, 4)) == False
    assert (Size(2, 5) < Size(1, 4)) == False
    
    assert (Size(2, 5) <= Size(3, 6)) == True
    assert (Size(2, 5) <= Size(2, 6)) == True
    assert (Size(2, 5) <= Size(3, 5)) == True
    assert (Size(2, 5) <= Size(2, 5)) == True
    assert (Size(2, 5) <= Size(1, 5)) == False
    assert (Size(2, 5) <= Size(2, 4)) == False
    assert (Size(2, 5) <= Size(1, 4)) == False
    
    assert (Size(3, 6) > Size(2, 5)) == True
    assert (Size(3, 6) > Size(3, 5)) == False
    assert (Size(3, 6) > Size(2, 6)) == False
    assert (Size(3, 6) > Size(3, 6)) == False
    assert (Size(3, 6) > Size(3, 7)) == False
    assert (Size(3, 6) > Size(4, 6)) == False
    assert (Size(3, 6) > Size(4, 7)) == False
    
    assert (Size(3, 6) >= Size(2, 5)) == True
    assert (Size(3, 6) >= Size(3, 5)) == True
    assert (Size(3, 6) >= Size(2, 6)) == True
    assert (Size(3, 6) >= Size(3, 6)) == True
    assert (Size(3, 6) >= Size(3, 7)) == False
    assert (Size(3, 6) >= Size(4, 6)) == False
    assert (Size(3, 6) >= Size(4, 7)) == False
    
    ### Pos and Size ###
    assert Pos(2, 3) * Size(10, 100) == Pos(20, 300)
    assert Pos(20, 300) / Size(10, 100) == Pos(2, 3)
    assert Pos(40, 50) + Size(1, 2) == Pos(41, 52)
    assert Pos(40, 50) - Size(1, 2) == Pos(39, 48)
    
    assert Pos(1, 2).to_size() == Size(1, 2)
    assert Size(1, 2).to_pos() == Pos(1, 2)
    
    ### Span ###
    span = Span(1, 2, 3, 4)
    assert span.x1 == 1 and span.y1 == 2 and span.x2 == 3 and span.y2 == 4
    
    assert span.get_from_pos() == Pos(1, 2)
    assert span.get_to_pos()   == Pos(3, 4)
    
    assert Span(0, 1, 2, 3) == Span(0, 1, 2, 3)
    assert (Span(0, 1, 2, 3) == Span(10, 1, 2, 3)) == False
    assert (Span(0, 1, 2, 3) == Span(0, 11, 2, 3)) == False
    assert (Span(0, 1, 2, 3) == Span(1, 1, 12, 3)) == False
    assert (Span(0, 1, 2, 3) == Span(1, 1, 2, 13)) == False

    assert (Span(0, 1, 2, 3) != Span(0, 1, 2, 3)) == False
    assert Span(0, 1, 2, 3) != Span(10, 1, 2, 3)
    assert Span(0, 1, 2, 3) != Span(0, 11, 2, 3)
    assert Span(0, 1, 2, 3) != Span(1, 1, 12, 3)
    assert Span(0, 1, 2, 3) != Span(1, 1, 2, 13)

    assert (Span(5, 2, 3, 4) * Span(10, 100, 1000, 10000)) == Span(50, 200, 3000, 40000)
    assert (Span(6, 20, 60, 3000) / Span(2, 5, 10, 100)) == Span(3, 4, 6, 30)
    assert (Span(6.0, 20.0, 60.0, 3000.0) / Span(2.0, 5.0, 10.0, 100.0)) == Span(3.0, 4.0, 6.0, 30.0)
    assert (Span(5, 2, 3, 4) + Span(10, 100, 1000, 10000)) == Span(15, 102, 1003, 10004)
    assert (Span(10, 20, 30, 40) - Span(1, 2, 3, 4)) == Span(9, 18, 27, 36)
    
    assert (Span(1, 2, 3, 4) * 10) == Span(10, 20, 30, 40)
    assert (Span(10, 20, 30, 40) / 10) == Span(1, 2, 3, 4)
    assert (Span(10.0, 20.0, 30.0, 40.0) / 10.0) == Span(1.0, 2.0, 3.0, 4.0)
    assert (Span(1, 2, 3, 4) + 10) == Span(11, 12, 13, 14)
    assert (Span(10, 20, 30, 40) - 1) == Span(9, 19, 29, 39)
    
    assert Span(3, 5, 10, 20).is_in(Pos(3, 5)) == True
    assert Span(3, 5, 10, 20).is_in(Pos(4, 6)) == True
    assert Span(3, 5, 10, 20).is_in(Pos(9, 19)) == True
    assert Span(3, 5, 10, 20).is_in(Pos(2, 5)) == False
    assert Span(3, 5, 10, 20).is_in(Pos(3, 4)) == False
    assert Span(3, 5, 10, 20).is_in(Pos(2, 4)) == False
    assert Span(3, 5, 10, 20).is_in(Pos(9, 20)) == False  
    assert Span(3, 5, 10, 20).is_in(Pos(10, 19)) == False  
    assert Span(3, 5, 10, 20).is_in(Pos(10, 20)) == False  
    
    assert SpanF(0, 1, 2, 3)               == Span(0.0, 1.0, 2.0, 3.0)
    assert SpanI(0.1, 1.1, 2.1, 3.1)       == Span(0, 1, 2, 3)
    assert SpanPP(Pos(0, 1), Pos(2, 3))    == Span(0, 1, 2, 3) 
    
    assert SpanF(0.1, 1.1, 2.1, 3.1).to_span_i() == SpanI(0, 1, 2, 3)
    assert SpanI(0, 1, 2, 3).to_span_f() == SpanF(0, 1, 2, 3)
    
    assert Span(10, 20, 30, 40) / Size(10, 5) == Span(1, 4, 3, 8)
    assert Span(10, 20, 30, 40).get_normalized(10, 5) == Span(1, 4, 3, 8)
    assert Span(10, 20, 30, 40).get_normalized_s(Size(10, 5)) == Span(1, 4, 3, 8)
    
    assert Span(1, 2, 3, 4).to_tuple() == (1, 2, 3, 4)
    assert Span(1, 2, 3, 4).to_dict()  == {'x1' : 1, 'y1' : 2, 'x2' : 3, 'y2' : 4}
    
    span = Span(1, 2, 3, 4)
    
    span.flip_on_x_axis(10)
    assert span == Span(1, 6, 3, 8)
    span.flip_on_y_axis(10)
    assert span == Span(7, 6, 9, 8)
    
    ### Area ###
    area = Area(1, 2, 3, 4)
    assert area.x == 1 and area.y == 2 and area.width == 3 and area.height == 4
    
    assert area.get_pos() == Pos(1, 2)
    assert area.get_size() == Size(3, 4)
    
    area.set_pos(Pos(10, 20))
    assert area.x == 10 and area.y == 20 and area.width == 3 and area.height == 4 
    
    area.set_size(Size(30, 40))
    assert area.x == 10 and area.y == 20 and area.width == 30 and area.height == 40
    
    assert Area(0, 1, 2, 3) == Area(0, 1, 2, 3)
    assert (Area(0, 1, 2, 3) == Area(10, 1, 2, 3)) == False
    assert (Area(0, 1, 2, 3) == Area(0, 11, 2, 3)) == False
    assert (Area(0, 1, 2, 3) == Area(1, 1, 12, 3)) == False
    assert (Area(0, 1, 2, 3) == Area(1, 1, 2, 13)) == False
    
    assert (Area(0, 1, 2, 3) != Area(0, 1, 2, 3)) == False
    assert Area(0, 1, 2, 3) != Area(10, 1, 2, 3)
    assert Area(0, 1, 2, 3) != Area(0, 11, 2, 3)
    assert Area(0, 1, 2, 3) != Area(1, 1, 12, 3)
    assert Area(0, 1, 2, 3) != Area(1, 1, 2, 13)
    
    assert Area(3, 5, 7, 15).is_in(Pos(3, 5)) == True
    assert Area(3, 5, 7, 15).is_in(Pos(4, 6)) == True
    assert Area(3, 5, 7, 15).is_in(Pos(9, 19)) == True
    assert Area(3, 5, 7, 15).is_in(Pos(2, 5)) == False
    assert Area(3, 5, 7, 15).is_in(Pos(3, 4)) == False
    assert Area(3, 5, 7, 15).is_in(Pos(2, 4)) == False
    assert Area(3, 5, 7, 15).is_in(Pos(9, 20)) == False  
    assert Area(3, 5, 7, 15).is_in(Pos(10, 19)) == False  
    assert Area(3, 5, 7, 15).is_in(Pos(10, 20)) == False  
    
    assert Area(1, 2, 3, 4) + Pos(10, 20) == Area(11, 22, 3, 4)
    assert Area(1, 2, 3, 4) + Size(10, 20) == Area(1, 2, 13, 24)
    
    assert Area(1, 2, 3, 4).to_tuple() == (1, 2, 3, 4)
    assert Area(1, 2, 3, 4).to_dict() == {'x' : 1, 'y' : 2, 'width' : 3, 'height' : 4}
    
    ### Area and Span ###
    assert Area(1, 2, 10, 20).to_span() == Span(1, 2, 11, 22)
    assert Span(1, 2, 11, 22).to_area() == Area(1, 2, 10, 20)
    
    ### FontInfo ###
    font_info = FontInfo("Courier New", 22, FontStyle.ITALIC, SizeUnit.POINT)
    assert font_info.name       == "Courier New"
    assert font_info.size       == 22
    assert font_info.style      == FontStyle.ITALIC
    assert font_info.size_unit  == SizeUnit.POINT
    
    ### FontData ###
    font_data = FontData()
    assert font_data.texture_data.data          == b''
    assert font_data.texture_data.pixel_format  == PixelFormat.UNKNOWN
    assert font_data.texture_data.size          == Size(0, 1)
    assert font_data.texture_glyph_infos        == {}
    assert font_data.max_glyph_height           == 0

    font_data = FontData(TextureData(b'abc', PixelFormat.RGBA, Size(12, 13)), {4 : (1.0, 2.0, 3.0, 4.0)}, 10)
    assert font_data.texture_data.data          == b'abc'
    assert font_data.texture_data.pixel_format  == PixelFormat.RGBA
    assert font_data.texture_data.size          == Size(12, 13)
    assert font_data.texture_glyph_infos        == {4 : (1.0, 2.0, 3.0, 4.0)}
    assert font_data.max_glyph_height           == 10
    
    ### FontSource ###
    font_source = FontSource("a", "b", "c", "d")
    assert font_source.normal_url           == "a"
    assert font_source.bold_url             == "b"
    assert font_source.italic_url           == "c"
    assert font_source.bold_and_italic_url  == "d"
    
    ### FontSourceRegister ###
    register = FontSourceRegister()
    assert register.get("x", FontStyle.BOLD)    == ""
    
    register.add("x", FontSource("a", "b", "c", "d"))
    register.add("y", FontSource(normal_url = "a2", bold_url = "b2", italic_url = "c2", bold_and_italic_url = "d2"))
    
    assert register.get("x", FontStyle.BOLD)            == "b"
    
    assert register.get("y", FontStyle.NORMAL)          == "a2"
    assert register.get("y", FontStyle.BOLD)            == "b2"
    assert register.get("y", FontStyle.ITALIC)          == "c2"
    assert register.get("y", FontStyle.BOLD_AND_ITALIC) == "d2"
    assert register.get("y", 100) == ""
    
    ### GlyphCodeBlock ###
    glyph_code_block = GlyphCodeBlock(10, 20)
    assert glyph_code_block.first == 10
    assert glyph_code_block.last == 20
    
    glyph_code_block_group = GlyphCodeBlockGroup(GlyphCodeBlock(10, 20)) + GlyphCodeBlockGroup(GlyphCodeBlock(21, 30), GlyphCodeBlock(31, 40))
    assert glyph_code_block_group.blocks[0].first == 10
    assert glyph_code_block_group.blocks[0].last == 20
    assert glyph_code_block_group.blocks[1].first == 21
    assert glyph_code_block_group.blocks[1].last == 30
    assert glyph_code_block_group.blocks[2].first == 31
    assert glyph_code_block_group.blocks[2].last == 40
    
    
    ### AnchorGroup ###
    anchor_group = AnchorGroup(AnchorAxisX.LEFT, AnchorAxisY.BOTTOM, AnchorAxisX.MIDDLE, AnchorAxisY.TOP)
    assert anchor_group.x1_anchor == AnchorAxisX.LEFT and anchor_group.y1_anchor == AnchorAxisY.BOTTOM and anchor_group.x2_anchor == AnchorAxisX.MIDDLE and anchor_group.y2_anchor == AnchorAxisY.TOP 
        
    anchor_group = AnchorGroup(AnchorAxisX.LEFT, AnchorAxisY.BOTTOM, AnchorAxisX.LEFT, AnchorAxisY.MIDDLE)
    assert anchor_group.x1_anchor == AnchorAxisX.LEFT and anchor_group.y1_anchor == AnchorAxisY.BOTTOM and anchor_group.x2_anchor == AnchorAxisX.LEFT and anchor_group.y2_anchor == AnchorAxisY.MIDDLE 
    
    anchor_group = make_anchor_group("")
    assert anchor_group.x1_anchor == AnchorAxisX.LEFT and anchor_group.y1_anchor == AnchorAxisY.BOTTOM and anchor_group.x2_anchor == AnchorAxisX.LEFT and anchor_group.y2_anchor == AnchorAxisY.BOTTOM 
    
    anchor_group = make_anchor_group("R")
    assert anchor_group.x1_anchor == AnchorAxisX.RIGHT and anchor_group.y1_anchor == AnchorAxisY.BOTTOM and anchor_group.x2_anchor == AnchorAxisX.LEFT and anchor_group.y2_anchor == AnchorAxisY.BOTTOM 
    
    anchor_group = make_anchor_group("MT")
    assert anchor_group.x1_anchor == AnchorAxisX.MIDDLE and anchor_group.y1_anchor == AnchorAxisY.TOP and anchor_group.x2_anchor == AnchorAxisX.LEFT and anchor_group.y2_anchor == AnchorAxisY.BOTTOM 
    
    anchor_group = make_anchor_group("LBR")
    assert anchor_group.x1_anchor == AnchorAxisX.LEFT and anchor_group.y1_anchor == AnchorAxisY.BOTTOM and anchor_group.x2_anchor == AnchorAxisX.RIGHT and anchor_group.y2_anchor == AnchorAxisY.BOTTOM 
    
    anchor_group = make_anchor_group("LBRM")
    assert anchor_group.x1_anchor == AnchorAxisX.LEFT and anchor_group.y1_anchor == AnchorAxisY.BOTTOM and anchor_group.x2_anchor == AnchorAxisX.RIGHT and anchor_group.y2_anchor == AnchorAxisY.MIDDLE 
    
    anchor_group = make_anchor_group("LBLB")
    assert anchor_group.x1_anchor == AnchorAxisX.LEFT and anchor_group.y1_anchor == AnchorAxisY.BOTTOM and anchor_group.x2_anchor == AnchorAxisX.LEFT and anchor_group.y2_anchor == AnchorAxisY.BOTTOM 
    
    anchor_group = make_anchor_group("LBRT")
    assert anchor_group.x1_anchor == AnchorAxisX.LEFT and anchor_group.y1_anchor == AnchorAxisY.BOTTOM and anchor_group.x2_anchor == AnchorAxisX.RIGHT and anchor_group.y2_anchor == AnchorAxisY.TOP 
    
    anchor_group = make_anchor_group("tertertdfgd")
    assert anchor_group.x1_anchor == AnchorAxisX.LEFT and anchor_group.y1_anchor == AnchorAxisY.BOTTOM and anchor_group.x2_anchor == AnchorAxisX.LEFT and anchor_group.y2_anchor == AnchorAxisY.BOTTOM 
    
    
    anchor_group = AnchorGroup(AnchorAxisX.LEFT, AnchorAxisY.BOTTOM, AnchorAxisX.LEFT, AnchorAxisY.BOTTOM)
    assert anchor_group.to_str() == "LBLB"
    
    anchor_group = AnchorGroup(AnchorAxisX.RIGHT, AnchorAxisY.TOP, AnchorAxisX.RIGHT, AnchorAxisY.TOP)
    assert anchor_group.to_str() == "RTRT"
    
    anchor_group = AnchorGroup(AnchorAxisX.MIDDLE, AnchorAxisY.MIDDLE, AnchorAxisX.RIGHT, AnchorAxisY.TOP)
    assert anchor_group.to_str() == "MMRT"
    
    anchor_group = AnchorGroup(AnchorAxisX.RIGHT, AnchorAxisY.TOP, AnchorAxisX.MIDDLE, AnchorAxisY.MIDDLE)
    assert anchor_group.to_str() == "RTMM"
    
if __name__ == "__main__":
    run_test(test_commons)



