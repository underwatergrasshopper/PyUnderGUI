# Set of tools for testing.
import sys
import os
import re

# Makes root package visible in tests.
SRC_PATH = re.sub(r"tests$", "src", os.getcwd())
sys.path.insert(0, SRC_PATH)

__all__ = ['TestManager', 'run_test']

class TestManager:
    """
    :ivar list(function())                         _tests:
    """
    def __init__(self):
        self._tests = [] 
    
    def add_test(self, test):
        """
        :param function()                          test:
        """
        self._tests += [test]
        
    def add_tests(self, tests):
        """
        :param list(function())                    test:
        """
        self._tests += tests

    def run_all_tests(self):
        for test in self._tests:
            run_test(test)


def run_test(test):
    """
    :param function()                          test:
    """
    print("runing %s" % test.__name__)
    test()
    print("done   %s" % test.__name__)