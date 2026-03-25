# Merged manuscript drafts

These files (`part-01-before-the-hype.md` through `part-20-future-stack.md`) are **one file per part** for linear reading and bulk editing.

**Canonical publishing layout** is **one topic per file** under **`book/part-NN/`**. To refresh topic bodies from these sections (overwrites `book/part-NN/*.md` chapter files):

```bash
python3 scripts/scaffold_topic_articles.py
```

Commit or stash topic-only edits before re-running if you expanded content only under `book/part-NN/` and not here.

Update **linear footers** on topic files (Previous / Part index / Next) without touching the rest of each file:

```bash
python3 scripts/patch_topic_navigation.py
```
