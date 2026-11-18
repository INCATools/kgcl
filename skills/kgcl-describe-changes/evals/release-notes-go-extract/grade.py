"""Check a run of the release-notes-go-extract test case.

Usage (needs kgcl-schema): python grade.py <directory with the run's output files> [grading.json]

Prints each check as PASS or FAIL; these are the same statements as in graders/. With a
second argument, also writes the results in the skill-creator grading.json format.
"""
import json
import re
import sys
from pathlib import Path

from kgcl_schema.grammar.parser import parse_statement
from kgcl_schema.grammar.render_operations import render
from kgcl_schema.utils import from_dict

BULLET = re.compile(r"^\s*[-*]\s+(.*)$")
KGCL_BLOCK = re.compile(r"^```kgcl\n(.*?)^```", re.MULTILINE | re.DOTALL)


def parses(cmd):
    try:
        return parse_statement(cmd)
    except Exception:
        return None


def read(p):
    return p.read_text(encoding="utf-8") if p.is_file() else ""


def norm(s):
    return re.sub(r"\s+", " ", s)


def grade_release(out: Path):
    notes = read(out / "release-notes.md")
    lines = [ln.strip() for b in KGCL_BLOCK.findall(notes) for ln in b.splitlines() if ln.strip()]
    bad = [ln for ln in lines if parses(ln) is None]
    s = set(lines)
    return [
        ("release-notes.md has KGCL commands in ```kgcl blocks and every one parses", bool(lines) and not bad, f"{len(lines)} commands; bad: {bad}"),
        ("Records the obsoletion as: obsolete GO:9999999 with replacement GO:0005634", "obsolete GO:9999999 with replacement GO:0005634" in s, ""),
        ("Records the hierarchy change as one command: deepen GO:0031965 from GO:0016020 to GO:0031090", "deepen GO:0031965 from GO:0016020 to GO:0031090" in s, ""),
        ("Does not list the delete/create edge pair for GO:0031965 as separate commands",
         "delete edge GO:0031965 rdfs:subClassOf GO:0016020" not in s, ""),
        ("Folds the 'obsolete cell nucleus' label change into the obsoletion (no separate rename command)",
         not any(ln.startswith("rename GO:9999999") for ln in lines), ""),
        ("Synonym recorded with its exact scope: create exact synonym 'cell nucleus' for GO:0005634",
         "create exact synonym 'cell nucleus' for GO:0005634" in s, ""),
        ("Definition recorded with its source: add definition 'A membrane-bounded organelle.' to GO:0005634 with xrefs GOC:go_curators",
         "add definition 'A membrane-bounded organelle.' to GO:0005634 with xrefs GOC:go_curators" in s, ""),
        ("New parent recorded: create edge GO:0005634 rdfs:subClassOf GO:0043231",
         "create edge GO:0005634 rdfs:subClassOf GO:0043231" in s, ""),
    ]


if __name__ == "__main__":
    results = grade_release(Path(sys.argv[1]))
    exp = [{"text": t, "passed": bool(p), "evidence": e} for t, p, e in results]
    n = sum(x["passed"] for x in exp)
    for x in exp:
        print(("PASS  " if x["passed"] else "FAIL  ") + x["text"])
    print(f"\n{n} of {len(exp)} checks passed.")
    if len(sys.argv) > 2:
        summary = {"passed": n, "failed": len(exp) - n, "total": len(exp), "pass_rate": round(n / len(exp), 2)}
        with open(sys.argv[2], "w") as f:
            json.dump({"expectations": exp, "summary": summary}, f, indent=2)
    sys.exit(0 if n == len(exp) else 1)
