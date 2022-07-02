"""Test rename."""
from kgcl.grammar.parser import parse_statement
from linkml_runtime.dumpers import yaml_dumper

from tests.util import run_test


def test_parse():
    """Test parsing KGCL DSL into objects."""
    change = parse_statement("rename 'Bacteria' to 'Virus'")
    print()
    print(change)
    print(yaml_dumper.dumps(change))