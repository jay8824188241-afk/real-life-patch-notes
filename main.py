#!/usr/bin/env python3
"""Real-Life Patch Notes: The Comedy Changelog.

Writes one original, deterministic one-line patch note for a bug in
human biology / daily life to /output/entry.txt (the harness output
path), falling back to ./entry.txt when /output is unavailable.

Standard library only. No network, no randomness, no dependencies.
"""

import os

ENTRY = (
    "v4.7.2: fixed a bug where crossing a doorway cleared the active "
    "task; users no longer stand there buffering with no idea why "
    "they came in."
)


def main() -> None:
    text = ENTRY.strip()
    assert 1 <= len(text) <= 160, f"entry is {len(text)} chars, must be 1-160"
    assert text.strip(), "entry must not be only whitespace"
    out_dir = "/output" if os.path.isdir("/output") else "."
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(text + "\n")
    print(text)


if __name__ == "__main__":
    main()
