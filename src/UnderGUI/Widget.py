from .Commons   import *
from .Window    import *

__all__ = ['Widget']

class Widget:
    """
    :ivar UnderGUI.Widget                      _parent:
    :ivar list(UnderGUI.Widget)                _childs:
    :ivar UnderGUI.Range                       _range:
    :ivar UnderGUI.AnchorGroup                 _anchor_group:
    :ivar UnderGUI.Window                      _window:
    """
    def __init__(self, parent, area_or_range, anchor_group = None, window = None):
        """
        :param UnderGUI.Widget or None             parent:
        :param UnderGUI.Area or UnderGUI.Range     area_or_range:
        :param UnderGUI.AnchorGroup or None        anchor_group:
        :param UnderGUI.Window or None             window:
        """
        self._parent        = parent
        self._childs        = []
        self._range         = area_or_range             if isinstance(area_or_range, Range) else area_or_range.to_range()
        self._anchor_group  = anchor_group              if anchor_group                     else AnchorGroup(AnchorAxisX.LEFT, AnchorAxisY.BOTTOM, AnchorAxisX.LEFT, AnchorAxisY.BOTTOM)
        self._window        = window                    if not self._parent                 else self._parent._window
        
    # to override
    def _update(self):
        pass
       
    # to override 
    def _draw(self):
        pass
    
    def _update_all(self):
        self._update()
        for child in self._childs:
            child._update_all()
            
    def _draw_all(self):
        self._draw()
        for child in self._childs:
            child._draw_all()
            
    def draw(self):
        self._update_all()
        self._draw_all()
            
            


            
        