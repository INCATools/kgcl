"""Test ontology model."""
import os
import unittest

from kgcl.datamodel.ontology_model import ClassNode, OwlTypeEnum

from tests.util import roundtrip


class OntologyModelTestSuite(unittest.TestCase):
    """Test ontology model."""

    def test_create(self):
        """Test create."""
        c = ClassNode(id="X:1", owl_type=OwlTypeEnum.CLASS)
        c2 = roundtrip(c)
        self.assertEqual(c, c2)
