#!/usr/bin/env python3
"""Check KGCL commands line by line.

Reads commands from arguments, from files (-f), or from standard input, one
per line. Blank lines and lines starting with '#' are skipped, and a leading
Markdown bullet ("- " or "* ") is removed.

If the input contains Ontobot's trigger phrase ("Hey ontobot!, apply:"), it is
read the way Ontobot reads an issue body: every bulleted line anywhere in the
text is a command, and all other lines are ignored. Ontobot also deletes "<"
and ">" from the body, so IRIs in angle brackets are flagged.

Otherwise, if the input contains ```kgcl code fences (a Markdown file such as
release notes), only the lines inside those fences are checked.

For each command, prints OK with the change type, or FAIL with the parser's
message. Also notes when the parser's own rendering of the change differs from
what was written (usually harmless, e.g. an IRI shortened to a CURIE).

Exit status is 0 if every command parsed, 1 otherwise.

    python check_kgcl.py "obsolete GO:0005634" "rename GO:0005634 from 'a' to 'b'"
    python check_kgcl.py -f changes.txt
    python check_kgcl.py -f release-notes.md   # only the ```kgcl blocks
    python check_kgcl.py -f changes.txt --yaml changes.yaml   # also write the changes as KGCL YAML

Requires the kgcl-schema package (pip install kgcl-schema).
"""

import argparse
import re
import sys

try:
    from kgcl_schema.datamodel.kgcl import Session
    from kgcl_schema.grammar.parser import parse_statement
    from kgcl_schema.grammar.render_operations import render
    from kgcl_schema.utils import to_yaml
except ImportError:
    sys.exit("kgcl-schema is not installed. Install it with: pip install kgcl-schema")

BULLET = re.compile(r"^\s*[-*]\s+")
ONTOBOT = re.compile(r"^\s*hey ontobot!?,?\s*apply:?\s*$", re.IGNORECASE)


def commands_from(lines):
    lines = [line.rstrip("\n") for line in lines]
    if any(ONTOBOT.match(line) for line in lines):
        # Ontobot treats every bulleted line in the issue body as a command
        lines = [line for line in lines if BULLET.match(line)]
    elif any(line.strip() == "```kgcl" for line in lines):
        # Markdown: keep only the lines inside ```kgcl fences
        kept, inside = [], False
        for line in lines:
            if line.strip().startswith("```"):
                inside = line.strip() == "```kgcl" and not inside
                continue
            if inside:
                kept.append(line)
        lines = kept
    for line in lines:
        line = BULLET.sub("", line).strip()
        if not line or line.startswith("#") or line.startswith("```"):
            continue
        yield line


APOSTROPHE = re.compile(r"\w'\w")


def first_line(message: str) -> str:
    lines = [ln for ln in str(message).splitlines() if ln.strip()]
    return lines[0] if lines else str(message)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("commands", nargs="*", help="KGCL commands, one per argument")
    ap.add_argument("-f", "--file", action="append", default=[], help="file of commands, one per line ('-' for standard input)")
    ap.add_argument("--yaml", metavar="PATH", help="write the parsed changes to PATH as KGCL YAML (only if all commands parse)")
    args = ap.parse_args()

    lines = list(args.commands)
    for name in args.file:
        stream = sys.stdin if name == "-" else open(name, encoding="utf-8")
        lines.extend(stream.readlines())
    if not args.commands and not args.file:
        lines.extend(sys.stdin.readlines())

    ontobot = any(ONTOBOT.match(line.rstrip("\n")) for line in lines)
    try:
        from importlib.metadata import version

        print(f"kgcl-schema {version('kgcl-schema')}\n")
    except Exception:
        pass
    changes, failures, total = [], 0, 0
    for command in commands_from(lines):
        total += 1
        try:
            change = parse_statement(command)
        except Exception as e:  # lark raises several exception types
            failures += 1
            print(f"FAIL  {command}\n      {first_line(e)}")
            if APOSTROPHE.search(command):
                print(
                    "      Quoted text cannot contain an apostrophe in a KGCL command;"
                    " write this change as YAML or JSON instead."
                )
            continue
        changes.append(change)
        print(f"OK    {command}\n      -> {type(change).__name__}")
        if ontobot and ("<" in command or ">" in command):
            print("      warning: Ontobot deletes '<' and '>' from issues; use a CURIE here.")
        rendered = render(change)
        if rendered != command:
            print(f"      parser reads it as: {rendered}")

    print(f"\n{total - failures} of {total} commands parsed.")
    if args.yaml:
        if failures:
            print(f"Not writing {args.yaml}: fix the failed commands first.")
        else:
            with open(args.yaml, "w", encoding="utf-8") as out:
                out.write(to_yaml(Session(change_set=changes)))
            print(f"Wrote {len(changes)} changes to {args.yaml}.")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
