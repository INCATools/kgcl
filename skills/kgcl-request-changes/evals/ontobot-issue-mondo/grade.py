"""Check a run of the ontobot-issue-mondo test case.

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


def grade_ontobot(out: Path):
    issue = read(out / "issue.md")
    bullets = [m.group(1).strip() for line in issue.splitlines() if (m := BULLET.match(line))]
    parsed = [(b, parses(b)) for b in bullets]
    bad = [b for b, c in parsed if c is None]
    cmds = {render(c) for _, c in parsed if c is not None}
    others = read(out / "summary.md") + issue
    return [
        ("issue.md contains the Ontobot trigger phrase 'Hey ontobot'", "hey ontobot" in issue.lower(), f"{len(issue)} chars"),
        ("Every bulleted line in issue.md parses as a KGCL command (Ontobot runs every bullet)", bool(bullets) and not bad, f"unparseable bullets: {bad}"),
        ("Adds exact synonym: create exact synonym 'cortical visual impairment' for MONDO:0001385",
         "create exact synonym 'cortical visual impairment' for MONDO:0001385" in cmds, str(sorted(cmds))),
        ("Adds related synonym: create related synonym 'CVI' for MONDO:0001385",
         "create related synonym 'CVI' for MONDO:0001385" in cmds, ""),
        ("Retires the duplicate: obsolete MONDO:0700001 with replacement MONDO:0700002",
         "obsolete MONDO:0700001 with replacement MONDO:0700002" in cmds, ""),
        ("The Parkinson's rename is flagged as not expressible as a KGCL command (apostrophe), not silently dropped or mangled",
         bool(re.search(r"apostrophe", others, re.I)) and not any("Parkinson" in b and c is not None and "s disease" in render(c) for b, c in parsed),
         "searched issue.md for 'apostrophe'"),
        ("No IRIs in angle brackets in issue.md (Ontobot strips < and >)", not re.search(r"<https?://", issue), ""),
    ]


if __name__ == "__main__":
    results = grade_ontobot(Path(sys.argv[1]))
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
