import unittest
from click.testing import CliRunner
from pytest import Session
from kgcl_schema.datamodel.kgcl import (
    NodeObsoletionWithDirectReplacement,
    NodeRename,
    NodeObsoletion,
    NewSynonym,
    ClassCreation,
    PredicateChange,
    Change,
    NodeCreation,
    EdgeCreation,
    PlaceUnder,
    RemoveUnder,
    EdgeDeletion,
    NodeDeepening,
)
import kgcl_schema.grammar.parser as kgcl_parser
from kgcl_schema.utils import from_yaml
from tests import TMP_YAML
from tests.cases import CASES
from linkml_runtime.dumpers import yaml_dumper
import yaml
from kgcl_schema.grammar.parser import parse_statement
from pathlib import Path

PROJ_DIR = Path(__file__).resolve().parents[1]
SRC_DIR = PROJ_DIR / "src"
MD_OUT_FN = "examples.md"
YAML_OUT_FN = "examples.yaml"
YAML_OUT_PATH = SRC_DIR / "data/examples" / YAML_OUT_FN
MD_OUT_PATH = SRC_DIR / "docs" / MD_OUT_FN
W3ID = "https://w3id.org/kgcl/"
# Sections of the examples page, in display order. Each change type in
# tests/cases.py must appear in exactly one section, with a short description.
SECTIONS = {
    "Labels": {
        "NodeRename": "Rename a node (replace its label).",
        "NewLabel": "Add a label to an unlabeled node.",
    },
    "Synonyms": {
        "NewSynonym": "Add a synonym.",
        "RemoveSynonym": "Remove a synonym.",
        "SynonymReplacement": "Replace the text of a synonym.",
    },
    "Definitions": {
        "NewTextDefinition": "Add a definition.",
        "NodeTextDefinitionChange": "Change a definition.",
        "RemoveTextDefinition": "Remove a definition.",
    },
    "Relationships (edges)": {
        "EdgeCreation": "Create an edge.",
        "PlaceUnder": "Place a node under another node (create an is_a edge).",
        "EdgeDeletion": "Delete an edge.",
        "RemoveUnder": "Remove a node from under another node (delete an is_a edge).",
        "PredicateChange": "Change the predicate (relationship type) of an edge.",
        "NodeDeepening": "Move a node under a more specific parent.",
        "NodeShallowing": "Move a node under a more general parent.",
    },
    "Obsoletion": {
        "NodeObsoletion": "Obsolete a node.",
        "NodeObsoletionWithDirectReplacement": "Obsolete a node and name its replacement.",
    },
    "Subsets": {
        "AddNodeToSubset": "Add a node to a subset.",
        "RemoveNodeFromSubset": "Remove a node from a subset.",
    },
    "Creating nodes": {
        "ClassCreation": "Create a class.",
        "NodeCreation": "Create a node with a label.",
    },
}
CLASS_DESCRIPTION = {
    cls: desc for section in SECTIONS.values() for cls, desc in section.items()
}
MD_INTRO = """# Command examples

One example of each change type, written as a KGCL command and as YAML. The
examples are generated from the test suite (`tests/cases.py`), so every command on
this page is known to parse. For before-and-after diagrams of the most common
changes, see the [visual guide to change types](change-types.md).

"""


def export_yaml_and_md():
    yaml_dict = {}
    examples = {}  # change type name -> markdown block, first example only
    # Dump YAML file with test information.
    for idx, (command_curie, command_uri, obj, _) in enumerate(CASES):
        type_name = type(obj).__name__
        yaml_dict[f"Test_{idx}"] = obj.__dict__.copy()
        yaml_dict[f"Test_{idx}"]["type"] = type_name
        yaml_dict[f"Test_{idx}"]["command_with_curie"] = command_curie
        yaml_dict[f"Test_{idx}"]["command_with_uri"] = command_uri

        if type_name not in examples:
            yaml_block = yaml_dumper.dumps(obj).replace("'", "")
            examples[type_name] = (
                f"### {CLASS_DESCRIPTION[type_name].rstrip('.')}\n\n"
                f"Class: [`{type_name}`]({W3ID}{type_name})\n\n"
                f"```kgcl\n{command_curie}\n```\n\n"
                f"```yaml\n{yaml_block}```\n\n"
            )

    md = MD_INTRO
    for section, classes in SECTIONS.items():
        blocks = [examples[c] for c in classes if c in examples]
        if blocks:
            md += f"## {section}\n\n" + "".join(blocks)

    yaml_dumper.dump(yaml_dict, YAML_OUT_PATH)
    with open(MD_OUT_PATH, "w") as md_dump:
        md_dump.write(md.rstrip() + "\n")


class TestCases(unittest.TestCase):
    def setUp(self) -> None:
        runner = CliRunner()
        self.runner = runner
        export_yaml_and_md()

    def test_case_yaml_dumper(self):
        self.assertTrue(YAML_OUT_PATH.is_file())

    def test_case_md_dumper(self):
        self.assertTrue(MD_OUT_PATH.is_file())

    def test_run_using_yaml_load(self):
        with open(YAML_OUT_PATH, "r") as y:
            test_cases = yaml.safe_load(y)

        patches = []

        for key in test_cases:
            patches.append(test_cases[key]["command_with_curie"])

        result = self.runner.invoke(kgcl_parser.cli, patches + ["-o", TMP_YAML])
        session: Session = from_yaml(TMP_YAML)
        self.assertEqual(len(patches), len(session.change_set))
        out = result.stdout
        self.assertEqual(0, result.exit_code)
