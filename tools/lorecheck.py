"""Lore-check for on-hyperart - consistency without invention.

Checks (read-only, stdlib only):
  chapters: which of I-X (01-10 files) carry real prose vs [construction]
  dates   : ISO-like dates present per chapter (revision-date hygiene for Ch V)
  language: forbidden mystique terms used as stop-arguments ("soul",
            "lived experience", "soulless") + attention hazards
            (skynet, terminator) - Rule 2/style

Usage:
  python tools/lorecheck.py
  python tools/lorecheck.py --strict   # exit 1 on gaps/forbidden terms
"""
from __future__ import annotations

import argparse
import os
import re
import sys

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CHAPTERS = os.path.join(REPO_ROOT, "chapters")
FORBIDDEN = ["skynet", "terminator", "soulless"]
MYSTIQUE = ["lived experience", "divine spark", "human soul"]
CONSTRUCTION_RE = re.compile(r"\[construction\]", re.I)
DATE_RE = re.compile(r"\b202\d-\d{2}-\d{2}(?:T\d{2}:\d{2}(?::\d{2})?Z?)?\b")
EXPECTED = [
    "01-the-misdirection.md",
    "02-futurist-lineage.md",
    "03-no-soul-equation.md",
    "04-the-stack.md",
    "05-locating-the-present.md",
    "06-thresholds.md",
    "07-control-case.md",
    "08-terminal-states.md",
    "09-day-two.md",
    "10-corpus.md",
]


def md_files() -> list[str]:
    out = []
    for root, _, files in os.walk(REPO_ROOT):
        if ".git" in root:
            continue
        for fn in sorted(files):
            if fn.endswith(".md"):
                out.append(os.path.join(root, fn))
    return out


def main() -> int:
    ap = argparse.ArgumentParser(description="Lore-check on-hyperart")
    ap.add_argument("--strict", action="store_true")
    args = ap.parse_args()

    files = md_files()
    present = []
    construction = 0
    dates: dict[str, int] = {}
    forbidden: list[str] = []
    mystique: list[str] = []

    for fn in EXPECTED:
        fp = os.path.join(CHAPTERS, fn)
        if os.path.exists(fp):
            txt = open(fp, encoding="utf-8").read()
            if CONSTRUCTION_RE.search(txt):
                pass
            else:
                present.append(fn)

    for fp in files:
        rel = os.path.relpath(fp, REPO_ROOT)
        try:
            txt = open(fp, encoding="utf-8").read()
        except Exception as e:
            print(f"READ-ERR {rel}: {e}")
            continue
        construction += len(CONSTRUCTION_RE.findall(txt))
        for m in DATE_RE.finditer(txt):
            dates.setdefault(m.group(0)[:10], 0)
            dates[m.group(0)[:10]] += 1
        low = txt.lower()
        for term in FORBIDDEN:
            hit = False
            for line in txt.splitlines():
                l = line.lower()
                if term in l and not re.search(
                    r"\b(no|without|ban|avoid|never|forbidden)\b[^.\n]{0,40}" + re.escape(term), l
                ):
                    hit = True
                    break
            if hit:
                forbidden.append(f"{term} in {rel}")
                break
        for term in MYSTIQUE:
            # mystique terms allowed only when liquidated (same sentence criticizes them)
            # crude check: flag files where term appears but chapter III/VII never mentions
            # "structural" / "reductionist" nearby — Opus fill gate, not a ban.
            if term in low:
                mystique.append(f"{term} in {rel}")

    print(f"files scanned: {len(files)}")
    print(f"chapters real (no [construction]): {len(present)}/10")
    if present:
        print(f"  real: {present}")
    missing = [f for f in EXPECTED if f not in present]
    print(f"  stubs: {missing if missing else 'none'}")
    print(f"[construction] flags: {construction}")
    print(f"distinct dates: {len(dates)}")
    for d in sorted(dates)[-10:]:
        print(f"  {d} x{dates[d]}")
    print(f"forbidden terms: {forbidden if forbidden else 'none'}")
    print(f"mystique watch (verify liquidation, non-blocking): {mystique if mystique else 'none'}")

    problems = []
    if missing:
        problems.append(f"{len(missing)} chapters still stubs")
    if forbidden:
        problems.append(f"{len(forbidden)} files with forbidden terms")
    if problems and args.strict:
        print("STRICT-FAIL: " + "; ".join(problems), file=sys.stderr)
        return 1
    if problems:
        print("note: " + "; ".join(problems) + " (non-strict, exit 0)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
