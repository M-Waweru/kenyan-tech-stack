# Authoring workspace (not published with `book/`)

Material here supports **writing, auditing, and regenerating** the manuscript. The **published** markdown tree is **`book/`** only.

## Layout

| Path | Contents |
|------|----------|
| **`meta/`** | [Structure](meta/structure.md) (master outline), [topic article schema](meta/topic-article-schema.md), [topic deepening workflow](meta/topic-deepening-workflow.md), [web citations](meta/web-citations.md), [factual rigor audit](meta/factual-rigor-audit.md) |
| **`manuscript/`** | Merged part drafts (`part-01-before-the-hype.md` … `part-20-future-stack.md`) — input to `scripts/scaffold_topic_articles.py` |
| **`AGENT-CHAPTER-GUIDE.md`** | **Hand this to another AI agent** when expanding or editing topic chapters |

## Scripts

- **`authoring/manuscript/`** → **`book/part-NN/`** via `python3 scripts/scaffold_topic_articles.py` (overwrites generated topic bodies; back up first).
- Canonical chapters for readers: **`book/part-NN/*.md`**.

## Prologue

The reader-facing prologue is **`book/prologue.md`**. `authoring/manuscript/` no longer holds a separate `prologue.md` after the split—edit the file under **`book/`** for the published book.
