"""Test conversion."""
import logging
import os
import unittest
from collections import defaultdict
from typing import List, Dict

from kgcl.datamodel.kgcl import SetLanguageForName
from linkml_runtime.linkml_model import ClassDefinitionName
from linkml_runtime.utils.yamlutils import YAMLRoot
from rdflib import Graph

from kgcl.utils import from_yaml, to_json, to_jsonld, to_rdf

# from test import EXAMPLE_DIR
from tests.util import roundtrip

cwd = os.path.abspath(os.path.dirname(__file__))
EXAMPLE_DIR = os.path.join(cwd, "../../examples")
OUTPUT_DIR = os.path.join(cwd, "../outputs")


def group_by_type(objs: List[YAMLRoot]) -> Dict[ClassDefinitionName, List[YAMLRoot]]:
    d = defaultdict(list)
    for obj in objs:
        cn = type(obj).class_name
        d[cn].append(obj)
    return d


class ConversionTestSuite(unittest.TestCase):
    """Reads examples from root /examples/ folder, converts them to json and rdf."""

    def setUp(self) -> None:
        """Set up tests."""
        self.session = from_yaml(f"{EXAMPLE_DIR}/de-novo.yaml")

    def test_convert(self):
        """Test convert."""
        session = from_yaml(f"{EXAMPLE_DIR}/de-novo.yaml")
        logging.info(f"Session: {session}")
        self.assertEqual(9, len(session.change_set))
        self.assertEqual(2, len(session.activity_set))
        tmap = group_by_type(session.change_set)
        ch = tmap['set language for name'][0]
        if isinstance(ch, SetLanguageForName):
            self.assertEqual('en', ch.new_value)
        else:
            raise ValueError(f"Unexpected type for {ch}")
        json = to_json(session)
        logging.info(f"Session: {json}")
        print(json)
        ofn = os.path.join(OUTPUT_DIR, "test.json")
        with open(ofn, "w") as stream:
            stream.write(json)
        with open(os.path.join(OUTPUT_DIR, "test.jsonld"), "w") as stream:
            stream.write(to_jsonld(session))
        with open(os.path.join(OUTPUT_DIR, "test.rdf"), "w") as stream:
            stream.write(to_rdf(session, {'uuid': 'http://example.org/uuid/'}))

