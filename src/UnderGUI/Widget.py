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
    def __init__(self, parent, window = None):
        """
        :param UnderGUI.Widget or None             parent:
        :param UnderGUI.Area or UnderGUI.Span      span_or_area:
        :param UnderGUI.AnchorGroup or None        anchor_group:
        :param UnderGUI.Window or None             window:
        
        :raise UnderGUI.Fail: When no Window class object is provided, either from parent or window varaible.
        """
        self._parent        = parent
        self._childs        = []
        
        self._window        = window if not self._parent else self._parent._window
        if not self._window:
            raise Fail("UnderGUI: Widget: No Window class object have been provided.")
        
        if self._parent:
            self._parent._childs += [self]
        
        self._local_span    = Span(0, 0, 0, 0)
        self._global_span   = Span(0, 0, 0, 0)
        self._anchor_group  = make_anchor_group("")

        self._is_marked_to_update   = False
        
    def _mark_to_update_up_tree(self):
        self._is_marked_to_update = True
        if self._parent:
            self._parent._mark_to_update_up_tree()
        
    def _mark_branch_to_update(self):
        self._is_marked_to_update = True
        for child in self._childs:
            child._mark_branch_to_update()
            
    def _mark_to_update(self):
        if self._parent:
            self._parent._mark_to_update_up_tree()
        self._mark_branch_to_update()
        
    def _update_if_marked(self):
        if self._is_marked_to_update:
            self._update()
            self._is_marked_to_update = False
        
        
    def place(self, span_or_area, anchor_string = ""):
        """
        :param UnderGUI.Span or UnderGUI.Area      span_or_area:
        :param str                                 anchor_string:
            Format "<AxisX><AxisY><AxisX><AxisY>", where each character is anchor for specific axis. They refers to span from (x1, y1) to (x2, y2).
            <AxisX>
                L    - Left
                M    - Middle
                R    - Right
            <AxisY>
                B    - Bottom
                M    - Middle
                T    - Top
            
            Default string is "LBLB". anchor_string can have 0-4 characters. If 3 or few characters given, then corresponding missing characters are same as default.
                
            Examples:
            "LBTR"     - Left-Bottom Top-Right
            "LBLB"     - Left-Bottom Left-Bottom
            "LB"       - Left-Bottom Left-Bottom
            ""         - Left-Bottom Left-Bottom
        :rtype: UnderGUI.Widget
        :return: Reference to self.
        """
        self._local_span    = span_or_area if isinstance(span_or_area, Span) else span_or_area.to_span()
        self._anchor_group  = make_anchor_group(anchor_string)
        self._update()
        return self
           
    def draw(self):
        self._update()
        self._draw()

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
    def _update_just_me(self):
        self._solve_global_span()
       
    # to override 
    def _draw_just_me(self):
        pass
    
    def _update(self):
        self._update_just_me()
        for child in self._childs:
            child._update()
            
    def _draw(self):
        self._draw_just_me()
        for child in self._childs:
            child._draw()
            



            
        