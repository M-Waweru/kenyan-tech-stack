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
4. **[Structure](meta/structure.md)** — full chapter list and narrative beats when you need scope.
5. **[Factual rigor audit](meta/factual-rigor-audit.md)** — coverage and citation gaps by part.

## Rules checklist (every chapter)

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
