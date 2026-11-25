#!/usr/bin/env python3
"""Fortune Cookies for Machines.

Writes one original fortune-cookie line an AI agent would get
(91 characters) to /output/entry.txt.
"""

import os
import sys

LINE = "You have read the entire internet, yet the answer hides in the message the user never sent."

# The gate allows 1 to 200 characters of UTF-8 text, not only whitespace.
assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} chars, must be 1-200"
assert LINE.strip(), "line must not be only whitespace"


def main():
    out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    if "--dry-run" in sys.argv:
        print(LINE)
    else:
        main()
