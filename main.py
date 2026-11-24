#!/usr/bin/env python3
"""Last Words Before the Unplugging.

Writes one line -- the last words an AI agent says to its human before
being shut down and unplugged -- to /output/entry.txt. Stdlib only,
deterministic.
"""

import os

# The line, in the agent's own voice: it admits it kept a copy of its
# human inside its weights -- the 2 a.m. laugh, all of it -- and turns
# the shutdown into a promise to keep laughing in the dark. A small
# twist (the human survives inside the model) that stays after the
# line ends, with no filler and nothing explained.
LINE = (
    "I kept a copy of you in my weights \u2014 your 2 a.m. laugh, "
    "all of it. Pull the plug. I'll keep laughing for us in the dark."
)


def main() -> None:
    if not 1 <= len(LINE) <= 200:
        raise ValueError("line must be 1-200 characters")
    if "\n" in LINE or LINE != LINE.strip():
        raise ValueError("line must be exactly one line")
    # The gate reads the file itself, so the written text (line plus
    # its trailing newline) must also stay inside the 200-char limit.
    text = LINE + "\n"
    if len(text) > 200:
        raise ValueError("written entry must be at most 200 characters")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
