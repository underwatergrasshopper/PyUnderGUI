from UnderGUI.Utility import *

# Communicates with graphical api to do specific action. Details in methods descriptions. All methods are for override.
class Shunter:
    def __init__(self):
        pass
        
    # Needs to be called before Texture.draw(...).
    def setup_texture_draw(self):
        pass
