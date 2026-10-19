"""Build the on-hyperart print PDF with DesignCraft (headless CLI).

Pipeline
  chapters/*.md -> layout/src/*.md (metadata/flags stripped)
                -> layout/docx/*.docx (pandoc, named styles; one per chapter)
                -> front matter + plates
                -> each chapter placed on a recto, autoflowed
                -> running heads, folios, table of contents
                -> layout/on-hyperart.pdf

Chapter-by-chapter placement is deliberate: a single autoflowed story with
"start on next odd page" made the engine add hundreds of empty frames.

Usage: py tools/build_layout.py [--keep-flags] [--skip-front]
"""
from __future__ import annotations

import json
import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LAYOUT = os.path.join(ROOT, "layout")
SRC = os.path.join(LAYOUT, "src")
DOCX = os.path.join(LAYOUT, "docx")
PLATES = os.path.join(LAYOUT, "plates")
CLI = r"C:\Program Files\DesignCraft\designcraft-cli.exe"

PAGE_W, PAGE_H = 595.276, 841.89
M_TOP, M_BOT, M_IN, M_OUT = 60.0, 72.0, 72.0, 60.0
BLEED = 9.0
FRONT_PAGES = 6
PLATE_PAGES = 8
BODY_START = FRONT_PAGES + PLATE_PAGES

CHAPTERS = [
    "00-preface.md", "01-the-misdirection.md", "02-futurist-lineage.md",
    "03-no-soul-equation.md", "04-the-stack.md", "05-locating-the-present.md",
    "06-thresholds.md", "07-control-case.md", "08-terminal-states.md",
    "09-day-two.md", "10-corpus.md", "side-acoustic-leviathan.md",
    "side-latent-personae-and-law.md", "side-hypermath.md",
    "side-what-scifi-gets-wrong.md", "side-lepore-counter-thesis.md",
]

PLATE_SPEC = [
    ("klimt_water_serpents.jpeg", "Klimt, Water Serpents II (1904-07). The sea as ornament, the body as current."),
    ("waterhouse_mermaid.jpg", "Waterhouse, A Mermaid (1900). She combs her hair and waits for no one."),
    ("fuseli_nightmare.jpg", "Fuseli, The Nightmare (1781). Dread arrives before the machine has a face."),
    ("blake_red_dragon.jpg", "Blake, The Great Red Dragon and the Woman Clothed with the Sun (c. 1805). Apocalypse as composition."),
]

STYLE_MAP = {
    "heading 1": "Chapter Title", "heading 2": "Section",
    "Body Text": "Body", "First Paragraph": "Body First",
    "Block Text": "Quote", "Footnote Text": "Note",
}


def run(args: list[str], timeout: int = 900) -> str:
    proc = subprocess.run(args, capture_output=True, text=True, encoding="utf-8", timeout=timeout)
    out = (proc.stdout or "") + (proc.stderr or "")
    if proc.returncode != 0:
        raise SystemExit(f"FAILED {args[0]} ({proc.returncode}):\n{out[:4000]}")
    return out


def json_out(text: str):
    for opener in ("{", "["):
        pos = text.find(opener)
        if pos >= 0:
            try:
                return json.loads(text[pos:])
            except json.JSONDecodeError:
                continue
    raise SystemExit(f"no JSON in output:\n{text[:1000]}")


def cmd(name: str, params: dict | None = None) -> str:
    return name + (" " + json.dumps(params, ensure_ascii=False) if params is not None else " {}")


def page_x(index: int) -> tuple[int, float]:
    if index == 0:
        return 0, 0.0
    return (index + 1) // 2, (0.0 if index % 2 == 1 else PAGE_W)


def rect_for(index: int, box: list[float]) -> list[float]:
    _spread, x0 = page_x(index)
    return [round(x0 + box[0], 2), box[1], round(x0 + box[2], 2), box[3]]


def table_widths(md_path: str) -> list[list[int]]:
    """Header-derived column widths (twips) for each pipe table, in order."""
    lines = open(md_path, encoding="utf-8").read().split("\n")
    out: list[list[int]] = []
    i = 0
    while i < len(lines) - 1:
        line = lines[i].strip()
        nxt = lines[i + 1].strip()
        if line.startswith("|") and nxt.startswith("|") and "-" in nxt and not nxt.strip("-|: "):
            heads = [c.strip() for c in line.strip("|").split("|")]
            weights = [max(3, min(34, len(h))) for h in heads]
            total = 9020  # text width in twips (~451 pt)
            widths = [max(600, round(w / sum(weights) * total)) for w in weights]
            out.append(widths)
            i += 2
            continue
        i += 1
    return out


