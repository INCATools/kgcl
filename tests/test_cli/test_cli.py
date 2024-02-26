import logging
import unittest

from click.testing import CliRunner

import kgcl.grammar.parser as kgcl_parser
from kgcl.datamodel.kgcl import Session
from kgcl.utils import from_yaml

from tests import TMP_YAML
from tests.cases import CASES, TODO_TOKEN, UID


class CliTestSuite(unittest.TestCase):
    """
    Tests command line interfaces
    """

    def setUp(self) -> None:
        runner = CliRunner(mix_stderr=False)
        self.runner = runner

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
        # for ch in session.change_set:
        #    ch.id = UID
        #    self.assertIn(ch, objs)
        out = result.stdout
        self.assertEqual(0, result.exit_code)
