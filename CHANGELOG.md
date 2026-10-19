# Changelog — on-hyperart

## v0.6 (2026-10-19) — new chapter, plates at chapter starts

- **XI. LLM Writing and Its Discontents** added: the reader is not a context
  window; the Stoppard phantom as a case study in confident synthesis; the four
  frictions (unearned explanation, flat register, no public embarrassment, no
  stake); the footnote as respect. Three notes.
- **Chapter I clarified**: "the junior in the studio", one lit compositing bay,
  the night guard — scene before thesis.
- **Plates now open their chapters** (recto image, caption, then the chapter),
  not a front plate section. Rossetti dropped: it did not fit. Seven plates:
  Böcklin (Isle, Triton, Waves), Fuseli, Bosch, Blake, Bruegel.
- **Typography up**: body 12.5/19.5, margins 84/92/92/78, chapter titles 26/30;
  notes down to 7.3/9.4 (they were shouting).
- 92 pages. The 150-page target needs roughly 8-10k more words, not more
  spacing; expansion plan in the handover.

## v0.5 (2026-10-19) — print edition

- **A4 book built with DesignCraft** (`just print`): 63 pages, facing pages,
  3 mm bleed, chapter openers on rectos.
- Front matter: title page, colophon, generated table of contents with folios.
- **Eight public-domain plates** from the local painting archive
  (`just plates-local`, `layout/plates8/CREDITS.md`): Böcklin *Isle of the
  Dead*, Rossetti *Ligeia Siren*, Böcklin *Triton and Nereid*, Böcklin
  *Play of the Waves*, Fuseli *The Nightmare*, Bruegel *The Triumph of
  Death*, Bosch (Hell detail), Blake *The Whirlwind of Lovers*. 71 pages.- Running heads (book title verso, chapter title recto) and folios, static
  per page so the edition is reproducible.
- Pipeline: `layout_prep.py` (strip Status/Revision/annotated flags, keep
  `[construction]` as a word, normalize pipe-table separators) -> pandoc DOCX
  with named styles -> DesignCraft `file.place` per chapter -> post-pass heads,
  folios, TOC -> PDF.
- Known limitation: imported tables get even column widths; DesignCraft's
  column commands need a caret inside a cell, so the Ch V logbook is readable
  but cramped. Follow-up: set widths after placement.
- AI-generated plates: pending PhotoCraft (registered, disabled; needs a
  restart). Slots reserved in the plate section.

## v0.4 (2026-10-19) — review absorbed, gate closed, counter-thesis faced

- **Cold open shipped** in Ch I (02:10, credit block still empty). Variants
  stub retired from the book order — process files stay out of the covers.
- **Structural cascade from the Opus review:** AI rows into Ch V (2023–2026,
  each tagged web-verified or memory-verify); L1/L2/L3 box + Dutton answer +
  dated Bellaiche prediction; thresholds A′/B′/D′ redefined to discriminate
  synthesis; strong brakes faced (copyrightability conceded, unions named,
  licensing mutation, C2PA vs invisible watermark); lineage corrected
  (Asimov → machine government, Data → interiority test).
- **Verifier clock** (from the 2026-10-19 Drive transcripts): verified
  recombination vs model collapse, and the domain table — art fell first
  because its verifier is a mammal who answers surveys. Wired into Ch I.
- **DIY section** in Ch IV: studio-in-a-bedroom glory, three dangers
  (attention, provenance, bespoke copies), asymmetry settled by verifier
  latency (bedroom studio vs basement protein generator).
- **Ch III corrections:** the mix is not a subtraction (pepper in coffee);
  collapse is a curation failure, not a law of recombination.
- **Lepore read** (*The Rise and Fall of the Artificial State*, 2026):
  new side file — world-alienation counter-thesis, three hits, the synthesis
  with the descent ladder, and the mechanism we lacked (the corpus cannot
  tell a warning from a recipe).
- ECONOMICS_OF_HYPERART populated with three flagged tables (L3 ledger).
- Falsifier boxed in Ch II. Tetralogy language fixed. bookkit migration
  (port 11156). Ch V revision-dated 2026-10-19.

## v0.1 (2026-10-11) — skeleton

- Repo scaffold parallel to on-hyperwar / on-ai-takeover.
- README + PRD + CONTRIBUTING + chapters I-X stubs + 3 side files.
- docs/: ASSESSMENT, GLOSSARY, REFERENCES, ECONOMICS_OF_HYPERART stubs.
- tools/ ported: declaim, lorecheck (hyperart-tuned), build_site, build_epub.
- Baseline lore: 0/10 chapters real, all `[construction]`.

## Unreleased

- Primary sources for the ~16 `[memory - verify]` Ch V rows (the gate is
  now: fill or cut, not "verify later").
- Page-level cites for Lepore (print copy) and for the review's web-verified
  items (court opinion, union statements, model cards).
- German edition (chapters_de still a gitkeep).
- Integrated volume: *On Verification* — the four books as cases of one
  variable. Write after the logbooks are fuller.
