# Agent guide — writing and expanding topic chapters

Give this file (or repo root **`AGENTS.md`**) to an AI or human editor working on *The Kenyan Tech Stack*.

## Where files live

| Goal | Location |
|------|----------|
| **Published / reader-facing** | `book/` only: `book/part-NN/NN-slug.md`, `book/prologue.md`, `book/appendices/*`, `book/index.md` |
| **Outline, audits, workflows** | `authoring/meta/*` |
| **Merged part drafts (scaffold input)** | `authoring/manuscript/part-*.md` |
| **Source ID catalog** | `book/appendices/sources.md` (`SRC-XX`) |

**Do not** add internal outlines, audit tables, or draft manuscripts under `book/` if they are not meant for the public site.

## Canonical doc chain (read in order)

1. **[Topic article schema](meta/topic-article-schema.md)** — YAML front matter, section order (Lead → Context → History → … → Sources → Navigate), **acronyms**, inline citation rules.
2. **[Topic deepening workflow](meta/topic-deepening-workflow.md)** — how to turn a thin outline into a researched narrative (inventory → sources → spine → characters → citations → sync).
3. **[Web citations](meta/web-citations.md)** — clickable links in body + link reference registry at file end; `SRC-XX` in **Sources** list only.
4. **[Structure](meta/structure.md)** — full chapter list, per-chapter **cold open / rail / shadow / bridge** bullets, and the canonical **RULES FOR WRITING THIS** block (also summarized below).
5. **[Factual rigor audit](meta/factual-rigor-audit.md)** — coverage and citation gaps by part.

## Narrative rules (docu-novel)

