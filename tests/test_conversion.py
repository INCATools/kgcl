"""Test conversion."""
import os
import unittest

from rdflib import Graph

from kgcl.utils import from_yaml, to_json, to_jsonld, to_rdf

# from test import EXAMPLE_DIR
cwd = os.path.abspath(os.path.dirname(__file__))
EXAMPLE_DIR = os.path.join(cwd, "../examples")
OUTPUT_DIR = os.path.join(cwd, "outputs")


class ConversionTestSuite(unittest.TestCase):
    """Reads examples from root /examples/ folder, converts them to json and rdf."""

    def setUp(self) -> None:
        """Set up tests."""
        self.session = from_yaml(f"{EXAMPLE_DIR}/de-novo.yaml")

    def test_convert(self):
        """Test convert."""
        session = from_yaml(f"{EXAMPLE_DIR}/de-novo.yaml")
        print(f"Session: {session}")
        json = to_json(session)
        ofn = os.path.join(OUTPUT_DIR, "test.json")
        with open(ofn, "w") as stream:
            stream.write(json)
        with open(os.path.join(OUTPUT_DIR, "test.jsonld"), "w") as stream:
            stream.write(to_jsonld(session))
        g: Graph
        g = to_rdf(session)
        g.serialize(os.path.join(OUTPUT_DIR, "test.rdf"), format="turtle")
