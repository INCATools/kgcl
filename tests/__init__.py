import os
import pprint
import sys
from os.path import dirname, join

EXAMPLE_DIR = os.path.join(os.path.abspath(os.path.dirname(__file__)), "..", "examples")
RESOURCE_DIR = os.path.join(os.path.abspath(os.path.dirname(__file__)), "resources")
TARGET_DIR = os.path.join(os.path.abspath(os.path.dirname(__file__)), "target")

sys.path.append(join(dirname(dirname(__file__)), "src/"))
