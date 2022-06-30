"""Test change model."""
import os
import unittest

from linkml_runtime.dumpers import JSONDumper

from kgcl.model.kgcl import NewSynonym, PredicateChange
from kgcl.model.ontology_model import Edge

cwd = os.path.abspath(os.path.dirname(__file__))
EXAMPLE_DIR = os.path.join(cwd, "../examples")
OUTPUT_DIR = os.path.join(cwd, "outputs")


class ChangeModelTestSuite(unittest.TestCase):
    """Test change in model."""

    def test_create(self):
        """Test create."""
        c = NewSynonym(id="chg12345", about_node="ANAT:HindLimb", new_value="hindlimb")
        print(c)
        d = JSONDumper()
        print(d.dumps(c))

    def test_predicate_change(self):
        """Test predicate change."""
        c = PredicateChange(
            id="chg4",
            about_edge=Edge(subject="ANAT:Hand", object="ANAT:Forelimb"),
            new_value="BFO:000005",
        )
        print(c)
        d = JSONDumper()
        print(d.dumps(c))
