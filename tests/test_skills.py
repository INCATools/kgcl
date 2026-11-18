"""Check the Agent Skills in skills/: KGCL examples parse, metadata is valid,
and the files shared between skills stay identical."""

import re
import subprocess
import sys
import unittest
from pathlib import Path

import yaml

from kgcl_schema.grammar.parser import parse_statement
from kgcl_schema.grammar.render_operations import render

SKILLS_DIR = Path(__file__).resolve().parents[1] / "skills"
SKILL_DIRS = sorted(p.parent for p in SKILLS_DIR.glob("*/SKILL.md"))
KGCL_BLOCK = re.compile(r"^```kgcl\n(.*?)^```", re.MULTILINE | re.DOTALL)
FRONTMATTER = re.compile(r"\A---\n(.*?)\n---\n", re.DOTALL)
# Files every skill carries its own copy of, so each works when installed alone
SHARED_FILES = ["references/kgcl-commands.md", "scripts/check_kgcl.py"]


def kgcl_commands():
    """Yield (file, command) for every line in a ```kgcl block in the skills."""
    for md_file in sorted(SKILLS_DIR.glob("**/*.md")):
        for block in KGCL_BLOCK.findall(md_file.read_text(encoding="utf-8")):
            for line in block.splitlines():
                if line.strip():
                    yield md_file.relative_to(SKILLS_DIR), line.strip()


class SkillsTestSuite(unittest.TestCase):
    def test_skills_exist(self):
        self.assertGreaterEqual(len(SKILL_DIRS), 3)
        self.assertGreater(len(list(kgcl_commands())), 10)

    def test_kgcl_examples_parse_and_round_trip(self):
        for path, command in kgcl_commands():
            with self.subTest(file=str(path), command=command):
                self.assertEqual(command, render(parse_statement(command)))

    def test_frontmatter(self):
        for skill in SKILL_DIRS:
            with self.subTest(skill=skill.name):
                text = (skill / "SKILL.md").read_text(encoding="utf-8")
                match = FRONTMATTER.match(text)
                self.assertIsNotNone(match, "SKILL.md must start with YAML frontmatter")
                meta = yaml.safe_load(match.group(1))
                self.assertEqual(skill.name, meta["name"])
                self.assertRegex(meta["name"], r"^[a-z0-9]+(-[a-z0-9]+)*$")
                self.assertLessEqual(len(meta["name"]), 64)
                self.assertTrue(meta["description"].strip())
                self.assertLessEqual(len(meta["description"]), 1024)

    def test_relative_links_resolve(self):
        for skill in SKILL_DIRS:
            text = (skill / "SKILL.md").read_text(encoding="utf-8")
            for target in re.findall(r"\]\(((?:references|scripts)/[^)#]+)", text):
                with self.subTest(skill=skill.name, link=target):
                    self.assertTrue((skill / target).is_file())

    def test_shared_files_identical(self):
        for name in SHARED_FILES:
            copies = {s.name: (s / name).read_text(encoding="utf-8") for s in SKILL_DIRS}
            with self.subTest(file=name):
                self.assertEqual(1, len(set(copies.values())), f"copies of {name} differ")

    def test_check_script(self):
        script = SKILL_DIRS[0] / "scripts" / "check_kgcl.py"
        issue = "Hey ontobot!, apply:\n\n- obsolete GO:0005634\n- create exact synonym 'x' for GO:0005634\n"
        ok = subprocess.run(
            [sys.executable, str(script), "-f", "-"], input=issue, capture_output=True, text=True
        )
        self.assertEqual(0, ok.returncode, ok.stdout + ok.stderr)
        self.assertIn("2 of 2 commands parsed", ok.stdout)
        # Read like Ontobot: prose ignored, every bullet is a command
        issue = "Why this is needed.\n\n" + issue + "\nThanks.\n\n* not a command\n"
        mixed = subprocess.run(
            [sys.executable, str(script), "-f", "-"], input=issue, capture_output=True, text=True
        )
        self.assertEqual(1, mixed.returncode)
        self.assertIn("2 of 3 commands parsed", mixed.stdout)
        bad = subprocess.run(
            [sys.executable, str(script), "add label 'Parkinson's disease' to MONDO:0005180"],
            capture_output=True,
            text=True,
        )
        self.assertEqual(1, bad.returncode)
        self.assertIn("apostrophe", bad.stdout)


    def test_check_script_markdown(self):
        script = SKILL_DIRS[0] / "scripts" / "check_kgcl.py"
        md = "# Notes\n\nSome prose.\n\n```kgcl\nobsolete GO:0005634\n```\n\n- a bullet\n\n```bash\nls\n```\n"
        run = subprocess.run(
            [sys.executable, str(script), "-f", "-"], input=md, capture_output=True, text=True
        )
        self.assertEqual(0, run.returncode, run.stdout)
        self.assertIn("1 of 1 commands parsed", run.stdout)

    def test_check_script_writes_yaml(self):
        import tempfile

        from kgcl_schema.utils import from_yaml

        script = SKILL_DIRS[0] / "scripts" / "check_kgcl.py"
        with tempfile.TemporaryDirectory() as tmp:
            out = Path(tmp) / "changes.yaml"
            run = subprocess.run(
                [sys.executable, str(script), "--yaml", str(out), "obsolete GO:0005634",
                 "create exact synonym 'x' for GO:0005634"],
                capture_output=True,
                text=True,
            )
            self.assertEqual(0, run.returncode, run.stdout + run.stderr)
            session = from_yaml(str(out))
            self.assertEqual(
                ["NodeObsoletion", "NewSynonym"], [type(c).__name__ for c in session.change_set]
            )


REFERENCE = SKILLS_DIR / "kgcl-request-changes" / "references" / "kgcl-commands.md"
# A reference table row: | `command` | `ChangeType` ... |
TABLE_ROW = re.compile(r"^\| `([^`]+)` \| `([A-Za-z]+)`", re.MULTILINE)


class ReferenceTestSuite(unittest.TestCase):
    def test_table_commands_have_stated_type(self):
        rows = TABLE_ROW.findall(REFERENCE.read_text(encoding="utf-8"))
        self.assertGreater(len(rows), 20)
        for command, change_type in rows:
            with self.subTest(command=command):
                self.assertEqual(change_type, type(parse_statement(command)).__name__)

    def test_every_change_type_is_covered(self):
        """Each concrete change class appears in a command table or in the
        no-command list, so agents don't invent syntax for it."""
        from kgcl_schema.schema import get_schemaview

        text = REFERENCE.read_text(encoding="utf-8")
        sv = get_schemaview()
        for cls in sv.class_descendants("Change"):
            c = sv.get_class(cls)
            if c.abstract or c.mixin:
                continue
            with self.subTest(change_type=cls):
                self.assertIn(f"`{cls}`", text)
