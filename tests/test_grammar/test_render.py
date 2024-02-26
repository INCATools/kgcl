import unittest

from kgcl.grammar.render_operations import render
from kgcl.grammar.parser import parse_statement

from tests.cases import CASES


def _first_word(command: str) -> str:
    return str.split(" ")[0]


class RenderTestSuite(unittest.TestCase):
    def test_render(self):
        """Test parsing KGCL DSL into objects."""
        for patch, _, _, _ in CASES:
            change = parse_statement(patch)
            print(patch)
            patch_roundtripped = render(change)
            print(f"{patch == patch_roundtripped}: {patch} ==> {patch_roundtripped}")
            # TODO:
            # - render does not currently accept CURIEs; it will place <>s around curies
            # - label tokens in rename broken
            self.assertEqual(patch, patch_roundtripped)
            # for now, we implement this much weaker test:
            # self.assertEqual(_first_word(patch), _first_word(patch_roundtripped))