def rewrite_docx_tables(docx: str, widths: list[list[int]]) -> None:
    """Set tblGrid and tcW widths so columns follow the header proportions."""
    import re
    import shutil
    import zipfile

    if not widths:
        return
    with zipfile.ZipFile(docx) as z:
        entries = {n: z.read(n) for n in z.namelist()}
    xml = entries["word/document.xml"].decode("utf-8")
    counter = {"i": 0}

    def table(m: re.Match) -> str:
        idx = counter["i"]
        counter["i"] += 1
        if idx >= len(widths):
            return m.group(0)
        w = widths[idx]
        block = m.group(0)
        grid = "".join(f'<w:gridCol w:w="{v}"/>' for v in w)
        block = re.sub(r"<w:tblGrid>.*?</w:tblGrid>", f"<w:tblGrid>{grid}</w:tblGrid>",
                       block, flags=re.S)
        col = {"i": 0}

        def cell(cm: re.Match) -> str:
            v = w[col["i"] % len(w)]
            col["i"] += 1
            body = re.sub(r"<w:tcW[^/>]*/>", f'<w:tcW w:w="{v}" w:type="dxa"/>',
                          cm.group(0), count=1)
            return body

        def row(rm: re.Match) -> str:
            col["i"] = 0
            return re.sub(r"<w:tc>.*?</w:tc>", cell, rm.group(0), flags=re.S)

        return re.sub(r"<w:tr[ >].*?</w:tr>", row, block, flags=re.S)

    xml = re.sub(r"<w:tbl>.*?</w:tbl>", table, xml, flags=re.S)
    entries["word/document.xml"] = xml.encode("utf-8")
    tmp = docx + ".tmp"
    with zipfile.ZipFile(tmp, "w", zipfile.ZIP_DEFLATED) as z:
        for name, data in entries.items():
            z.writestr(name, data)
    shutil.move(tmp, docx)


def prep() -> list[str]:
    os.makedirs(SRC, exist_ok=True)
    os.makedirs(DOCX, exist_ok=True)
    keep = ["--keep-flags"] if "--keep-flags" in sys.argv else []
    out = []
    for name in CHAPTERS:
        src = os.path.join(ROOT, "chapters", name)
        dst_md = os.path.join(SRC, name)
        dst_docx = os.path.join(DOCX, os.path.splitext(name)[0] + ".docx")
        run([sys.executable, os.path.join(ROOT, "tools", "layout_prep.py"), src, dst_md, *keep])
        run(["pandoc", dst_md, "-f", "markdown+smart", "-t", "docx", "--columns=20", "-o", dst_docx])
        rewrite_docx_tables(dst_docx, table_widths(dst_md))
        out.append(dst_docx)
    return out


