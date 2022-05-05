from .Commons   import *
from .Window    import *

__all__ = ['Widget']

class Widget:
    def __init__(self, parent, area_or_range, anchor_group = None, window = None):
        """
        :param UnderGUI.Widget or None             parent:
        :param UnderGUI.Area or UnderGUI.Range     area_or_range:
        :param UnderGUI.AnchorGroup or None        anchor_group:
        :param UnderGUI.Window or None             window:
        """
        self._parent        = parent
        self._range         = area_or_range             if isinstance(area_or_range, Range) else area_or_range.to_range()
        self._anchor_group  = anchor_group              if anchor_group                     else AnchorGroup(AnchorAxisX.LEFT, AnchorAxisY.BOTTOM, AnchorAxisX.LEFT, AnchorAxisY.BOTTOM)
        self._window        = window                    if window or not self._parent       else self._parent._window


            
        