These rules come from **[Structure — RULES FOR WRITING THIS](meta/structure.md#rules-for-writing-this-so-its-narrative-character-driven-energetic)**. Follow them in every topic chapter unless the author explicitly relaxes them for a special case.

### 1) Every chapter begins with a scene

Do **not** open with a dry year line (“In 2009…”). Open the **Lead** with a **moment** (real or composite, labelled if composite), then zoom out to thesis and stakes. Examples of moments: an agent counting cash, a student revising via SMS, a developer debugging a callback, a driver refusing a fare, a chama treasurer managing disputes, a creator posting a skit.

### 2) The three-protagonist rule

Every chapter must make visible:

- **Builder** — founder, engineer, policy architect, or institution building the rail  
- **User** — merchant, driver, student, farmer, citizen stretching the rail in practice  
- **Referee** — regulator, telco, bank, state body licensing or constraining the rail  

Map them explicitly in **Context**, **Regulation and referees**, or **Adoption** if the Lead is scene-heavy.

### 3) Name the rail

Each chapter must **introduce or evolve** a named rail (what new capability the stack gains). Say it in plain language: e.g. merchant acceptance rail, payments-as-API rail, identity rail. The **History** and **Product and mechanics** sections are natural homes.

### 4) Conflict is mandatory

Pick **one** central tension per chapter, e.g. inclusion vs fraud, growth vs livelihoods, speed vs regulation, transparency vs control, convenience vs unit economics, centralization vs interoperability. **Setbacks and controversies** and **Competition** should reflect it.

### 5) Recurring motifs

Weave the shared objects of Kenya’s stack like a novelist: agent stall, cybercafé, WhatsApp group, OTP, Till, PayBill, STK push, dashboard, protest hashtag, data center—where historically accurate.

### 6) Companies through turning points

Do **not** treat chapters as company lists. A company appears when it **changes behaviour** or has a clear **moment**. Otherwise it belongs in a footnote, appendix, or “see also,” not the spine.

### 7) Character hooks

When you name someone important, give a **hook**: what they believed, what they risked, what problem haunted them, what tradeoff they made. Add recurring figures to **[Cast](../book/appendices/appendix-cast.md)** when they become anchors.

### 8) Show energy

Kenya’s tech story is emotional: hackathon nights, agents hustling, drivers organizing, teachers improvising, policy fights. Let **Adoption** and **History** carry some of that texture—not only timelines.

### 9) Shadows honestly

Include fraud, scams, disinformation, crackdowns, exploitation, unintended harms where relevant. **Analyse and witness; do not write instructions** for wrongdoing.

### 10) Appendices

New major people or rails should stay consistent with **[Cast](../book/appendices/appendix-cast.md)** and **[Rail map](../book/appendices/appendix-rail-map.md)**; update those files when you add durable entries.

### Field vignette + referee beat (editorial target)

When deepening a chapter, aim for **at least one** concrete **field vignette** (agent kiosk, classroom, boda stage, county office, support desk) and **one referee beat** (circular, compliance update, ruling, policy memo) so the builder–user–referee triangle is under visible pressure—not only in theory.

### Mapping narrative beats → topic sections

| Beat | Typical sections |
|------|------------------|
| Cold open / moment | **Lead** (opening paragraphs) |
| Rail named and explained | **History**, **Product and mechanics** |
| Builder–user–referee | **Context**, **Regulation**, **Adoption** |
| Shadow / conflict | **Setbacks and controversies**, **Competition** |
| Bridge to next layer | **Legacy and open questions**, **Ecosystem effects**, **See also** |
| Non-neutral take for builders | **Builder read** |

Per-chapter **cold open • rail • shadow • bridge** prompts live under each chapter heading in [Structure](meta/structure.md).

## Rules checklist (every chapter)

### Narrative (docu-novel)

- [ ] **Lead** opens with a **scene or moment**, not a dry “In [year]…” abstract.
- [ ] **Builder**, **user**, and **referee** are all visible somewhere in the chapter.
- [ ] The **rail** is named and its behaviour change is clear.
- [ ] **One central conflict** drives tension (reflected in Setbacks / Competition).
- [ ] **Motifs** or concrete objects appear where appropriate.
- [ ] **Companies** enter via turning points, not undifferentiated lists.
- [ ] Named characters have a **hook**; major anchors considered for **Cast**.
- [ ] **Shadow** side is honest; no how-to for abuse.
- [ ] **Energy** (human scale) shows up, not only dates and acronyms.

### Structure, citations, and tooling

- [ ] **Sections** match the schema: Lead, Context, History, Product and mechanics, Business model, Regulation, Adoption, Ecosystem effects, Setbacks, Competition, Legacy, Builder read, See also, Sources, Navigate.
- [ ] **Acronyms:** first use in the file = **Full Name (ABBR)**; if a term appears first late, expand it there. Brand names like **M-PESA** may stay unexpanded when standard.
- [ ] **Citations:** body prose uses **markdown links** to real URLs, not bare `` (`SRC-34`) ``. Add `[key]: https://…` **registry at end of file** (after Navigate). List every cited `SRC-XX` under **Sources** with the same URL.
- [ ] **New sources:** add a row to `book/appendices/sources.md` before first use; use next free `SRC-XX`.
- [ ] **Prose:** prefer narrative paragraphs; avoid semicolon-chained unrelated clauses (`a; b; c` as lazy lists). Use periods or “and”.
- [ ] **Composite scenes** allowed if labelled *Composite* and grounded in documented practice.
- [ ] **Navigate** footer: Previous · Part index · Next (see `scripts/patch_topic_navigation.py` after bulk edits).
- [ ] **See also** links to adjacent stack chapters where useful.

## Scripts (from repo root)

```bash
# Regenerate topic files from merged manuscript (OVERWRITES topic bodies — merge first)
python3 scripts/scaffold_topic_articles.py

# Refresh only ### Navigate footers on topic files
python3 scripts/patch_topic_navigation.py
```

## Reference quality

Part I (`book/part-01/01`–`03`) is the **reference** for depth, citations, acronyms, and registry style.

## Publishing boundary

CI or Quartz should **publish `book/`** (and repo `SUMMARY.md` if using GitBook). Do not publish `authoring/` unless you explicitly want internal docs public.
