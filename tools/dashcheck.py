"""Dash-style check: house style is spaced em dashes in prose.

Flags, outside ``` fences:
  - " - "   spaced ASCII hyphen (should be an em dash)
  - " -"    hyphen at end of line
  - " -\n"  same, multiline

Never flags ISO dates (2026-10-19), hyphenated compounds (self-healing), or
anything inside code fences. Exit 1 if anything is flagged.

Usage: py tools/dashcheck.py [chapters]
"""
from __future__ import annotations

import os
import sys

EM = chr(0x2014)
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEFAULT_DIR = os.path.join(ROOT, "chapters")


def check_file(path: str) -> list[tuple[int, str]]:
    hits: list[tuple[int, str]] = []
    in_fence = False
    with open(path, encoding="utf-8") as fh:
        for number, line in enumerate(fh.read().split("\n"), 1):
            if line.strip().startswith("```"):
                in_fence = not in_fence
                continue
            if in_fence:
                continue
            if " - " in line or line.rstrip().endswith(" -"):
                hits.append((number, line.strip()[:90]))
    return hits


def main() -> int:
    target = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_DIR
    files: list[str] = []
    if os.path.isdir(target):
        files = sorted(
            os.path.join(target, name)
            for name in os.listdir(target)
            if name.endswith(".md")
        )
    elif os.path.isfile(target):
        files = [target]
    else:
        print(f"not found: {target}", file=sys.stderr)
        return 2

    total = 0
    for path in files:
        hits = check_file(path)
        if not hits:
            continue
        total += len(hits)
        rel = os.path.relpath(path, ROOT)
        for number, text in hits:
            print(f"{rel}:{number}: spaced hyphen, use {EM!r} -> {text}")
    if total:
        print(f"FAIL: {total} spaced-hyphen line(s); house style is ' {EM} '")
        return 1
    print(f"OK: {len(files)} file(s), no spaced hyphens outside fences")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
