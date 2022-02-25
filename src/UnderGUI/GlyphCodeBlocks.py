from .Commons import GlyphCodeBlock, GlyphCodeBlockGroup

__all__ = [
    'UnicodeBlock',
    'UnicodeBlockGroup'
]

class UnicodeBlock:
    BASIC_LATIN                 = GlyphCodeBlock(0x0000, 0x007F)
    LATIN_1_SUPPLEMENT          = GlyphCodeBlock(0x0080, 0x00FF)
    LATIN_EXTENDED_A            = GlyphCodeBlock(0x0100, 0x017F)
    LATIN_EXTENDED_B            = GlyphCodeBlock(0x0180, 0x024F)
    IPA_EXTENSIONS              = GlyphCodeBlock(0x0250, 0x02AF)
    SPACING_MODIFIER_LETTERS    = GlyphCodeBlock(0x02B0, 0x02FF)
    COMBINING_DIACRITICAL_MARKS = GlyphCodeBlock(0x0300, 0x036F)
    GREEK_AND_COPTIC            = GlyphCodeBlock(0x0370, 0x03FF)
    
    CYRILLIC                    = GlyphCodeBlock(0x0400, 0x04FF)
    CYRILLIC_SUPPLEMENT         = GlyphCodeBlock(0x0500, 0x052F)

class UnicodeBlockGroup:
    ASCII   = GlyphCodeBlockGroup(
        UnicodeBlock.BASIC_LATIN
    )
    EUROPE  = GlyphCodeBlockGroup(
        UnicodeBlock.BASIC_LATIN,
        UnicodeBlock.LATIN_1_SUPPLEMENT,
        UnicodeBlock.LATIN_EXTENDED_A,
        UnicodeBlock.LATIN_EXTENDED_B,
        UnicodeBlock.IPA_EXTENSIONS,
        UnicodeBlock.SPACING_MODIFIER_LETTERS,
        UnicodeBlock.COMBINING_DIACRITICAL_MARKS,
        UnicodeBlock.GREEK_AND_COPTIC,
    )
    RUSSIA  = GlyphCodeBlockGroup(
        UnicodeBlock.CYRILLIC,
        UnicodeBlock.CYRILLIC_SUPPLEMENT,
    )
