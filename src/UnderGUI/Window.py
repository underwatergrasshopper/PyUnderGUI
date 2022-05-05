from .Commons import *

__all__ = ['Window']

class Window:
    """
    :ivar str                                      _name:
    :ivar UnderGUI.Size                            _resolution:
    """
    def __init__(self, name, resolution):
        """
        :param str                                 name:
        :param UnderGUI.Size                       resolution:
        """
        self._name          = name
        self._resolution    = resolution

    def get_name(self):
        """
        :rtype str:
        """
        return self._name 
    
    def get_drawable_area_size(self):
        """
        :rtype UnderGUI.Size:
        """
        # TODO: exclude title bar and frames, only client area by default
        return self._resolution 