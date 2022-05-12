import os
import json

from .Commons           import *
from .Utility           import *
from .Exceptions        import *
from .Color             import *
from .GlyphCodeBlocks   import *

import PIL.ImageFont, PIL.Image, PIL.ImageDraw

__all__ = ['FontFetcher']   

class FontFetcher:
    """
    Fetches font's glyphs into texture and maps their locations.
    
    :ivar UnderGUI.Size                            _min_size:
    :ivar UnderGUI.FontData                        _font_data:
    :ivar UnderGUI.FontSourceRegister              _font_source_register:
    :ivar list(UnderGUI.GlyphCodeBlock)            _glyph_code_blocks:
    :ivar PIL.Image                                _image:
    :ivar str                                      _export_path:
    :ivar UnderGUI.FontInfo                        _font_info:
    """
    def __init__(self):
        self._min_size              = Size(0, 1)
        self._font_data             = FontData()
        self._font_source_register  = FontSourceRegister()
        self._glyph_code_blocks     = []
        
        self._image                 = None
        self._export_path           = ""
        self._font_info             = None

    def set_font_texture_minimal_size(self, min_size):
        """
        :param UnderGUI.Size                       min_size:
            Height of generated texture can be bigger than min_size.height, to fit all font glyphs of requested characters.
        """
        self._min_size = min_size
        
    def add_font_source(self, font_name, font_source):
        """
        :param str                                     font_name:
        :param UnderGUI.FontSource                     font_source:
            URLs of font files. Those files are searched firstly in run directory and secondary in system font folder (%windir%/Fonts for windows).
            Supported formats of font files: ttf.
        """
        self._font_source_register.add(font_name, font_source)
        
        
    def add_glyph_span(self, first, last):
        """
        Registers block of glyph codes from span <frist, last>, which will be drawn into generated font texture.
        
        :param int                                 first:
        :param int                                 last:
        """
        self._glyph_code_blocks += [GlyphCodeBlock(first, last)]
        
    def add_glyph_block(self, block):
        """
        Registers block of glyph codes, which will be drawn into generated font texture.
        
        :param UnderGUI.GlyphCodeBlock             block:
        """
        self._glyph_code_blocks += [block]
        
    def add_glyph_block_group(self, block_group):
        """
        Registers group of glyph code blocks, which will be drawn into generated font texture.
        
        :param UnderGUI.GlyphCodeBlock             block:
        """
        self._glyph_code_blocks += block_group.blocks
        
    def fetch(self, font_info, glyph_color = ColorI(255, 255, 255, 255), background_color = ColorI(0, 0, 0, 0)):  
        """
        Fetches font from file and creates texture.
        
        :param UnderGUI.FontInfo                   font_info:
        :param UnderGUI.Color                      background_color:
        :raises UnderGUI.Fail:
        """
        self.clear()
        
        font_source_url = self._font_source_register.get(font_info.name, font_info.style)
        if font_source_url == "":
            raise Fail("UnderGUI: No source files find for font '%s'." % (font_info.name))
        else:
            font_size = font_info.size
            
            if font_info.size_unit == SizeUnit.POINT:
                font_size = convert_size_in_points_to_size_in_pixels(font_size)
                    
            font = PIL.ImageFont.truetype(font_source_url, font_size, encoding = "unic")
            
            ascent, descent = font.getmetrics()
            glyph_height    = descent + ascent
            
            x = 0
            y = 0
            
            texture_glyph_infos = {}
            
            for glyph_code_block in self._glyph_code_blocks:
                for code in range(glyph_code_block.first, glyph_code_block.last + 1):
                    try:
                        # checks if code corresponds to glyph
                        glyph = chr(code)
                    except Exception as exception:
                        raise Fail("UnderGUI: %s" % str(exception)) from exception
                    else:
                        glyph_width, glyph_local_height = font.getsize(chr(code))
    
                        if (x + glyph_width) > self._min_size.width:
                            x = 0
                            y += glyph_height
    
                        area        = Area(x, y, glyph_width, glyph_height)
                        glyph_span = area.to_span()
                        texture_glyph_infos[code] = TextureGlyphInfo(glyph_span, area)
                        
                        x += glyph_width
    
            final_height = max(self._min_size.width, y + glyph_height)

            self._image = PIL.Image.new('RGBA', (self._min_size.width, final_height), background_color.to_color_i().get_rgba())
            draw = PIL.ImageDraw.Draw(self._image)
            
            for glyph_code in texture_glyph_infos:
                # creates font texture
                pos = texture_glyph_infos[glyph_code].area.get_pos()
                draw.text((pos.x, pos.y), chr(glyph_code), glyph_color.to_color_i().get_rgba(), font, spacing = 0)

                # converts coordinate to texture span
                glyph_span_ref = texture_glyph_infos[glyph_code].glyph_span
                glyph_span_ref.normalize(self._min_size.width, final_height)
                # flip from image coordinates (origin left-top) to texture coordinates (origin left-bottom).
                glyph_span_ref.flip_on_x_axis(1.0)  

            self._font_info = font_info
            self._font_data = FontData(get_texture_data_and_convert_to_rgba(self._image), texture_glyph_infos, glyph_height)

            
    def set_export_path(self, export_path):
        """
        :param str                                 export_path:
        """
        self._export_path = export_path
        
    def export(self):
        """
        Export texture and glyph locations to location set by 'set_export_path'.
        """
        if self._image and self._font_info:
            
            url = self._font_info.name
            
            if self._export_path != "":
                url = self._export_path + "/" + url
                
            if not os.path.exists(url):
                os.makedirs(url)
  
            self._image.save(url + "/Font.png", "PNG")
 
            # json.dump requires trivial structures to be able dump data to json file.
            trivialized_texture_glyph_infos = {}
            for code, info in self._font_data.texture_glyph_infos.items():
                combined = {}
                combined.update(info.glyph_span.to_dict())
                combined.update(info.area.to_dict())
                trivialized_texture_glyph_infos[code] = combined
                
            json_url = url + "/Font.json"
            try:
                with open(json_url, "w", encoding = "utf-8") as file:
                    json.dump(trivialized_texture_glyph_infos, file, ensure_ascii = False, indent = 4)
            except Exception as exception:
                raise Fail("UnderGUI: Cannot save font data in '%s' file. %s" % (json_url, str(exception))) from exception 

        
    def is_exported(self):
        """
        :rtype: bool
        """
        if self._image and self._font_info:
            
            url = self._font_info.name
            
            if self._export_path != "":
                url = self._export_path + "/" + url
                
            return os.path.exists(url)
        return False
        
    def show(self):
        if self._image:
            self._image.show()
        
    def clear(self):
        if self._image:
            self._image.close()
            del self._image
            
        self._image     = None
        self._font_info = None
        
    def get_font_data(self):
        """
        :rtype: UnderGUI.FontData
        """
        return self._font_data
