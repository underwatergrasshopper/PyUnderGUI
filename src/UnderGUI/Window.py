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
    
    def get_resolution(self):
        """
        :rtype UnderGUI.Size:
        """
        return self._resolution 