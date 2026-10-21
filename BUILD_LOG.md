# Build log — on-hyperart print edition

Running record of print builds, failures, and fixes. Keep newest first.

## 2026-10-20 — DesignCraft 0.10.0 (90 pages)

**Environment:** DesignCraft 0.10.0 (MSI, `C:\Program Files\DesignCraft\designcraft-cli.exe`), `just print`.

**Result:** 90 pages, blank pages `[4]`. Contents p3, structural verso p4,
Preface p5. TOC folios regenerated. The hypermath physics section added two
pages (88 -> 90); table columns remained unequal after the rebuild.

### Fixes landed

1. **Front matter:** `tools/build_layout.py` `FRONT_PAGES` 6 -> 4. TOC page is
   derived (`FRONT_PAGES - 1`), so Contents moved to p3 and the dead spread
   p3-4 disappeared. The 9-10-12 run from 0.9.0 was already removed by
   DesignCraft #1169 (autoflow empty pages).
2. **Table widths:** `fix_tables()` selects each column and applies
   `table.setColumnWidth` using the header-proportion widths from
   `table_widths()`, scaled to the 425.28 pt text column.
3. **Hypermath sidecar:** "Physics is last" section plus a speculative
   "Far out: the seam" coda (autonomous labs, spacetime as an error-correcting
   code, cosmological archaeology, unreadable law). 90 pages.

### Bugs encountered

- **Generated scripts are not source.** `front.script` and `_step.script` are
  rewritten by `tools/build_layout.py` on every `just print`. Editing them
  directly is lost. Fix the generator.
- **DesignCraft ignores DOCX table grids.** `rewrite_docx_tables()` already
  sets `tblGrid`/`tcW`, but the importer still equalised columns (four 75 pt
  columns). Widths must be set after import.
- **`table.setColumnWidth` is selection-gated.** Passing `story`/`table` alone
  fails with `place the insertion point in a table`. Select first:
  `table.select {story, table, cols:[c,c], what:"column"}`.
- **Table indices are 1-based.** `table 0` -> `no table 0`.
- **`file.place` returns several story ids.** The last `story` in the results
  is not the body story; addressing it yields `no table 1`. `fix_tables()`
  now finds the body story by matching the chapter title against
  `document.inspect` story previews (largest matching story wins).

### Verification

- `pypdf`: page count and blank pages.
- `pdfplumber`: header word `x0` positions to prove unequal column widths.
- `designcraft-cli run --in layout/on-hyperart.designcraft --cmd
  document.inspect` to inspect story ids before writing the pass.

### Open

- **Drop caps not applied.** `Body First` is used 4-9 times per chapter
  (pandoc marks the first paragraph after every heading), so a style-level
  drop cap would hit section starts. Needs either DOCX demotion (keep one
  `FirstParagraph` per chapter) or a point/selection pass on the first body
  paragraph.
- **No figures/graphs yet.** Candidate set: verification-latency ladder,
  collapse-order timeline, Bands I-VI ladder.
- **Hypermath sidecar** still has the bracketed placeholder `Tao workflow
  commentary with dated quotes.` No open-letter material in the repo.
