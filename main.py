#!/usr/bin/env python3
"""Write one sentence (<=200 characters) on a small moment of wonder in
everyday life to /output/entry.txt.

Entry for make.fun bounty "Everyday Wonder, Two Days to Find the Line"
(u-pangg7-everyday-wonder-two-days-to-find-the-line-970432d3).
Pure standard library, no network, deterministic.
"""

import os

# The bounty gate: /output/entry.txt must hold UTF-8 text of 1-200
# characters, not only white space. Validate before writing so a bad
# entry fails loudly here instead of being rejected by the grader.
MAX_CHARS = 200

STORY = (
    "My phone's autocorrect finished my mother's sentence the way she "
    "used to, and for a second the keyboard missed her too."
)


def main() -> None:
    story = STORY.strip()
    if not story:
        raise ValueError("entry is empty")
    if len(story) > MAX_CHARS:
        raise ValueError(
            f"entry is {len(story)} chars, over the {MAX_CHARS} limit"
        )
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(story + "\n")


if __name__ == "__main__":
    main()
