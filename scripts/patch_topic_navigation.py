#!/usr/bin/env python3
"""Add or replace ### Navigate footer on each topic file (prev / part index / next)."""
from __future__ import annotations

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from scaffold_topic_articles import (  # noqa: E402
    BOOK,
    CHAPTERS,
    chapter_to_part,
    load_all_chapter_titles,
    topic_navigation_footer,
)

NAV_BLOCK_RE = re.compile(r"\n\n---\n\n### Navigate\n\n.*\Z", re.DOTALL)


def main() -> None:
    titles = load_all_chapter_titles()
    root = BOOK.parent
    for ch in range(1, 77):
        part = chapter_to_part(ch)
        slug = CHAPTERS[ch][0]
        path = BOOK / f"part-{part:02d}" / f"{slug}.md"
        if not path.exists():
            print("Skip missing", path)
            continue
        text = path.read_text(encoding="utf-8")
        text = NAV_BLOCK_RE.sub("", text)
        text = text.rstrip() + topic_navigation_footer(ch, titles)
        path.write_text(text, encoding="utf-8")
        print("Patched", path.relative_to(root))


if __name__ == "__main__":
    main()
