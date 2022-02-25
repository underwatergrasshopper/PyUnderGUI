import TestKit

import shutil
import os

from UnderGUI import *
from UnderGUI._Private import *

################################################################################

if __name__ == "__main__":
    font_fetcher = FontFetcher()
    
    font_fetcher.add_font_source("Courier New", FontSource(normal_url = "cour.ttf", bold_url = "courbd.ttf", italic_url = "couri.ttf", bold_and_italic_url = "courbi.ttf"))
    
    font_fetcher.set_font_texture_minimal_size(Size(512, 512))
    #font_fetcher.add_glyph_range(0x0000, 0x007F)
    #font_fetcher.add_glyph_block(UnicodeBlock.LATIN_1_SUPPLEMENT)
    font_fetcher.add_glyph_block_group(UnicodeBlockGroup.EUROPE)
    font_fetcher.set_export_path("../temp_junk")
    
    font_fetcher.fetch(FontInfo("Courier New", 12, size_unit = SizeUnit.POINT), ColorF(0, 0, 0, 1))
    
    if os.path.exists("../temp_junk"):
        shutil.rmtree("../temp_junk")
    assert font_fetcher.is_exported() == False
    font_fetcher.export()
    assert font_fetcher.is_exported()
    font_fetcher.show()
    
    
    