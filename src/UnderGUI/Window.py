from .Commons       import *
from .Widget        import *
from .Exceptions    import *

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
        self._name                  = name
        self._resolution            = resolution
        
        self._drawable_area_size    = Size(0, 0)
        self._drawable_area         = Area(0, 0, 0, 0)
        self._drawable_span         = Span(0, 0, 0, 0)
        
        self._set_drawable_area_size(self._resolution)
        
        self._root_widget           = Root(self).place(self.get_drawable_area())


    def get_name(self):
        """
        :rtype str:
        """
        return self._name 
    
    def get_drawable_area_size(self):
        """
        :rtype UnderGUI.Size:
        """
        
        return self._drawable_area_size 
    
    def get_drawable_area(self):
        """
        :rtype UnderGUI.Area:
        """
        return self._drawable_area
    
    def get_drawable_span(self):
        """
        :rtype UnderGUI.Span:
        """
        return self._drawable_span
    
    def get_root_widget(self):
        """
        :rtype UnderGUI.Widget:
        """
        return self._root_widget
    
    def draw(self):
        self._root_widget.draw()
        
    def update(self):
        self._set_drawable_area_size(self._resolution)
        self._root_widget.update()
        
    def _set_drawable_area_size(self, size):
        self._drawable_area_size    = size
        self._drawable_area         = AreaPS(Pos(0, 0), self._drawable_area_size)
        self._drawable_span         = self._drawable_area.to_span()
    
class Root(Widget):
    def __init__(self, window):
        super().__init__(None, window)
               
                         


