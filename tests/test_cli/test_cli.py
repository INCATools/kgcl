import logging
import unittest

import rdflib
from click.testing import CliRunner

import kgcl_schema.kgcl as kgcl_apply
import kgcl_schema.kgcl_diff as kgcl_diff
import kgcl_schema.grammar.parser as kgcl_parser
from kgcl_schema.datamodel.kgcl import Session
from kgcl_schema.utils import from_yaml

from tests import INPUT, TMP_OUTPUT, DIFF_OUTPUT, DIFF_OUTPUT_DIR, TMP_YAML
from tests.cases import CASES, TODO_TOKEN, UID


class CliTestSuite(unittest.TestCase):
    """
    Tests command line interfaces
    """

    def setUp(self) -> None:
        runner = CliRunner(mix_stderr=False)
        self.runner = runner

    def test_apply_help(self):
        result = self.runner.invoke(kgcl_apply.cli, ["--help"])
        out = result.stdout
        self.assertIn("--graph", out)
        self.assertIn("PATCH", out)
        self.assertEqual(0, result.exit_code)

    def test_diff_help(self):
        result = self.runner.invoke(kgcl_diff.cli, ["--help"])
        out = result.stdout
        self.assertEqual(0, result.exit_code)

    def test_parse_help(self):
        result = self.runner.invoke(kgcl_parser.cli, ["--help"])
        out = result.stdout
        self.assertEqual(0, result.exit_code)

    def test_parse_multi(self):
        patches = [t[0] for t in CASES]
        objs = [t[2] for t in CASES]
        result = self.runner.invoke(kgcl_parser.cli, patches + ["-o", TMP_YAML])
        session: Session = from_yaml(TMP_YAML)
        self.assertEqual(len(patches), len(session.change_set))
        #for ch in session.change_set:
        #    ch.id = UID
        #    self.assertIn(ch, objs)
        out = result.stdout
        self.assertEqual(0, result.exit_code)

    def test_diff_to_empty(self):
        g = rdflib.Graph()
        g.serialize(destination=TMP_OUTPUT)
        diff_result = self.runner.invoke(
            kgcl_diff.cli, [INPUT, TMP_OUTPUT, '-o', DIFF_OUTPUT, '-d', DIFF_OUTPUT_DIR]
        )
        self.assertEqual(0, diff_result.exit_code)

    def test_cases(self):
        """Test CLI on each case."""
        for patch, expected_diff, _, _ in CASES:
            parse_result = self.runner.invoke(
                kgcl_parser.cli, ['-o', TMP_OUTPUT, patch]
            )
            #from_yaml
            self.assertEqual(0, parse_result.exit_code)
            apply_result = self.runner.invoke(
                kgcl_apply.cli, ['--graph', INPUT, '-o', TMP_OUTPUT, patch]
            )
            self.assertEqual(0, apply_result.exit_code)
            diff_result = self.runner.invoke(
                kgcl_diff.cli, [INPUT, TMP_OUTPUT, '-o', DIFF_OUTPUT, '-d', DIFF_OUTPUT_DIR]
            )
            self.assertEqual(0, diff_result.exit_code)
            changes = [line.strip() for line in (open(DIFF_OUTPUT).readlines())]
            if expected_diff is None:
                self.assertGreater(len(changes), 0)
                logging.warning(f"TODO: cases is under-specified here. Patch({patch}) ==> {changes}")
            elif isinstance(expected_diff, list):
                self.assertCountEqual(expected_diff, changes)
            elif expected_diff == TODO_TOKEN:
                pass
            else:
                self.assertEqual(1, len(changes))
                self.assertEqual(changes[0], expected_diff)


