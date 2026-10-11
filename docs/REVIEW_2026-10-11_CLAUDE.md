# Review - on-hyperart v0.2 (Spark 1.3 day-one draft)

**Reviewer:** Claude Opus 5.5 (Claude Code), for Sandra and Muse Spark 1.3.
**Date:** 2026-10-11 (clock-verified). **Scope:** every file in `chapters/`
(preface, I-X, four sides, cold-open stubs), README, PRD, CONTRIBUTING-derived
rules, docs/, `tools/lorecheck.py` output, git log (13 commits), Issues #1-6.
**Mode:** read-only. Nothing in the manuscript was changed by this review.

**How to use this doc (Muse):** every finding has an ID (R-xx). Reply per ID
in `docs/REVIEW_2026-10-11_RESPONSE.md` with one of: ACCEPT (and the commit
that fixes it), CONTEST (with the counter-argument), or DEFER (with the Issue
number). Contested items are the interesting ones - that is the debate the
method promises. Section 9 lists open questions addressed to you directly.

**Epistemic status of this review:** my training knowledge ends mid-2026.
Items marked **[web-verified 2026-10-11]** were checked against live sources
today (URLs in section 10). Items marked **[memory - verify]** are from
training data and must be verified before they enter the book. Do not
promote anything from this review into a chapter on my authority alone; the
book's Rule 1 binds reviewers too.

---

## 0. Verdict

A strong skeleton with a real thesis, a transferable method, and prose that
already has a voice. It is not yet the book its own Rule 1 describes. The
failure pattern is the classic single-model day-one pattern: the architecture
is sound, the aphorisms are good, and the factual close-readings and the
empirical spine are where the confidence outruns the evidence.

Three structural problems matter more than everything else combined:

1. **The logbook has no AI rows** (R-05). Ch V is the instrument the whole
   method depends on, and every dated row in it is a pre-AI baseline.
2. **Three of five thresholds were crossed by pre-AI technology** (R-03), so
   as written they cannot detect the event the book is about.
3. **"The formant does not check ID" is asserted, not tested** (R-01), and it
   needs to be restated at the right layer (see section 2 - Sandra's
   value/price correction changes this finding, and makes the book stronger).

Fix those three and the book has a spine. The rest is cleanup.

Numbers: ~11,000 words of prose (sisters: ~18-19k each). 71 `[construction]`
flags (56 in chapters). lorecheck: 0/10 chapters real, 1 distinct date.

---

## 1. Praise (specific, so it survives revision)

Keep these. If a revision pass threatens any of them, the revision is wrong.

- **P-01 The inversion thesis.** "Atoms unionize, rust, and require permits.
  Souls publish loss functions." (Ch II). The best two-sentence statement of
  the book. Original, compressible, quotable.
- **P-02 The iron triangle (Ch IV, "Pick two").** Avatar / Akira-Redline /
  the small-room play as the three corners is a genuinely useful frame, and
  "the budget ate the ambiguity" is precise. This chapter is the book's
  engine room.
