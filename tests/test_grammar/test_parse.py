import unittest

from kgcl_schema.grammar.parser import parse_statement
from kgcl_schema.schema import get_schemaview
from linkml_runtime.dumpers import yaml_dumper, json_dumper
from linkml_runtime.utils.inference_utils import infer_slot_value, infer_all_slot_values

from dataclasses import fields, is_dataclass

from lark import Token

from tests.cases import CASES


def _token_or_quoted_values(obj, path=""):
    """Yield (path, value) for any value that is a lark Token or keeps its quotes."""
    for f in fields(obj):
        value = getattr(obj, f.name)
        if is_dataclass(value):
            yield from _token_or_quoted_values(value, f"{path}{f.name}.")
        elif isinstance(value, Token) or (
            isinstance(value, str) and value[:1] in ("'", '"')
        ):
            yield f"{path}{f.name}", value


class ParserTestSuite(unittest.TestCase):
    def setUp(self) -> None:
        self.schemaview = get_schemaview()

    def test_parse(self):
        """Test parsing KGCL DSL into objects."""
        for txt, _, obj, _ in CASES:
            # print(txt)
            change = parse_statement(txt)
            change.id = obj.id
            change_json = json_dumper.dumps(change)
            obj_json = json_dumper.dumps(obj)
            # print(f"{change_json} == {obj_json}")
            self.assertEqual(change_json, obj_json)

    def test_parse_returns_clean_values(self):
        """Parsed objects hold plain strings, not lark Tokens or quoted text."""
        for txt, _, _, _ in CASES:
            with self.subTest(txt=txt):
                change = parse_statement(txt)
                self.assertEqual(list(_token_or_quoted_values(change)), [])
            # infer_slot_value(change,
            #                 slot_name='change description',
            #                 schemaview=self.schemaview)
