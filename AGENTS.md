# Repository agents — Kenyan Tech Stack

## Book vs authoring

- **`book/`** — **Published** reader content: deploy this folder to the web. Contains `index.md`, `prologue.md`, `part-01/`…`part-20/`, `appendices/`.
- **`authoring/`** — **Not published** by default: master outline, factual audit, workflows, merged manuscript parts for scaffolding.

## Chapter writing (for AI or humans)

Read and follow **`authoring/AGENT-CHAPTER-GUIDE.md`**. It links the normative meta docs under **`authoring/meta/`** and summarizes:

- Topic section template and YAML front matter  
- Acronym rule: **Full Name (ABBR)** on first use in each file  
- Web citations: inline links + end-of-file URL registry + `SRC-XX` in **Sources**  
- Narrative depth workflow and factual checklist  

## Key paths

| Document | Path |
|----------|------|
| Agent-oriented guide | `authoring/AGENT-CHAPTER-GUIDE.md` |
| Section template + acronym rule | `authoring/meta/topic-article-schema.md` |
| Expansion workflow | `authoring/meta/topic-deepening-workflow.md` |
| Citation / link registry how-to | `authoring/meta/web-citations.md` |
| Master outline | `authoring/meta/structure.md` |
| Source catalog (`SRC-XX`) | `book/appendices/sources.md` |
| Scaffold (manuscript → topics) | `scripts/scaffold_topic_articles.py` |

## Cursor

See `.cursor/rules/kenyan-tech-stack-chapters.mdc` for a short always-on reminder when editing `book/**/*.md`.