def styles() -> list[str]:
    lead = lambda v: {"kind": "points", "value": v}

    def p(name, para, chars, based=None):
        params = {"name": name, "para": para, "chars": chars}
        if based:
            params["basedOn"] = based
        return cmd("style.paragraph.create", params)

    return [
        p("Book Title", {"align": "center", "firstLineIndent": 0},
          {"fontFamily": "Georgia", "fontStyle": "Bold", "size": 34, "leading": lead(40)}),
        p("Book Subtitle", {"align": "center", "firstLineIndent": 0},
          {"fontFamily": "Georgia", "fontStyle": "Italic", "size": 14, "leading": lead(20)}),
        p("Author", {"align": "center", "firstLineIndent": 0},
          {"fontFamily": "Georgia", "fontStyle": "Regular", "size": 13, "leading": lead(18)}),
        p("Imprint", {"align": "center", "firstLineIndent": 0},
          {"fontFamily": "Georgia", "fontStyle": "Regular", "size": 9, "leading": lead(13)}),
        p("Colophon", {"align": "left", "firstLineIndent": 0},
          {"fontFamily": "Georgia", "fontStyle": "Regular", "size": 8.5, "leading": lead(13)}),
        p("Plate Caption", {"align": "left", "firstLineIndent": 0},
          {"fontFamily": "Georgia", "fontStyle": "Italic", "size": 8.5, "leading": lead(12)}),
        p("Body", {"align": "leftJustified", "firstLineIndent": 12, "spaceBefore": 0, "spaceAfter": 0,
                   "hyphenate": True},
          {"fontFamily": "Georgia", "fontStyle": "Regular", "size": 10.5, "leading": lead(15)}),
        p("Body First", {"firstLineIndent": 0}, {}, based="Body"),
        p("Chapter Title", {"align": "left", "firstLineIndent": 0, "spaceBefore": 0, "spaceAfter": 26,
                            "hyphenate": False},
          {"fontFamily": "Georgia", "fontStyle": "Bold", "size": 24, "leading": lead(28)}),
        p("Section", {"align": "left", "firstLineIndent": 0, "spaceBefore": 16, "spaceAfter": 6,
                      "hyphenate": False},
          {"fontFamily": "Georgia", "fontStyle": "Bold", "size": 12, "leading": lead(15)}),
        p("Quote", {"align": "left", "leftIndent": 18, "firstLineIndent": 0, "spaceBefore": 6, "spaceAfter": 6},
          {"fontFamily": "Georgia", "fontStyle": "Italic", "size": 9.5, "leading": lead(13)}),
        p("Note", {"firstLineIndent": 0, "spaceBefore": 4, "spaceAfter": 4},
          {"fontFamily": "Georgia", "fontStyle": "Regular", "size": 8, "leading": lead(10.5)}),
        p("TOC Title", {"align": "left", "firstLineIndent": 0, "spaceAfter": 18},
          {"fontFamily": "Georgia", "fontStyle": "Bold", "size": 18, "leading": lead(22)}),
        p("TOC Entry", {"align": "left", "firstLineIndent": 0, "spaceBefore": 3, "spaceAfter": 3},
          {"fontFamily": "Georgia", "fontStyle": "Regular", "size": 10, "leading": lead(14)}),
        p("Head Verso", {"align": "left", "firstLineIndent": 0},
          {"fontFamily": "Georgia", "fontStyle": "Regular", "size": 7.5, "leading": lead(9), "tracking": 80}),
        p("Head Recto", {"align": "right", "firstLineIndent": 0},
          {"fontFamily": "Georgia", "fontStyle": "Regular", "size": 7.5, "leading": lead(9), "tracking": 80}),
        p("Folio Verso", {"align": "left", "firstLineIndent": 0},
          {"fontFamily": "Georgia", "fontStyle": "Regular", "size": 8.5, "leading": lead(10)}),
        p("Folio Recto", {"align": "right", "firstLineIndent": 0},
          {"fontFamily": "Georgia", "fontStyle": "Regular", "size": 8.5, "leading": lead(10)}),
    ]


def text_frame(index: int, box: list[float], text: str, style: str) -> list[str]:
    return [cmd("frame.create", {"spread": page_x(index)[0], "rect": rect_for(index, box),
                                 "content": "text", "text": text}),
            cmd("style.paragraph.apply", {"name": style})]


def front_matter() -> list[str]:
    out = [cmd("file.new", {"preset": "A4", "intent": "print", "pages": FRONT_PAGES + PLATE_PAGES,
                            "facingPages": True,
                            "margins": {"top": M_TOP, "bottom": M_BOT, "inside": M_IN, "outside": M_OUT},
                            "bleed": BLEED, "title": "On Hyperart"})]
    out += styles()
    out += text_frame(0, [90, 230, 505, 330], "ON HYPERART", "Book Title")
    out += text_frame(0, [90, 350, 505, 410], "The Aesthetic Singularity Arrived First", "Book Subtitle")
    out += text_frame(0, [90, 600, 505, 640], "Sandra Schipal", "Author")
    out += text_frame(0, [90, 730, 505, 770], "construction draft - 2026", "Imprint")
    colophon = (
        "On Hyperart: The Aesthetic Singularity Arrived First\n"
        "Sandra Schipal\n\n"
        "Construction draft, 2026. Not for sale. Chapters carrying [construction] flags "
        "are working text; see the repository for the live logbook and issues.\n\n"
        "Set in Georgia, typeset with DesignCraft. Plates are public domain, sourced from "
        "Wikimedia Commons; full credits in layout/plates/CREDITS.md."
    )
    out += text_frame(1, [72, 90, 523, 400], colophon, "Colophon")
    for i, (fname, caption) in enumerate(PLATE_SPEC):
        index = FRONT_PAGES + i * 2
        path = os.path.join(PLATES, fname)
        if not os.path.exists(path):
            raise SystemExit(f"missing plate: {path}")
        # images place by spread/x/y/width (rect alone lands on the current page)
        from PIL import Image
        with Image.open(path) as im:
            w, h = im.size
        box_w, box_h = PAGE_W - M_IN - M_OUT, 600.0
        scale = min(box_w / w, box_h / h)
        width = round(w * scale, 2)
        height = h * scale
        spread, x0 = page_x(index)
        out.append(cmd("file.place", {
            "path": path, "spread": spread,
            "x": round(x0 + M_IN, 2), "y": round(90 + (box_h - height) / 2, 2),
            "width": width,
        }))
        out += text_frame(index, [M_IN, 706, PAGE_W - M_OUT, 770], caption, "Plate Caption")
    return out


