"""Test ontology model."""
import os
import unittest

from kgcl_schema.schema import get_schemaview
from linkml_runtime.dumpers import JSONDumper


class IntrospectionTestSuite(unittest.TestCase):
    """Test introspection model."""

    def setUp(self) -> None:
        self.schemaview = get_schemaview()

    def test_introspect(self):
        """Test introspections."""
        sv = self.schemaview
        for c in ["EdgeChange", "NodeDeepening"]:
            self.assertIn(c, sv.all_classes())
        for s in ["about_node", "was_generated_by"]:
            self.assertIn(s, sv.all_slots())
