# Base for Shunter class.

from UnderGUI.Utility import *

__all__ = ['ShunterBase']

# Communicates with graphical api to do specific action. Details in methods descriptions. All methods are for override.
class ShunterBase:
    def __init__(self):
        pass
        
    # Needs to be called before Texture.draw(...).
    def setup_texture_draw(self):
        pass
