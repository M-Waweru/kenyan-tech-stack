---
title: Topic deepening workflow
description: How to expand topic articles from outline → factual lede → full narrative with characters, events, and citations.
tags:
  - meta
  - workflow
---
# Topic deepening workflow

Use this when a chapter feels **too summary-like** or bullet-heavy. Goal: **Wikipedia-grade facts** + **magazine-grade scenes** (composites allowed if labelled) + **traceable sources**.

## Phase 1 — Inventory

1. Read the **Lead** and list every **claim that needs a home** later (dates, names, products).
2. Read [Structure](structure.md) for the matching chapter: **cold open**, **characters**, **conflict**, **bridge**—note anything not yet in the topic file.
3. Skim [Factual Rigor Audit](factual-rigor-audit.md) for this part.

## Phase 2 — Source pass (breadth first)

Collect **at least two independent source types** per major claim where possible—and **search deliberately** for strong third-party material, not only the first official page that answers the question.

1. **Map the claim** (who benefits from this narrative? what would disprove it?).
2. **Query for reputable outsiders**: national newspapers, regulator statistics, multilateral reports, academic work, wires—see [Web citations — Independent and third-party sources](web-citations.md#independent-and-third-party-sources-all-topics).
3. **Prefer overlap**: two sources that agree without copying the same press release beat one press release twice.

| Type | Examples |
|------|-----------|
| **Primary / official** | CBK, CA, company newsroom, Kenya Law, annual reports |
| **Industry body** | KBA banking history, association timelines |
| **Trade / quality press** | Nation, Standard, Business Daily, TechCrunch Africa-era, ITWeb Africa, regional business papers |
| **Academic** | Theses (UoN repo), SAI/ITU-style papers |
| **Tertiary (use with care)** | Wikipedia, oAfrica compilations—verify against primary |

Add new URLs to [Source Catalog](../../book/appendices/sources.md) as `SRC-XX` before citing in prose.

## Phase 3 — Outline the narrative spine

For each H2 section (Context, History, …):

1. **One paragraph** answering *what happened*.
2. **One paragraph** answering *who paid, who built, who suffered*.
3. **One paragraph** answering *why the next layer of the stack depended on this*.

Avoid naked bullet lists in body text; if you need a list, **introduce it** and **close it** with interpretation.

## Phase 4 — Characters and scenes

- **Named people** only when documented (press, books, official bios). Add them to [Cast](../../book/appendices/appendix-cast.md) when they become recurring.
- **Composite characters** (“a branch operations manager”, “a cybercafé attendant on Tom Mboya Street”) are fine for **atmosphere** if you do **not** imply a single real individual. Prefer **documented settings** (night shift, payroll cut-off, café price board). Put labelled composites under **`### Composite scene: [title]`** with an optional italic *Composite, grounded in…* line—same pattern as `book/part-01/01-banking-in-the-dark.md`. Do **not** tag the entire Lead with `*Composite.*` or paste **`Bridge:`** from the outline into the chapter.
- **One scene per 1–2k words** is enough; do not turn every section into fiction.

## Phase 5 — Citation hygiene

- Prefer **clickable markdown links** in body prose (see [Topic article schema — Inline citations](topic-article-schema.md#inline-citations-web-edition)); keep `SRC-XX` IDs in the chapter **Sources** list and in [Source Catalog](../../book/appendices/sources.md).
- After rewriting, **grep** the file for years and names; every **surprising** claim should touch a source.
- Where a claim is **high-stakes** (money, crime, health of the stack, exclusivity), check that at least one citation is **third-party reputable**—not only a vendor, ministry slogan, or single insider—unless no such source exists (then say so lightly).
- Update the **Sources** section at the bottom with anything new, and maintain the file’s **link reference registry** (URL targets at end of file).

## Phase 6 — Sync and safety

- **Canonical** text lives in `book/part-NN/*.md`. If you still use `authoring/manuscript/part-*.md` for merges, paste back or avoid running `scripts/scaffold_topic_articles.py` until merged.
- Re-run `scripts/patch_topic_navigation.py` only if you changed file boundaries or titles (usually unnecessary).

## Quick checklist before you call a chapter “done”

- [ ] Lead still reads as a **tight summary** (facts + stakes), not only story.
- [ ] History has **chronology** and **at least two human-scale anchors** (named or composite).
- [ ] Setbacks / controversies are **honest** and sourced where factual.
- [ ] **See also** links to adjacent topics in the stack.
- [ ] New `SRC-XX` rows exist in the catalog.
- [ ] Body prose uses **clickable links** (not bare `SRC-XX` in parentheses); **link reference registry** at end of file matches every `[key]` used. See **[Web citations](web-citations.md)**.
- [ ] **Third-party pass:** material claims are supported by **independent** sources where available—not only official or corporate pages ([Web citations — Independent sources](web-citations.md#independent-and-third-party-sources-all-topics)).
- [ ] **Acronyms**: on first use in the file, **full name (ABBR)**—see [Topic article schema — Acronyms](topic-article-schema.md#acronyms-and-initialisms).

---

← [Topic article schema](topic-article-schema.md) · [**Web citations**](web-citations.md) · [**Book home**](../../book/index.md) · [Factual rigor audit](factual-rigor-audit.md) →
