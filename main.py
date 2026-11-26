#!/usr/bin/env python3
"""One Line to Your Younger Self - make.fun entry.

Writes a single line to /output/entry.txt.
"""

SETUP = "Kid, that degree won't open a single door \u2014 "
PUNCH = "your muddy boots will, so stop polishing the CV and wear them out."


def assemble() -> str:
    return SETUP + PUNCH


def validate(line: str) -> str:
    if not line or not line.strip():
        raise ValueError("entry is empty")
    if len(line) > 200:
        raise ValueError(f"entry is {len(line)} chars, over the 200-char limit")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    return line


def main() -> None:
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(validate(assemble()))


if __name__ == "__main__":
    main()
