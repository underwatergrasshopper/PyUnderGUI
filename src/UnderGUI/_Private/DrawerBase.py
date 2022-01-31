# Base for drawer.

from UnderGUI.Utility import *

__all__ = ['DrawerBase']

# Draws to window client area. All methods are for override.
class DrawerBase:
    def __init__(self):
        pass
    
    # Fills window client area with color.
    # color     (ColorF) Color of the fulfilment.
    def fill_view(self, color):
        pass
