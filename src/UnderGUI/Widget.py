from .Commons           import *
from .Window            import *
from .Color             import *
from .Exceptions        import *

from ._Private.Draw     import *

__all__ = ['Widget']

class Widget:
    """
    :ivar UnderGUI.Widget                      _parent:
    :ivar list(UnderGUI.Widget)                _childs:
    :ivar UnderGUI.Span                        _local_span:
    :ivar UnderGUI.AnchorGroup                 _anchor_group:
    :ivar UnderGUI.Window                      _window:
    """
    def __init__(self, parent, area_or_local_span, anchor_group = None, window = None):
        """
        :param UnderGUI.Widget or None             parent:
        :param UnderGUI.Area or UnderGUI.Span     area_or_local_span:
        :param UnderGUI.AnchorGroup or None        anchor_group:
        :param UnderGUI.Window or None             window:
        
        :raise UnderGUI.Fail: When no Window class object is provided, either from parent or window varaible.
        """
        self._parent        = parent
        self._childs        = []
        self._local_span   = area_or_local_span       if isinstance(area_or_local_span, Span)   else area_or_local_span.to_span()
        self._anchor_group  = anchor_group              if anchor_group                             else AnchorGroup(AnchorAxisX.LEFT, AnchorAxisY.BOTTOM, AnchorAxisX.LEFT, AnchorAxisY.BOTTOM)
        self._window        = window                    if not self._parent                         else self._parent._window
        
        if not self._window:
            raise Fail("UnderGUI: Widget: No Window class object have been provided.")
        
        self._solve_global_span()
        
    def _solve_global_span(self):
        base_area = self._parent.to_area() if self._parent else AreaPS(Pos(0, 0), self._window.get_drawable_area_size())
        
        self._global_span = convert_sub_span_to_left_bottom_orientation_in_area(
            base_area,
            self._local_span,
            self._anchor_group
        )
        
    # to override
    def _update(self):
        pass
       
    # to override 
    def _draw(self):
        fill_span(self._local_span, ColorF(1, 0, 0))
    
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
            
            


            
        