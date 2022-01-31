# Base for drawer.
__all__ = ['Drawer']

# Draws to window client area. All methods are for override.
class Drawer:
    def __init__(self):
        pass
    
    # Fills window client area with color.
    # color     (ColorF) Color of the fulfilment.
    def fill_view(self, color):
        pass
