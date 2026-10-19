"""Prepare a chapter for typesetting: strip working metadata, keep prose.

Removes:
  - **Status:** / **Revision date:** lines (site builder hides these too)
  - inline [construction: ...] blocks (draft flags; set KEEP_FLAGS=1 to keep)

Writes UTF-8 markdown; pandoc then turns it into a styled DOCX.

Usage: py layout_prep.py <in.md> <out.md> [--keep-flags]
"""
import re
import sys

STATUS_RE = re.compile(r"^\*\*(Status|Revision date):\*\*.*$", re.M)
FLAG_RE = re.compile(r"`?\[construction:[^\]]*\]`?", re.I)
BARE_RE = re.compile(r"`?\[construction\]`?", re.I)


def normalize_tables(text: str) -> str:
    """Give pipe tables proportional column widths.

    Pandoc derives DOCX column widths from the separator dashes; equal dashes
    make every column equal, which crushes the wide "what it proves" columns.
    Widths here follow the header lengths.
    """
    def is_sep(line: str) -> bool:
        s = line.strip()
        return s.startswith("|") and s.endswith("|") and "-" in s and not s.strip("-|: ")

    def cells(line: str) -> list[str]:
        return [c.strip() for c in line.strip().strip("|").split("|")]

    out: list[str] = []
    for line in text.split("\n"):
        if is_sep(line) and out and out[-1].strip().startswith("|"):
            header = cells(out[-1])
            cols = cells(line)
            if len(header) == len(cols) and len(header) > 1:
                weights = [max(3, min(34, len(h))) for h in header]
                total = sum(weights)
                widths = [max(3, round(w / total * 64)) for w in weights]
                out.append("|" + "|".join("-" * w for w in widths) + "|")
                continue
        out.append(line)
    return "\n".join(out)


def main() -> int:
    src, dst = sys.argv[1], sys.argv[2]
    keep = "--keep-flags" in sys.argv
    text = open(src, encoding="utf-8").read()
    text = STATUS_RE.sub("", text)
    if not keep:
        # annotated flags are working notes: cut them
        text = FLAG_RE.sub("", text)
        # bare flags are prose ("[construction] flags"): keep the word so
        # surrounding emphasis still parses (**`[construction]` flags**)
        text = BARE_RE.sub("construction", text)
    text = normalize_tables(text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    open(dst, "w", encoding="utf-8", newline="\n").write(text)
    print(f"{dst}: {len(text.split())} words")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
