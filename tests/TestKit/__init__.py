# Set of tools for testing.

import sys
import os
import re

# Adds package path to system paths.
SRC_PATH = re.sub(r"tests$", "src", os.getcwd())
sys.path.insert(0, SRC_PATH)



