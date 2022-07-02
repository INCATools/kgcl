"""Test ontology model."""
import os
import unittest

from linkml_runtime.dumpers import JSONDumper

from kgcl.datamodel.ontology_model import ClassNode, OwlTypeEnum

cwd = os.path.abspath(os.path.dirname(__file__))
EXAMPLE_DIR = os.path.join(cwd, "../../examples")
OUTPUT_DIR = os.path.join(cwd, "../outputs")


class OntologyModelTestSuite(unittest.TestCase):
    """Test ontology model."""

    def test_create(self):
        """Test create."""
        c = ClassNode(id="X:1", owl_type=OwlTypeEnum.CLASS)
        print(c)
        d = JSONDumper()
        print(d.dumps(c))
