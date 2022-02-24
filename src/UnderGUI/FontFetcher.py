from enum import Enum

from .Commons import *

__all__ = ['FontFetcher']   


class FontFetcher:
    """
    Fetches font's glyphs into texture and maps their locations.
    
    :ivar UnderGUI.Size                            _min_size:
    :ivar UnderGUI.FontData                        _font_data:
    """
    def __init__(self):
        self._min_size  = Size(0, 1)
        self._font_data = FontData()

    def set_font_texture_minimal_size(self, min_size):
        """
        :param UnderGUI.Size                       min_size:
            Height of generated texture can be bigger than min_size.height, to fit all font glyphs of requested characters.
        """
        self._min_size = min_size
        
    def fetch(self, font_info):   
        pass


"""   
FontFetcher

    add_character_range(first, last)
    add_character_block(character_block)
    add_character_block_group(character_block_gorup)
    
    add_font_source(font_name, font_url_group)
    
    set_export_path(directory_path) # /tests/_temp # not versioned
    is_exported() : .bool
    
    fetch(font_info)
    export()
    show()
    clear()

    get_font_data() : FontData
"""