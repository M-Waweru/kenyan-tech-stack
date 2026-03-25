---
title: Published book (deploy this folder)
description: Reader-facing markdown only — sync or copy this tree to your static site generator.
tags:
  - manuscript
---
# Published book content (`book/`)

Deploy **`book/`** to the web (Quartz, GitBook content root, etc.). **Do not** move `authoring/` into the same public tree unless you intend to expose internal outlines and drafts.

## What belongs here

| Path | Role |
|------|------|
| **`index.md`** | Reader landing / book home |
| **`prologue.md`** | Opening chapter (linear read starts here) |
| **`part-01/` … `part-20/`** | Topic articles (`NN-slug.md`) + per-part **`index.md`** |
| **`appendices/`** | Cast, rail map, research methodology, source catalog |

## What does **not** belong here

- Merged part manuscripts, master outline, factual audit, scaffold workflows → **`authoring/`** at repo root (see [authoring/README.md](../authoring/README.md)).

## Tooling (repo root)

- `scripts/scaffold_topic_articles.py` — reads `authoring/manuscript/part-*.md`, writes **`book/part-NN/*.md`** (destructive on topic bodies; merge first).
- `scripts/patch_topic_navigation.py` — refreshes **Navigate** footers in `book/part-NN/*.md`.
- `SUMMARY.md` — GitBook TOC; keep paths under `book/…`.

## Conventions for chapters

Summarized for agents in [authoring/AGENT-CHAPTER-GUIDE.md](../authoring/AGENT-CHAPTER-GUIDE.md): linked citations, acronym first use, narrative sections, `SRC-XX` catalog, link registry at end of each topic file.
