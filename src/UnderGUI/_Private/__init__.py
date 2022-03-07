from .Texture           import *
from .Drawer            import *
from .Shunter           import *

from .OpenGL_Texture    import *
from .OpenGL_Drawer     import *
from .OpenGL_Shunter    import *

def create_texture():
    return OpenGL_Texture()

def create_drawer():
    return OpenGL_Drawer()

def create_shunter():
    return OpenGL_Shunter()
