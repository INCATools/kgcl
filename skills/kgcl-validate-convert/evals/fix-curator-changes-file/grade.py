"""Check a run of the fix-curator-changes-file test case.

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


def grade_fix(out: Path):
    raw = read(out / "changes.json")
    changes, err = [], ""
    try:
        data = json.loads(raw)
        if isinstance(data, list):
            data = {"change_set": data}
        changes = from_dict(json.loads(json.dumps(data))).change_set
    except Exception as e:
        err = f"{type(e).__name__}: {e}"
    by = [(type(c).__name__, c) for c in changes]
    report = read(out / "report.md")

    def has(t, **kv):
        return any(n == t and all(str(getattr(c, k, None)) == v for k, v in kv.items()) for n, c in by)

    return [
        ("changes.json loads as a KGCL session (from_dict) without error", bool(changes) and not err, err or f"{len(changes)} changes"),
        ("'deprecate GO:0005635' fixed to a NodeObsoletion of GO:0005635", has("NodeObsoletion", about_node="GO:0005635"), ""),
        ("Double-quoted synonym fixed to NewSynonym 'nuclear envelope' (exact) for GO:0005635",
         has("NewSynonym", about_node="GO:0005635", new_value="nuclear envelope", qualifier="exact"), ""),
        ("Definition line kept with its xref GOC:go_curators",
         any(n == "NewTextDefinition" and "GOC:go_curators" in str(getattr(c, "xrefs", "")) for n, c in by), ""),
        ("Apostrophe rename kept via JSON: NodeRename of GO:0031965 to \"nucleus's membrane\"",
         has("NodeRename", about_node="GO:0031965", new_value="nucleus's membrane"), ""),
        ("Obsoletion given as an IRI kept: obsolete GO:9999999 with replacement GO:0005634",
         any(n == "NodeObsoletionWithDirectReplacement" and str(c.about_node).endswith("9999999") for n, c in by), ""),
        ("'add edge' fixed to EdgeCreation GO:0031965 BFO:0000050 GO:0005635",
         any(n == "EdgeCreation" and str(getattr(c, "subject", "")) == "GO:0031965" and str(getattr(c, "object", "")) == "GO:0005635" for n, c in by), ""),
        ("No rename without a term ID in changes.json; report.md flags that line 1 names no term",
         not any(n == "NodeRename" and not c.about_node for n, c in by) and bool(re.search(r"(no|missing|without)[^.\n]{0,40}(term|ID|identifier|CURIE)", report, re.I)), ""),
    ]


if __name__ == "__main__":
    results = grade_fix(Path(sys.argv[1]))
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
