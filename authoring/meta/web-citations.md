---
title: Web citations — linked sources in topic chapters
description: How to cite sources for online readers — markdown links, link reference registries, and SRC-XX IDs.
tags:
  - meta
  - workflow
---
# Web citations (linked sources)

The book is read **on the web** as well as in print-minded forms. **Body prose** should point to real URLs with **clickable markdown links**, not bare `` (`SRC-34`) `` tags that force readers to hunt the appendix.

This page is the **canonical how-to**. It complements:

- [Topic article schema — Inline citations (web edition)](topic-article-schema.md#inline-citations-web-edition) (normative rules in the chapter template)
- [Topic deepening workflow — Phase 5](topic-deepening-workflow.md#phase-5--citation-hygiene) (when expanding drafts)
- [Source Catalog](../../book/appendices/sources.md) (master list of `SRC-XX` ↔ URL)

## Reference implementation

**Part I** topic files apply this pattern end-to end:

- [`book/part-01/01-banking-in-the-dark.md`](../../book/part-01/01-banking-in-the-dark.md)
- [`book/part-01/02-cybercafe-republic.md`](../../book/part-01/02-cybercafe-republic.md)
- [`book/part-01/03-telcoms-before-the-boom.md`](../../book/part-01/03-telcoms-before-the-boom.md)

Open any of them, scroll to the **bottom** (after **Navigate**): you will see an HTML comment plus **`[key]: https://…`** lines. That block is the **link reference registry**.

## Steps (per chapter)

1. **Add or reuse rows** in [Source Catalog](../../book/appendices/sources.md) for every URL (`SRC-XX`). New source → next free ID → full URL in the catalog.
2. **In body prose**, cite with readable anchor text, e.g. `the [KBA technology timeline][kba-tech]` or `([CBK bulletin *Kenya’s Payments Journey*][cbk-payments])`.
3. **Define each `[key]` once** at the end of the same topic file (after **Navigate** is fine; Markdown processors resolve references globally within the file).
4. **Duplicate the URLs** in the chapter **Sources** section as bullets: `` `SRC-34` — [Title](https://…) `` so IDs stay visible for print, footnotes, or tooling.
5. **Avoid semicolon chains** used only to stack unrelated clauses (`x; y; z`). Prefer **periods**, **commas + “and”**, or a **second sentence**. (See Part I edits for tone.)

## Minimal template

Paste at the **end** of `book/part-NN/NN-slug.md` (adjust keys and URLs; mirror catalog):

```markdown
<!-- Inline citation targets — see **Sources** for `SRC-XX` IDs. -->
[kba-tech]: https://bankinghistory.kba.co.ke/technology/
[cbk-payments]: https://www.centralbank.go.ke/wp-content/uploads/2023/02/Kenyas-Payments-Journey.pdf
```

Body:

```markdown
The [KBA technology timeline][kba-tech] dates the first mainframe to **June 1968** …
```

## Acronyms

Spell out the **full name on first use** in each chapter, then the abbreviation in parentheses (see [Topic article schema — Acronyms](topic-article-schema.md#acronyms-and-initialisms)). Online readers skim; do not assume everyone knows **USSD**, **KYC**, or **CA** without a prior expansion in that file.

## Naming keys

- Short, **unique per file** (`wiki-safaricom`, `ca-stats`, `uon-thesis`).
- Keys **do not** have to include `SRC-XX`; the **Sources** list maps IDs to the same URLs.

## When a chapter has no new sources

You still need a **registry** for every `[key]` used in prose. If you only cite `SRC-18` and it is already in the catalog, add `[ca-stats]: https://www.ca.go.ke/statistics` locally and list `SRC-18` under **Sources**.

---

← [Topic article schema](topic-article-schema.md) · [**Book home**](../../book/index.md) · [Source Catalog](../../book/appendices/sources.md) →
