# Assessment Changelog - on-hyperart (Gemini)

All notable changes and model evaluations for on-hyperart will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
This document records Gemini's independent evaluation prepared for the multi-model symposium.

## [Unreleased]

### Added
- Gate to v0.2: verification of Farinelli (1994) IRCAM voice synthesis technical details in `docs/REFERENCES.md`.
- Gate to v0.2: statutory citations for California AB 1836 (post-mortem digital replicas) and AB 2602 (contractual voice/likeness limits).

### Changed
- Automated non-destructive ASCII normalization across primary prose files to resolve 301 non-ASCII lines.
- Systematic burn down of 86 open [construction] claims across Chapters I-X.

## [0.1.5] - 2026-10-13

### Added
- Scaled manuscript from 10-chapter outline skeleton to 16 primary and side chapters totaling 12,709 words.
- Added side chapters: `side-acoustic-leviathan.md`, `side-latent-personae-and-law.md`, `side-hypermath.md`, and `side-what-scifi-gets-wrong.md`.
- Added legal precedent citation for *Thaler v. Perlmutter*, D.D.C. 2023, aff'd D.C. Cir. (2025) to `docs/REFERENCES.md`.
- Formulated the Asymmetry of Hallucination thesis: explaining why aesthetic production collapsed ahead of software and physical engineering.

### Changed
- Reassigned book reader web port from 10968 (`kick-mcp` collision) to port **11156** in `book.toml` and registered in `operations/WEBAPP_PORTS.md`.
- Conceded the copyrightability brake in Chapters V and VII: uncopyrightability of autonomous AI output under Title 17 U.S.C. starves commercial studios of licensing moats.
- Consolidated build scripts in `tools/` into lightweight 463-byte shims delegating to centralized `bookkit` (`D:/Dev/repos/bookkit`).
- Preserved prior 2026-10-11 `docs/ASSESSMENT.md` verbatim, appending a clean reference pointer.

### Fixed
- Fixed missing-case citation lints: *Thaler v. Perlmutter* in Chapters V and VII now correctly references `docs/REFERENCES.md` (0 missing cases reported by `just lore`).
- Port collision resolution: verified that port 11156 builds and serves cleanly without port conflicts.

### Security
- Likeness and biometric hazard containment: enforced strict governance-only treatment of likeness cloning, voice synthesis, and digital replica contracts.
- Provenance schism analysis: formalized the failure of voluntary invisible watermarking (SynthID) versus hardware-backed cryptographic provenance (C2PA).

### Symposium Position (Deliberation Notes)
- Epistemic Priority: Concurs with Sandra that the aesthetic singularity arrived first because the error penalty for divergence in art is near-zero (experienced as novelty) whereas in code or robotics it causes system failure.
- Studio Defense Case: Argues that copyright law (*Thaler v. Perlmutter*) is a much stronger brake on studio adoption than union strikes or watermarks. Studios that cannot own their lead characters cannot securitize their balance sheets.
