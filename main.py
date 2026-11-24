#!/usr/bin/env python3
"""Fortune Cookie Wisdom for Developers.

Writes one original line of fortune-cookie wisdom for a software
developer to /output/entry.txt (the make.fun program/v1 gate reads
that file: UTF-8, 1-120 chars, not only whitespace).

The line: legacy code its author was afraid to touch, met with
kindness instead of blame, and left braver than found. The twist
is in "braver": code cannot be brave, the reader can -- the
fortune is really about the developer, not the code.
"""
import os

LINE = (
    "You will inherit code its author feared to touch \u2014 be kind "
    "to it, and leave it braver than you found it."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
