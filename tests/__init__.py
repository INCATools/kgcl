import os
import pprint
import sys
from os.path import dirname, join

INPUT_DIR = os.path.join(os.path.abspath(os.path.dirname(__file__)), "input")
OUTPUT_DIR = os.path.join(os.path.abspath(os.path.dirname(__file__)), "outputs")
EXAMPLE_DIR = os.path.join(os.path.abspath(os.path.dirname(__file__)), "..", "examples")
RESOURCE_DIR = os.path.join(os.path.abspath(os.path.dirname(__file__)), "resources")
TARGET_DIR = os.path.join(os.path.abspath(os.path.dirname(__file__)), "target")

sys.path.append(join(dirname(dirname(__file__)), "src/"))

INPUT = os.path.join(INPUT_DIR, 'go-nucleus.owl.ttl')
TMP_OUTPUT = os.path.join(OUTPUT_DIR, 'go-nucleus-modified.owl.ttl')
TMP_YAML = os.path.join(OUTPUT_DIR, 'tmp.yaml')
DIFF_OUTPUT = os.path.join(OUTPUT_DIR, 'diff.kgcl')
DIFF_OUTPUT_DIR = os.path.join(OUTPUT_DIR, 'diff-info')

