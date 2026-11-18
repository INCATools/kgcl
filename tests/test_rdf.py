"""Tests for RDF (Turtle) export. See issue #115."""

import os
import unittest

from click.testing import CliRunner
from rdflib import RDF, Graph, Literal, URIRef

import kgcl_schema.grammar.parser as kgcl_parser
from kgcl_schema.datamodel.kgcl import Session
from kgcl_schema.grammar.parser import parse_statement
from kgcl_schema.utils import KGCL_BASE, from_dict, to_rdf
from tests import OUTPUT_DIR
from tests.cases import CASES, TODO_TOKEN

KGCL = KGCL_BASE
TMP_RDF = os.path.join(OUTPUT_DIR, "test.rdf")
NUCLEUS_URI = URIRef("http://purl.obolibrary.org/obo/GO_0005634")


def _graph(ttl: str) -> Graph:
    g = Graph()
    g.parse(data=ttl, format="turtle")
    return g


def _changes(g: Graph):
    session = next(g.subjects(RDF.type, URIRef(KGCL + "Session")))
    return list(g.objects(session, URIRef(KGCL + "change_set")))


class TestRdf(unittest.TestCase):
    def test_all_cases(self):
        """Every parseable test case exports to RDF that parses back."""
        for command_curie, command_uri, obj, _ in CASES:
            for command in (command_curie, command_uri):
                if command is None or command == TODO_TOKEN:
                    continue
                with self.subTest(command=command):
                    change = parse_statement(command)
                    g = _graph(to_rdf(Session(change_set=[change])))
                    [node] = _changes(g)
                    expected = URIRef(KGCL + type(obj).__name__)
                    self.assertIn(expected, list(g.objects(node, RDF.type)))
                    for o in g.objects(node, RDF.type):
                        self.assertNotIsInstance(o, Literal)

    def test_obsoletion(self):
        ttl = to_rdf(Session(change_set=[parse_statement("obsolete GO:0005634")]))
        self.assertNotIn("@base", ttl)
        g = _graph(ttl)
        [node] = _changes(g)
        self.assertEqual(
            [URIRef(KGCL + "NodeObsoletion")], list(g.objects(node, RDF.type))
        )
        self.assertEqual(
            [NUCLEUS_URI], list(g.objects(node, URIRef(KGCL + "about_node")))
        )

    def test_label_node(self):
        """A node given by label is written as a literal, not an IRI."""
        change = parse_statement("obsolete 'nuclear envelope'")
        g = _graph(to_rdf(Session(change_set=[change])))
        [node] = _changes(g)
        self.assertEqual(
            [Literal("nuclear envelope")],
            list(g.objects(node, URIRef(KGCL + "about_node"))),
        )

    def test_caller_base(self):
        """A caller's @base applies to change IDs, not to labels."""
        change = parse_statement("obsolete 'nuclear envelope'")
        change.id = "change_1"
        g = _graph(
            to_rdf(
                Session(change_set=[change]),
                prefix_map={"@base": "http://example.org/changes/"},
            )
        )
        [node] = _changes(g)
        self.assertEqual(URIRef("http://example.org/changes/change_1"), node)
        self.assertEqual(
            [Literal("nuclear envelope")],
            list(g.objects(node, URIRef(KGCL + "about_node"))),
        )

    def test_from_dict_session(self):
        """Sessions loaded from YAML/JSON get uuid: change IDs."""
        session = from_dict(
            {"change_set": [{"type": "NodeObsoletion", "about_node": "GO:0005634"}]}
        )
        g = _graph(to_rdf(session))
        [node] = _changes(g)
        self.assertTrue(str(node).startswith("https://example.org/uuid/"))
        self.assertEqual(
            [NUCLEUS_URI], list(g.objects(node, URIRef(KGCL + "about_node")))
        )

    def test_prefix_map_overrides_default(self):
        change = parse_statement("obsolete GO:0005634")
        g = _graph(
            to_rdf(
                Session(change_set=[change]),
                prefix_map={"GO": "http://example.org/go/"},
            )
        )
        [node] = _changes(g)
        self.assertEqual(
            [URIRef("http://example.org/go/0005634")],
            list(g.objects(node, URIRef(KGCL + "about_node"))),
        )

    def test_cli(self):
        result = CliRunner().invoke(
            kgcl_parser.cli,
            [
                "-O",
                "rdf",
                "-o",
                TMP_RDF,
                "obsolete GO:0005634",
                "create synonym 'foo' for GO:0005634",
            ],
        )
        self.assertEqual(0, result.exit_code, result.output)
        g = Graph()
        g.parse(TMP_RDF, format="turtle")
        self.assertEqual(2, len(_changes(g)))
