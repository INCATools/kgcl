import os
import unittest

import rdflib
from kgcl_schema.apply import graph_transformer
from kgcl_schema.grammar import parser
from kgcl_schema.kgcl_diff import diff
from rdflib.util import guess_format

from tests import INPUT
from tests.cases import NUCLEUS, NUCLEUS_URI, NEW_TERM_URI, CASES


EXPECTED = [
    (f"create exact synonym 'foo' for {NUCLEUS}",
     f"create exact synonym 'foo' for {NUCLEUS_URI}"),

    (f"create exact synonym 'foo' for {NUCLEUS_URI}",
     f"create exact synonym 'foo' for {NUCLEUS_URI}"),

    (f"create narrow synonym 'foo' for {NUCLEUS}",
     f"create narrow synonym 'foo' for {NUCLEUS_URI}"),

    ("delete edge GO:0005634 rdfs:subClassOf GO:0043231",
     "delete edge <http://purl.obolibrary.org/obo/GO_0005634> <http://www.w3.org/2000/01/rdf-schema#subClassOf> <http://purl.obolibrary.org/obo/GO_0043231>"),

    (f"create {NEW_TERM_URI}",
     f"create {NEW_TERM_URI}"),

    #(f"change relationship between {NUCLEAR_ENVELOPE} and {NUCLEUS} from {PART_OF} to {IS_A}",
    # f"change relationship between {NUCLEAR_ENVELOPE} and {NUCLEUS} from {PART_OF} to {IS_A}"),

    #("obsolete GO:0005634",
    #"create exact synonym 'foo' for <http://purl.obolibrary.org/obo/GO_0005634>"),
]


class ParserTestSuite(unittest.TestCase):

    def setUp(self) -> None:
        g = rdflib.Graph()
        g.parse(INPUT, format=guess_format(INPUT))
        self.graph = g

    def test_diff(self):
        """Test roundtripping."""
        g = self.graph
        for patch, expected_diff in EXPECTED:
            g_modified = rdflib.Graph()
            for t in g:
                g_modified.add(t)
            change = parser.parse(patch)
            graph_transformer.apply_patch(change, g_modified)
            changes = diff(g, g_modified)
            for change in changes:
                print(f"{type(change)} : {change}")
            if isinstance(expected_diff, list):
                self.assertCountEqual(expected_diff, changes)
            else:
                self.assertEqual(1, len(changes))
                self.assertEqual(changes[0], expected_diff)

    def test_cases(self):
        """Test round-tripping."""
        g = self.graph
        for patch, expected_diff, _, _ in CASES:
            print(f"PATCH={patch}; EXPECTED={expected_diff}")
            g_modified = rdflib.Graph()
            for t in g:
                g_modified.add(t)
            change = parser.parse(patch)
            graph_transformer.apply_patch(change, g_modified)
            changes = diff(g, g_modified)
            print(f"Num changes = {len(changes)}")
            #for change in changes:
            #    print(f"{type(change)} : {change}")
            if expected_diff is None:
                self.assertGreater(len(changes), 0)
                print(f"TODO: {changes}")
            elif isinstance(expected_diff, list):
                self.assertCountEqual(expected_diff, changes)
            elif expected_diff == 'TODO':
                pass
            else:
                self.assertEqual(1, len(changes))
                self.assertEqual(changes[0], expected_diff)