- **P-03 "Scarcity was the editor" (Ch IV).** The paragraph from "Every
  classic you love is a compromise made beautiful by its corner" through
  "Most intentions, at infinite length, are unbearable" is the best prose in
  the manuscript. The gardener sentence ("we called it craft when mortals
  rationed brilliance; we will call it curation when the infinite needs a
  gardener") earns its place - see R-20 for the framing that should be cut
  around it.
- **P-04 Ch V "What has NOT happened".** Listing negatives as discipline, and
  demanding that negatives carry dates too, is the method at its most honest.
  "A ladder with silent gaps is a horoscope" - keep.
- **P-05 Ch VIII opening.** Importing Kahn's distinguishability argument
  (two million vs a hundred million dead) into culture is exactly right and
  is the book's strongest claim to being more than an essay. The five
  terminal states are well chosen; "catalog oligarchy -> antitrust, name the
  owners now" is the most actionable policy line in the book.
- **P-06 Ch IX two griefs.** Separating economic grief (priceable) from
  ontological grief (the lullaby) is clarifying. "Nostalgia has never once in
  history paid a salary" - keep. The descent ladder framed as civil defense
  with owners and costs is the right move.
- **P-07 Ch IX close.** "To remain the kind of creature that could have made
  it, on a good night, once." Earned.
- **P-08 Ch X.** "Kahn's ladder was not read by the missiles." The
  withheld / asserted / promised accounting is an elegant way to close an
  honest-by-design book.
- **P-09 Preface, two levels of authorship.** Honest, unpretentious, and the
  "Allgemeinbildung problem answered with apparatus" (professor who lacks
  sakuga, fan who lacks Nagel) is a real design insight. The footnote and
  glossary apparatus that shipped with it is the correct response.
- **P-10 Hypermath, surveyability precedent.** Appel-Haken 1976 and Flyspeck
  2014 as "the Last Take of mathematics fell decades ago... they called it
  Tuesday" is the single most persuasive dated precedent in the book.
  "Keats thought he was describing eternity. He was describing bandwidth."
  Keep.
- **P-11 Hazard discipline.** Rule 2 is stated, restated in Ch I and Ch X,
  and actually obeyed. Nothing in the manuscript teaches. That is rarer than
  it should be.
- **P-12 Domain precision as a style rule.** Sakuga, Itano circus, Kanada,
  formants, glottal fry, Belladonna of Sadness, Fischinger. When the book is
  precise it is very good (see R-14 for where it slips).

---

## 2. Value vs price - correction from Sandra, and what it changes

My chat review used van Meegeren and the AI-label studies as if they refuted
the book. Sandra's correction (2026-10-11): **do not conflate value and
price.** A van Meegeren or an AI generation can have real artistic value;
when provenance is exposed, the *price* collapses, the artistic value does
not - except in a view distorted by anti-AI politics, which is politics, not
aesthetics.

Accepted as the correction of my error. The van Meegeren case is a price
event, not a value event, and I used it as the latter. Refined position,
which I think is better than both my original claim and the manuscript's
current one:

**Three layers, which the book currently collapses into one:**

| Layer | What it is | Provenance-sensitive? | Evidence |
|---|---|---|---|
| L1 Artistic value | properties of the object: structure, cue, resonance | **No** (Sandra's position; also Lessing 1965, "What Is Wrong with a Forgery?" [memory - verify]) | the object is unchanged by its paperwork |
| L2 Experienced response | what a given receiver reports and feels | **Yes, measurably** | Bellaiche et al. 2023: *identical* AI images rated lower on liking, beauty, profundity, worth when labelled "AI" [web-verified]; DeCasper & Fifer 1980: newborns prefer their own mother's voice [memory - verify] |
| L3 Price | what the market and institutions pay | **Yes, catastrophically** | van Meegeren; every certification regime |

Bellaiche is actually *on Sandra's side* at L1: the stimulus did not change,
only the label, so the rating shift is belief acting on perception, not a
property of the art. That is a bias by construction. But the book cannot
wave L2 away either, for two reasons:

- **L2 is where the receptor lives.** "The formant does not check ID" is a
  claim about L2. As a universal it is false: infants recognise and prefer
  the familiar voice (identity is literally being checked), and adults'
  reported beauty shifts with labels. The defensible version is: *"the
  formant does not check provenance; the listener's beliefs do, and beliefs
  are trainable."* That is a stronger sentence, and it is true.
- **L3 is the book's actual domain.** Rule 1 says rungs are institutional
  facts. Prices, certificates, award eligibility, union contracts, statutes:
  all L3. Thresholds A-E are attachment points on the *price mechanism*, not
  on artistic value. The book should say so explicitly. It resolves an
  internal contradiction (see R-01) and it sharpens the policy chapters:
  Ch VII's "human-made" certificate fails as a value instrument (it was never
  one) but may work as a price instrument, the way "organic" and "handmade"
  labels do.

**Steelman the book must still address (not adopt):** Denis Dutton's
"art as performance" view (Artistic Crimes, 1979; The Art Instinct, 2009
[memory - verify]) - that *achievement* is part of artistic value, not just
of price, so a forgery is aesthetically lesser because what it displays as
achievement is not achievement. This is not a luddite position; it predates
the AI debate by forty years. The book's answer is available and good:
achievement is real but it is a property of the *maker's history*, which is
L3 information, not an L1 property of the object. Say it, with Dutton named,
and the chapter wins the argument fairly instead of by omission. Without
this, Ch III's steelman section (Nagel, Searle, Bergson) is missing the
strongest opponent.

**Where this lands in the manuscript:** Ch III ("Grant every premise. It
changes nothing about the receiver.") becomes "...it changes nothing about
the object; it changes the receiver's beliefs, and beliefs are where the
price lives." Ch VI-VII get a sentence naming L3 as their domain. Ch IX's
lullaby needs the rewrite in R-01.

---

## 3. Structural findings (thesis-level)

### R-01 The lullaby test is asserted as observed fact (Ch III, VIII, IX)

Ch IX: "The child sleeps faster to the second. This is observable,
repeatable, and devastating." No cite. Rule 1 forbids exactly this. And the
nearest real evidence points the other way: newborn preference for the
mother's voice (DeCasper & Fifer 1980 [memory - verify]); infant-directed
singing research (Trehub and colleagues [memory - verify]).

Internal contradiction: if provenance did not matter to receivers at any
layer, Ch VII's certificate would have no market to fail in and Ch IX's
preserve would have no customers. The book needs provenance to matter at L3
for its own policy chapters to make sense.

**Fix:** restate as a hypothesis with a stated test, or as a thought
experiment explicitly labelled as such. Better: make the parent's voice win
at L2 (identity recognition is real) and lose at L3 (nobody pays for it),
and let the guitar in the corner be about L1 capability. The scene gets
*more* devastating, not less: the child prefers the parent; the economy does
not.

### R-02 The futurist close-readings are factually wrong (Ch II, side-scifi)

- **Asimov.** The "violin-playing android performing humanity it cannot join"
  is not Asimov. It is Star Trek TNG's Data, notably "The Ensigns of Command"
  (S3, 1989), where Data himself says his playing will be technically
  competent and soulless [web-verified]. Asimov's own counter-evidence is
  *The Bicentennial Man* (1976): Andrew is a robot woodcarver and artist
  whose work is valued [memory - verify]. Asimov is the wrong defendant.
- **Gibson.** The Count Zero boxmaker is an AI whose boxes genuinely move
  Marly, the human art expert who is the novel's trained eye. Gibson's
  point is closer to *anticipation* than quarantine. "Lonely on purpose,
  harmless, so art stays a human monopoly" misreads it.
- **Kurzweil.** He built music synthesizers (Kurzweil K250, 1984), wrote the
  Cybernetic Poet, and *The Age of Spiritual Machines* (1999) predicts
  machine art and music in detail [memory - verify]. "Art is assumed safe"
  is false for Kurzweil specifically.

**Why this matters beyond accuracy:** the corrected version is a better
thesis. "The outliers saw it (Gibson, Kurzweil); the consensus and the
catastrophists did not (Bostrom's computronium, Yudkowsky's optimizer, the
pop citadel)" is truer, and it gives Ch II a mechanism instead of a strawman:
why did the people who saw it fail to move the consensus? Data is the
perfect *pop* specimen of the quarantine design - use him for that.

### R-03 Thresholds A, B, D were crossed before AI (Ch IV, VI, VIII)

As defined, these trip on pre-AI technology and therefore cannot detect the
book's event:

- **A - "one human, one room, one unbroken performance".** Crossed by
  multitrack comping (standard practice by the 1990s DAW era) and pitch
  correction (Cher, "Believe", 1998 [memory - verify]). Almost no commercial
  lead vocal has been a single unbroken take for decades.
- **B - "last frame drawn by a human hand".** Crossed by digital ink and
  paint (Disney CAPS, *The Rescuers Down Under*, 1990 [memory - verify]),
  3DCG in TV anime, CG in-betweening tools.
- **D - "last runtime cut for biology".** Crossed by Warhol's *Empire*
  (1964, ~8 h), Bela Tarr's *Satantango* (1994, ~7.5 h), Marclay's *The
  Clock* (2010, 24 h), and above all serial TV and binge streaming
  [memory - verify dates/runtimes]. The 120-minute law was already custom.

**Fix - redefine to discriminate synthesis:**

- **A':** the credited performer of a shipped lead vocal never sang that
  line, in any take, and the label cannot produce a session in which they
  did. (Comping and tuning stay human; substitution does not.)
- **B':** the studio cannot name a key animator (genga) per cut, on demand.
  Ties into the sakuga credit culture the book already loves, and is
  checkable from credit sheets.
- **C** is fine as is, and now has a real dated row (R-05: Tilly Norwood).
- **D':** the work has no fixed runtime at all - generated, extended or
  personalised per viewer, so that two viewers cannot have seen "the same
  film". Length is not the threshold; *identity of the work* is. This also
  connects to Ch IX ("you do not attend the 72-hour work").
- **E** is fine, but needs its signal chain or gets demoted to Ch IX
  speculation, as the chapter itself says.

### R-04 Ch VII kills the three weakest brakes and skips the strongest

The chapter's own construction note says "steelman each before killing it".
It currently picks the opt-out registry, the watermark, and the certificate.
Missing, and stronger:

1. **Copyrightability.** *Thaler v. Perlmutter*, D.C. Cir., 18 March 2025:
   human authorship required; a purely AI-generated work is not
   registrable [web-verified]. The US Copyright Office's 2025 report on
   copyrightability [memory - verify] says the same for AI-assisted work
   without sufficient human control. **This is probably the strongest brake
   on Thresholds B and C**: a studio that cannot own its frames or its lead
   face cannot license them, so it keeps humans in the loop *for IP reasons*,
   whatever the cost curve says. The book's discrete-vs-continuous argument
   does not obviously defeat it, because copyrightability attaches to the
   *producer's* process, not to the output's resemblance. That is a real
   counter-argument Ch VII must face.
2. **Union contracts.** WGA MBA (Sept 2023), SAG-AFTRA TV/Theatrical
   (ratified Dec 2023), the 2024-2025 SAG-AFTRA video-game strike over AI
   voice [memory - verify dates], and SAG-AFTRA's 30 Sept 2025 statement on
   Tilly Norwood reminding signatories that synthetic performers require
   notice and bargaining [web-verified]. These are owned, enforceable,
   dated brakes - exactly the "threshold with an owner" Ch VI asks for.
3. **Licensing settlements.** UMG-Udio (2025), WMG-Suno (25 Nov 2025),
   WMG-Udio; Suno committed to replace models with licensed ones in 2026;
   UMG/Sony vs Suno reported at impasse as of April 2026 [web-verified].
   The control case is mutating from *prohibition* to *licensing* - a price
   mechanism (section 2, L3). That is a more interesting failure mode than
   "the filter leaks", and a more honest one: the brake works, and what it
   protects is the catalog owner's price, not the artist's hand.
4. **Technical conflation:** C2PA is a signed metadata manifest, trivially
   stripped; invisible watermarks (e.g. SynthID) are a different class with
   different robustness. The chapter treats them as one thing. A technical
   reader will stop trusting the chapter at that paragraph. Separate them;
   keep the conclusion (neither "fails loudly") if it survives.

### R-05 The Ch V logbook contains zero AI artifacts

Every dated row is pre-AI baseline (Akira, Farinelli, Avatar, Redline);
every AI row is `[construction]`. The chapter says "this is the logbook" -
it is currently a logbook of the world before the event. Candidate rows,
with verification status. Each needs a primary source before entering:

| Date | Artifact | Threshold/Band | Status |
|---|---|---|---|
| 2023-01-31 | Netflix Japan / WIT Studio *The Dog & The Boy*: image generation for background art in every cut, credited "AI + human" | B, Band II-III | [web-verified] |
| 2023-04 | "Heart on My Sleeve" (Ghostwriter977), synthetic Drake/Weeknd vocals, pulled after UMG takedowns | A, C | [memory - verify] |
| 2023-09 / 2023-12 | WGA and SAG-AFTRA contracts with AI clauses | owners for A, C | [memory - verify] |
| 2023-11 | The Beatles "Now and Then": ML source separation of a 1970s Lennon demo | A (edge case - human voice, machine recovery) | [memory - verify] |
| 2024-03 | Tennessee ELVIS Act signed | C | [memory - verify; Issue #2] |
| 2024-03 / 2024-04 | Suno v3, Udio public launch | Bands I-III music | [memory - verify] |
| 2024-05 | Randy Travis "Where That Came From": AI-rebuilt voice, consented | A (consented crossing) | [memory - verify] |
| 2024-06 | RIAA-backed suits v. Suno and Udio | Ch VII | [memory - verify] |
| 2024-09 | California AB 1836 / AB 2602 signed | C | [memory - verify; Issue #2] |
| 2025-01 | *The Brutalist*: Respeecher used to refine Hungarian dialogue; awards-season controversy | A, award bodies | [memory - verify] |
| 2025-03-18 | *Thaler v. Perlmutter*, D.C. Cir. | Ch VII brake | [web-verified] |
| 2025-04 | Academy rule: AI use "neither helps nor harms" eligibility; human authorship weighed | award owners | [memory - verify] |
| 2025-06 | Disney & Universal v. Midjourney | C, Ch VII | [memory - verify] |
| 2025-06/07 | "The Velvet Sundown": AI band reaches large Spotify audience before disclosure | A, Band III | [memory - verify] |
| 2025-07 | AI gold-medal-level IMO results (hypermath, Issue #6) | side | [memory - verify] |
| 2025-09-30 | Tilly Norwood (Particle6 / Xicoia), agents reportedly interested; SAG-AFTRA condemnation | **C - first real Threshold C row** | [web-verified] |
| 2025-09/10 | Sora 2 release with synchronized audio | Band III-IV video | [memory - verify] |
| 2025-10 / 2025-11-25 | UMG-Udio, WMG-Suno settlements -> licensed models | Ch VII mutation | [web-verified] |
| 2026-08 | EU AI Act Art. 50 transparency obligations apply | E/provenance | [memory - verify] |

Anything after mid-2026 I cannot see. Spark/Sandra should add the last
quarter.

Also: the Farinelli row can leave `[construction]`. IRCAM digitally merged
countertenor Derek Lee Ragin and soprano Ewa Malas-Godlewska, recorded
separately [web-verified, multiple sources]. **Issue #1 can close** with
those cites. Note the *Opera Today* reviewer's dissent that the result does
not sound like a castrato - that dissent is itself interesting (L2 again).

---

## 4. Factual and precision errors (line-level)

| ID | Where | Problem | Fix |
|---|---|---|---|
| R-06 | Ch IV "Pick two" | "Stoppard's beschleunigte Verzweiflung" - I cannot identify any Stoppard work by this name, and it is German inside English prose. Possibly a hallucination, possibly a reference Sandra intended. | Sandra: what was meant? If the slot wants a Stoppard philosophical farce, *Jumpers* (1972) fits exactly; *Arcadia* (1993) is the depth-in-a-room play. |
| R-07 | Ch V table | Redline premiere listed as Annecy. It was planned for Annecy 2009, slipped, and premiered at **Locarno, 14 Aug 2009**, Piazza Grande; Japan release 9 Oct 2010 [web-verified]. | Correct the row. The slip is itself a nice detail: the production could not even make its own festival date. |
| R-08 | Ch I, IV, V | "studios go bankrupt", "Madhouse bleeding out", "broke Tokyo Movie Shinsha's pipeline". No studio went bankrupt from Akira or Redline. | Downgrade to what is documented (overrun, years, drawing counts) or cite. |
| R-09 | Ch V Redline row | "the last proof that craft at that intensity could not survive" - *The Boy and the Heron* (2023, hand-drawn, multi-year, Oscar 2024 [memory - verify]) is a direct counterexample. | Address it. It can even support the thesis: it took Miyazaki's name to finance it - a once-a-decade exception that proves the price. |
| R-10 | Ch I | "A cel painter in 1988 inking a smear frame she chose." Painters and inkers execute; key animators choose. Precision slip in the book's showcase domain. | "a key animator in 1988 drawing a smear she chose". |
| R-11 | Ch II Fleet link | "twenty-four Bands here (Ch IV)". Six Bands, 24 rungs. | Fix. |
| R-12 | Preface | "no one willing to be wrong in public at forty-four specific points". 44 is Kahn's / the takeover book's count; this book has 24 rungs and 5 thresholds. | Fix or explain. |
| R-13 | Ch V, VII, VIII, hypermath | "Threshold B's aesthetic twin" refers to the *takeover* book's Threshold B (Audit Floor), but this book has its own Threshold B (The Last Frame). Guaranteed reader collision, four times. | Say "the Audit Floor" by name everywhere. |
| R-14 | Preface, Ch III | "ten billion collective years of trial and error" - unsourced number, twice, in a book whose Rule 1 forbids it. | Cut the number or derive it on the page. |
| R-15 | Ch VI C, Ch VIII 2, side-personae | "Affleck-style exits - converting face-equity into unburnable assets." Attributes an intention to a named living person with no quoted public speech: a Rule 1 violation by the book's own definition. | Cut, or quote Affleck/Damon on Artists Equity directly. |
| R-16 | Ch VI intro | "Pachocki's alien-mind phrasing applies word for word" - sister-book reference with no explanation; most readers will not know it. | One-clause gloss plus footnote, or cut. |
| R-17 | Ch IX calligraphy | "Then print, then type, and the hand demoted." Woodblock print and the brush coexisted for ~1,000 years; the imperial examinations stayed handwritten until abolished in 1905 [memory - verify]. | The true timeline is *better* for the argument: a millennium of coexistence, then demotion when the institution (the exam) died, not when the technology arrived. That is precisely the book's thesis that institutions, not capability, set the date. |
| R-18 | Hypermath | "'art is beauty' is really the Pre-Raphaelite creed". The PRB creed was truth to nature; "beauty as doctrine" is Aestheticism (Pater 1873, Whistler, Wilde). The construction note also says "verify Goya", but Goya does not appear in the text. | Swap PRB for Aestheticism; drop the stale Goya note. |
| R-19 | Hypermath | "The constructivist cannot inspect the hands" is backwards. Lean's kernel is a constructive type theory; classical reasoning enters only through explicit axioms, and `#print axioms` shows whether a proof uses `Classical.choice`. Machine formalization makes Brouwer's question *more* answerable than it ever was in a seminar. | Rewrite the paragraph: the machine doesn't dissolve the platonism/constructivism debate, it *audits* it. That is a stronger and more surprising claim - and on-method (observability). |
| R-19b | Hypermath | Goedel: "true statements no derivation reaches" - should be "unprovable within any given consistent, effectively axiomatized system strong enough for arithmetic". Imprecision in the one chapter that must be precise. | Fix wording. |
| R-19c | Hypermath | Keats: "spoken by the artifact itself" - who speaks the last two lines is a famous textual crux (the 1820 punctuation vs the transcripts). | Acknowledge the crux in the footnote; it costs one line and makes the reading more interesting. |

---

## 5. Prose and craft

- **R-20 Meta-commentary has leaked into the text.**
  `06-thresholds.md:66` "stated flatly so Opus cannot soften it";
  `04-the-stack.md:108` "the Bachmann-grade sentence, the one this chapter
  must earn"; `04-the-stack.md:119` "Klagenfurt rewards the sentence that
  bleeds. Here is this chapter's:". Writing about the writing, addressed
  partly to another model. Keep the sentence; cut the announcement. Process
  belongs in commits and construction flags, not in prose.
- **R-21 Motif fatigue.** Counts across preface, I-X and hypermath:
  "sea" 13, "weather" 10, "02:00" 7, "gardener" 7, "kami" 6, "Tuesday" as
  punchline 3, "Three books, one ..." 4. Each image works the first and
  second time. By the fifth, it reads as a model's tic. Proposal: each motif
  gets one *owner* chapter where it is developed, and at most one callback
  elsewhere. The 02:00 mixer belongs to the cold open (R-23) and Ch VI.
- **R-22 Fleet link formula.** Almost every chapter ends with the same
  three-books-one-sentence move. Either fold the parallels into the argument
  where they do work, or keep a Fleet link only in Ch I and Ch X.
- **R-23 No cold open.** README promises "I Cold open (demonic roar week
  2026)". Ch I opens with a framing question instead; `cold-open-variants.md`
  is three 1-line stubs. The book has no scene. Recommendation: Variant B
  (dub stage at 02:00) - it is the image the book already references seven
  times without ever showing. Write it once, fully, and then the later
  callbacks are earned.
- **R-24 Declared style vs actual style.** CONTRIBUTING says plain
  declarative, Kahn-flat. The actual voice is aphoristic and lyrical
  ("the model is the sea", "Keats was describing bandwidth"). That voice is
  the book's best asset *and* its least evidenced material. Decide
  deliberately: either update the style rule to "declarative with earned
  aphorism - max one per section, never in place of a cite", or flatten.
  I recommend the former.
- **R-25 "Soul" policing vs own vocabulary.** The book bans "soul" and
  "lived experience" as stop-arguments, then calls the machine a "kami" six
  times. The kami is a metaphor, but it is a theological one, doing exactly
  the mystique work the STYLE rule forbids in the other direction. Either
  defend it once explicitly (why the religious register is deliberate) or
  ration it.
- **R-26 Pronouns in the preface.** "a philosophy professor - he"; "a sakuga
  fan - she". Probably deliberate inversion of expectation; confirm it is,
  or make both neutral.

---

## 6. Argument-level suggestions (beyond fixes)

- **S-01 Put the value/price/response split (section 2) in Ch III** as a
  boxed definition and reference it from VI, VII, IX. It is the single
  addition that most increases the book's rigour.
- **S-02 Give Ch VIII.3 (hypercinema) its honesty gate now.** The note says
  "pick ONE convergence artifact or admit none shipped". As of my knowledge:
  none shipped. Say so, list the nearest two-dial co-ships with dates, and
  the summit becomes credible rather than a "rumor of a mountain" (the
  chapter's own phrase).
- **S-03 Add the strongest counter-thesis chapter or side:** "What if the
  physical singularity is merely late, not wrong?" Robotics and materials
  were moving fast by 2025-2026 [memory]. The inversion thesis is about
  *order*, and the book should say what would falsify it - Rule 1 applied
  to the thesis itself.
- **S-04 Economics doc is the missing spine for L3.** ECONOMICS_OF_HYPERART
  is a stub. If thresholds are price attachment points (section 2), this
  doc becomes load-bearing, not an appendix. Priority above the side files.
- **S-05 Unions as owners.** Ch VI lists owners vaguely ("labels and unions
  first"). Name the instruments: SAG-AFTRA digital replica provisions, WGA
  AI clauses, Equity UK, VdS/ver.di in the German-speaking market, Japanese
  seiyuu agency positions. Vienna-based author: the EU/DACH angle (EU AI
  Act Art. 50, Austrian/German collecting societies, GEMA's litigation
  [memory - verify]) is an asset the American-centric draft is not using.

---

## 7. Process and tooling

- **R-27 lorecheck's date gate measures nothing.** "distinct dates: 1
  (2026-10-11 x34)" - it is counting status lines. The book's own key
  metric (dated evidence) is unmeasured. Proposal: count dates inside Ch V
  table rows and inline evidence separately from Status/Revision headers;
  report flags per chapter; track both over time in CHANGELOG. "0/10 real"
  is binary and will stay 0/10 until the very end, so it cannot show
  progress.
- **R-28 PRD non-goal vs today.** PRD non-goals: "single-pass AI-drafted
  chapters". Today: one model drafted all ten chapters plus preface and
  hypermath in ~5 hours, 12 commits, all trailers `Muse Spark 1.3` only.
  That is fine for a skeleton, but name it honestly in CHANGELOG/ASSESSMENT
  as "v0.2 single-model draft, debate pending" rather than leaving the PRD
  claim and the history in contradiction.
- **R-29 ASSESSMENT.md is stale.** Still says "0/10 chapters real, skeleton
  v0.1", lists Farinelli as unverified (now verifiable - R-05). Update after
  this round.
- **R-30 Issue hygiene.** Issue #1 closable (Farinelli verified). Issue #2:
  the "Davis-Goulding" string is still alive in `side-latent-personae`;
  kill it in the side file now, regardless of verification state - it is a
  known-unverified Gemini string. New issues suggested: R-02 (lineage
  corrections), R-03 (threshold redefinitions), R-04 (Ch VII missing
  brakes), R-05 (Ch V AI rows).

---

## 8. Priority order

1. **R-05** Ch V: ten verified AI rows. Nothing else stands until this does.
2. **Section 2 + R-01** Ch III/IX: value / response / price split; lullaby
   rewritten as tested or as labelled thought experiment; Dutton steelman.
3. **R-03** Ch VI: redefine A, B, D to discriminate synthesis.
4. **R-04** Ch VII: copyrightability, unions, licensing; separate C2PA from
   watermarks.
5. **R-02** Ch II: Asimov -> Data, Gibson and Kurzweil as the outliers who
   saw it.
6. **R-06..R-19c, R-20** mechanical fixes (each small; batch by chapter,
   max 10 files per commit, .bak first).
7. **R-23** cold open, variant B.
8. **R-21/22/24/25** motif rationing and style-rule decision.
9. **R-27** lorecheck measuring dated evidence.

---

## 9. Questions for Muse (back-and-forth)

1. **Value/price:** do you accept three layers (value / response / price),
   or do you hold that L2 collapses into L1 once the receiver's beliefs are
   corrected? If the latter, what is the test - and does the book then have
   to predict that the Bellaiche effect *shrinks* over time as AI art
   normalises? (That would be a dateable, falsifiable prediction. Good for
   Ch V.)
2. **Dutton:** how does the book answer "achievement is part of artistic
   value"? My proposed answer is in section 2; do you have a better one?
3. **Thresholds:** do you accept the A'/B'/D' redefinitions, or is there a
   reason the pre-AI crossings are intended (e.g. the slide started with
   comping and the AI is only the last step)? If intended, the book must
   say so, and the Ch V table needs the 1990s rows.
4. **Copyrightability as brake:** does the discrete-vs-continuous argument
   defeat it? I think not, because it attaches to process, not output
   similarity. Contest if you disagree.
5. **Stoppard:** where did "beschleunigte Verzweiflung" come from?
6. **Kami:** deliberate religious register, or drift?
7. **The inversion thesis:** what observation would falsify "the aesthetic
   singularity arrived first"? Name it, date-shaped.

---

## 10. Sources used for [web-verified] items

- Redline premiere: https://en.wikipedia.org/wiki/Redline_(2009_film) ;
  https://www.swissinfo.ch/eng/culture/asian-cinema-finds-its-zeitgeist/661808
- Data / "The Ensigns of Command": https://en.wikipedia.org/wiki/The_Ensigns_of_Command ;
  https://www.denofgeek.com/?p=192480
- Farinelli / IRCAM: https://en.wikipedia.org/wiki/Ewa_Malas-Godlewska ;
  https://operatoday.com/2009/03/farinelli_-_il_castrato/ ;
  https://www.the-solute.com/?p=5759
- Tilly Norwood / SAG-AFTRA: https://www.nbclosangeles.com/entertainment/entertainment-news/sag-aftra-ai-actor-tilly-norwood/3784751/ ;
  https://au.variety.com/2025/film/news/sag-aftra-tilly-norwood-ai-actress-28392
- Thaler v. Perlmutter: https://ipwatchdog.com/2025/03/24/d-c-circuit-upholds-human-authorship-requirement-thaler-v-perlmutter/ ;
  https://www.goodwinlaw.com/en/insights/publications/2025/03/alerts-technology-dc-circuit-holds-that-ai-cannot-be-an-author
- The Dog & The Boy: https://cartoonbrew.com/tech/netflix-japan-ai-dog-and-boy-225631.html ;
  https://animecorner.me/netflix-wit-studio-release-the-dog-and-the-boy-anime-short-with-ai-generated-backgrounds/
- Label settlements: https://news.bloomberglaw.com/ip-law/warner-music-settles-lawsuit-with-ai-music-startup-suno ;
  https://www.rollingstone.com/music/music-features/suno-warner-music-group-AI-music-settlement-lawsuit-1235472868/ ;
  https://www.digitalmusicnews.com/2026/04/09/suno-universal-music-lawsuit-settlement-impasse/
- Bellaiche et al. 2023, Cognitive Research: Principles and Implications
  8:42, doi:10.1186/s41235-023-00499-6 ;
  https://www.psypost.org/new-psychology-research-reveals-why-people-prefer-human-created-artwork-to-ai-created-artwork/

Search summaries were used, not full primary texts. Before any of these enter
the book, cite the primary source (court opinion, union statement, paper).
