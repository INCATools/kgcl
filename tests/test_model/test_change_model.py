"""Test change model."""
import os
import unittest

from linkml_runtime.dumpers import JSONDumper

from kgcl_schema.datamodel.kgcl import NewSynonym, PredicateChange
from kgcl_schema.datamodel.ontology_model import Edge

from tests.util import roundtrip

cwd = os.path.abspath(os.path.dirname(__file__))
EXAMPLE_DIR = os.path.join(cwd, "../../examples")
OUTPUT_DIR = os.path.join(cwd, "../outputs")


class ChangeModelTestSuite(unittest.TestCase):
    """Test change in model."""

    def test_create(self):
        """Test create."""
        c = NewSynonym(id="chg12345", about_node="ANAT:HindLimb", new_value="hindlimb")
        self.assertEqual(c, roundtrip(c))
        c = PredicateChange(
            id="chg4",
            about_edge=Edge(subject="ANAT:Hand", object="ANAT:Forelimb"),
            new_value="BFO:000005",
        )
        self.assertEqual(c, roundtrip(c))