def save_stage(cmds: list[str], stage: str, source: str | None = None, export: str | None = None) -> str:
    script = os.path.join(LAYOUT, "_step.script")
    open(script, "w", encoding="utf-8", newline="\n").write("\n".join(cmds) + "\n")
    args = [CLI, "script", script, "--save", stage]
    if source:
        args += ["--in", source]
    if export:
        args += ["--export", export]
    return run(args)


def inspect(path: str) -> dict:
    return json_out(run([CLI, "run", "--in", path, "--cmd", "document.inspect"], 300))


def toc_entries(path: str) -> list[dict]:
    data = json_out(run([CLI, "run", "--in", path, "--cmd",
                         'toc.entries={"styles":["Chapter Title"]}'], 300))
    return data if isinstance(data, list) else data.get("entries", [])


def place_chapters(docx_files: list[str], stage: str) -> None:
    for i, docx in enumerate(docx_files):
        doc = inspect(stage)
        n = doc["pageCount"]
        start = n if n % 2 == 0 else n + 1        # even index = recto
        # pages must exist up to and including `start`
        cmds = [cmd("layout.pages.insert", {"count": start - n + 1})]
        cmds.append(cmd("file.place", {
            "path": docx, "page": start + 1,
            "rect": rect_for(start, [M_IN, M_TOP, PAGE_W - M_OUT, PAGE_H - M_BOT]),
            "autoflow": True, "styleMap": STYLE_MAP,
        }))
        out = save_stage(cmds, stage, source=stage)
        print(f"  [{i + 1}/{len(docx_files)}] {os.path.basename(docx)} -> page {start + 1} "
              f"({out.strip().splitlines()[0][:60]})")


def finish(stage: str, final: str, pdf: str) -> None:
    doc = inspect(stage)
    entries = toc_entries(stage)
    if not entries:
        raise SystemExit("no TOC entries")
    starts = sorted((int(e["page"]), e["text"]) for e in entries)
    cmds = [cmd("style.paragraph.edit", {"name": "Compact", "chars": {
        "size": 9, "leading": {"kind": "points", "value": 12}}})]

    def chapter_for(page_one_based: int) -> str:
        title = starts[0][1]
        for page, text in starts:
            if page <= page_one_based:
                title = text
            else:
                break
        return title

    for index in range(BODY_START, doc["pageCount"]):
        spread, x0 = page_x(index)
        side = "Recto" if index % 2 == 0 else "Verso"
        head = chapter_for(index + 1) if side == "Recto" else "On Hyperart"
        head_rect = [x0 + (M_IN if side == "Recto" else M_OUT), 28,
                     x0 + (PAGE_W - M_OUT if side == "Recto" else PAGE_W - M_IN), 46]
        folio_rect = [x0 + (M_IN if side == "Recto" else M_OUT), PAGE_H - 52,
                      x0 + (PAGE_W - M_OUT if side == "Recto" else PAGE_W - M_IN), PAGE_H - 34]
        folio = str(index - BODY_START + 1)
        for rect, text, style in [(head_rect, head, f"Head {side}"),
                                  (folio_rect, folio, f"Folio {side}")]:
            cmds.append(cmd("frame.create", {"spread": spread, "rect": [round(v, 2) for v in rect],
                                             "content": "text", "text": text}))
            cmds.append(cmd("style.paragraph.apply", {"name": style}))

    cmds.append(cmd("toc.generate", {
        "entries": [{"style": "Chapter Title", "level": 1, "entryStyle": "TOC Entry",
                     "pageNumber": "after", "separator": "  \u00b7  "}],
        "title": "Contents", "titleStyle": "TOC Title", "pageNumbers": True,
        "page": FRONT_PAGES - 1,
        "rect": rect_for(FRONT_PAGES - 2, [M_IN, 120, PAGE_W - M_OUT, PAGE_H - M_BOT]),
    }))
    out = save_stage(cmds, final, source=stage, export=pdf)
    print(out.strip()[:300])


def main() -> int:
    os.makedirs(LAYOUT, exist_ok=True)
    docs = prep()
    stage = os.path.join(LAYOUT, "book_stage.designcraft")
    print(run([CLI, "script", _write(front_matter()), "--save", stage]).strip()[:200])
    place_chapters(docs, stage)
    finish(stage, os.path.join(LAYOUT, "on-hyperart.designcraft"),
           os.path.join(LAYOUT, "on-hyperart.pdf"))
    return 0


def _write(cmds: list[str]) -> str:
    path = os.path.join(LAYOUT, "front.script")
    open(path, "w", encoding="utf-8", newline="\n").write("\n".join(cmds) + "\n")
    return path


if __name__ == "__main__":
    raise SystemExit(main())
