from TestKit        import TestManager

from test_commons   import *
from test_color     import *
from test_utility   import *

if __name__ == "__main__":
    test_manager = TestManager()
    
    test_manager.add_tests([
        test_commons,
        test_color,
        test_utility
    ])
    
    test_manager.run_all_tests()