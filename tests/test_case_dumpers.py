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

def export_yaml_and_md():
    yaml_dict = {}
    used_type = {}
    md = "# KGCL Commands.\n\n"
    # Dump YAML file with test information.
    for idx, (command_curie, command_uri, obj, _) in enumerate(CASES):            
        yaml_dict[f"Test_{idx}"] = obj.__dict__.copy()
        yaml_dict[f"Test_{idx}"]["type"] = type(obj).__name__
        yaml_dict[f"Test_{idx}"]["command_with_curie"] = command_curie
        yaml_dict[f"Test_{idx}"]["command_with_uri"] = command_uri

        if type(obj).__name__ not in used_type:
            used_type[type(obj).__name__] = 1
            md += f"## `{type(obj).__name__}`:\n"
            md += f"\tCommand using CURIEs: `{command_curie}`\n"
            if command_uri and command_uri != "TODO":
                md += f"\tCommand using URIs: `{command_uri}`\n\n"
            else:
                md += "\n"

        yaml_dumper.dump(yaml_dict, YAML_OUT_PATH)
        with open(MD_OUT_PATH, "w") as md_dump:
            md_dump.write(md)
class TestCases(unittest.TestCase):
    def setUp(self) -> None:
        runner = CliRunner(mix_stderr=False)
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
