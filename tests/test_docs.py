"""Check that the KGCL examples in the documentation are valid."""
import re
import unittest
from pathlib import Path

from kgcl_schema.grammar.parser import parse_statement
from kgcl_schema.grammar.render_operations import render

DOCS_DIR = Path(__file__).resolve().parents[1] / "src" / "docs"
KGCL_BLOCK = re.compile(r"^```kgcl\n(.*?)^```", re.MULTILINE | re.DOTALL)


def kgcl_commands():
    """Yield (file name, command) for every line in a ```kgcl block in the docs."""
    for md_file in sorted(DOCS_DIR.glob("*.md")):
        for block in KGCL_BLOCK.findall(md_file.read_text()):
            for line in block.splitlines():
                if line.strip():
                    yield md_file.name, line.strip()


class DocsTestSuite(unittest.TestCase):
    def test_docs_have_kgcl_examples(self):
        self.assertGreater(len(list(kgcl_commands())), 10)

    def test_kgcl_examples_parse_and_round_trip(self):
        for md_name, command in kgcl_commands():
            with self.subTest(file=md_name, command=command):
                change = parse_statement(command)
                self.assertEqual(command, render(change))
