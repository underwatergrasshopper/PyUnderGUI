from .Commons           import *
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
    def __init__(self, parent, span_or_area, anchor_group = None, window = None):
        """
        :param UnderGUI.Widget or None             parent:
        :param UnderGUI.Area or UnderGUI.Span      span_or_area:
        :param UnderGUI.AnchorGroup or None        anchor_group:
        :param UnderGUI.Window or None             window:
        
        :raise UnderGUI.Fail: When no Window class object is provided, either from parent or window varaible.
        """
        self._parent        = parent
        self._childs        = []
        
        if self._parent:
            self._parent._childs += [self]
        
        self._local_span    = span_or_area              if isinstance(span_or_area, Span)           else span_or_area.to_span()
        self._anchor_group  = anchor_group              if anchor_group                             else AnchorGroup(AnchorAxisX.LEFT, AnchorAxisY.BOTTOM, AnchorAxisX.LEFT, AnchorAxisY.BOTTOM)
        self._window        = window                    if not self._parent                         else self._parent._window
        if not self._window:
            raise Fail("UnderGUI: Widget: No Window class object have been provided.")
        
        self._global_span   = Span(0, 0, 0, 0)
        
        self._update()

    def _get_base_area(self):
        """
        :rtype: UnderGUI.Area
        """
        if self._parent:
            return self._parent._global_span.to_area() 
        return self._window.get_drawable_area()

    def _solve_global_span(self):
        self._global_span = convert_sub_span_to_left_bottom_orientation_in_area(self._get_base_area(), self._local_span, self._anchor_group)
        # print(self._global_span.x1, self._global_span.y1, self._global_span.x2, self._global_span.y2) # debug
        
    # to override
    def _update(self):
        self._solve_global_span()
       
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

    def get_global_span(self):
        """
        :rtype: UnderGUI.Span
        """
        return self._global_span
    
    def get_span(self):
        """
        :rtype: UnderGUI.Span
        """
        return self._local_span
    
    def get_global_area(self):
        """
        :rtype: UnderGUI.Area
        """
        return self._global_span.to_area()
    
    def get_area(self):
        """
        :rtype: UnderGUI.Area
        """
        return self._local_span.to_area()
            



            
        