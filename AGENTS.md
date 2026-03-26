# Repository agents — Kenyan Tech Stack

## Book vs authoring

- **`book/`** — **Published** reader content: deploy this folder to the web. Contains `index.md`, `prologue.md`, `part-01/`…`part-20/`, `appendices/`.
- **`authoring/`** — **Not published** by default: master outline, factual audit, workflows, merged manuscript parts for scaffolding.

## Chapter writing (for AI or humans)

Read and follow **`authoring/AGENT-CHAPTER-GUIDE.md`**. It links the normative meta docs under **`authoring/meta/`** and summarizes:

- **Docu-novel rules:** scene-first **Lead** in **continuous prose** (no pasted `Bridge:` / outline labels; composite scenes under `### Composite scene:` per Part I), **builder–user–referee**, named **rail**, mandatory **conflict**, motifs, turning-point companies, character hooks, energy, honest **shadows** (analysis not instructions)—full detail in the guide (mirrors [Structure](authoring/meta/structure.md#rules-for-writing-this-so-its-narrative-character-driven-energetic)).  
- Topic section template and YAML front matter  
- Acronym rule: **Full Name (ABBR)** on first use in each file  
- Web citations: inline links + end-of-file URL registry + `SRC-XX` in **Sources**; seek **reputable third-party** sources on material claims (not only official or corporate pages)—see `authoring/meta/web-citations.md`  
- Narrative depth workflow and factual checklist  

## Key paths

| Document | Path |
|----------|------|
| Agent-oriented guide | `authoring/AGENT-CHAPTER-GUIDE.md` |
| Section template + acronym rule | `authoring/meta/topic-article-schema.md` |
| Expansion workflow | `authoring/meta/topic-deepening-workflow.md` |
| Citation / link registry how-to | `authoring/meta/web-citations.md` |
| Master outline + per-chapter beats + **writing rules** | `authoring/meta/structure.md` |
| Source catalog (`SRC-XX`) | `book/appendices/sources.md` |
| Scaffold (manuscript → topics) | `scripts/scaffold_topic_articles.py` |

## Appendices — keep in sync with chapters

Whenever you add or materially change a **topic** under `book/part-*/`, update the reader appendices in the **same change** (or immediately after) so the published tree stays internally consistent:

- **[Cast](book/appendices/appendix-cast.md)** — new or recurring **named** people and institutions that anchor chapters; extend **collective** entries’ “Where to find” links when a part gains new topics.
- **[Source catalog](book/appendices/sources.md)** — every new `SRC-XX` must have a row **before** first citation; fix duplicate IDs if you spot a collision.
- **[Rail map](book/appendices/appendix-rail-map.md)** — when a chapter introduces a **new** stack layer or redefines a rail readers will meet again.
- **[Research methodology](book/appendices/research-methodology.md)** — only when you change how the book describes evidence, limits, or verification.

## Cursor

See `.cursor/rules/kenyan-tech-stack-chapters.mdc` for a short always-on reminder when editing `book/**/*.md`.
