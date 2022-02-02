__all__ = ['Drawer']

class Drawer:
    """
    Draws to window client area.
    """
    
    # to override
    def fill_view(self, color):
        """
        Fills window client area with color.
        
        :param                                     color:
        :type                                      color: 
            UnderGUI.ColorF or UnderGUI.ColorI or UnderGUI.ColorB
        """
        pass
