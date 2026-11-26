#!/usr/bin/env python3
"""Worst pizza topping pitch for make.fun.

The program prints one funny sales line for the worst pizza topping
imaginable and writes that same line to the entry file the grader reads.
It uses only the standard library, takes no input, and always produces
the exact same line, so every run is byte-identical.
"""

import os

# The pitch: the topping is a whole second pizza, sold as an upgrade.
# One sentence, one line, well under the 200-character gate.
LINE = (
    "New topping: a whole second pizza on your pizza, "
    "twice the crust, twice the regret, and yes, we charge extra for it."
)

MAX_CHARS = 200


def entry_line():
    """Return the single entry line, checked against the gate."""
    line = LINE.strip()
    if not line:
        raise ValueError("entry line is empty")
    if "\n" in line or "\r" in line:
        raise ValueError("entry line must be a single line")
    if len(line) > MAX_CHARS:
        raise ValueError(
            "entry line is %d characters, over the %d limit"
            % (len(line), MAX_CHARS)
        )
    return line


def output_path():
    """Where the entry file goes: $OUTPUT_PATH, else /output/entry.txt."""
    explicit = os.environ.get("OUTPUT_PATH")
    if explicit:
        return explicit
    return "/output/entry.txt"


def main():
    os.umask(0o022)
    line = entry_line()
    path = output_path()
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(line + "\n")
    # The grader collects the file as another user, so the file itself
    # must be world-readable. Only the file is chmodded, never its
    # directory (the output directory is root-owned on the grader).
    os.chmod(path, 0o644)
    print(line)


if __name__ == "__main__":
    main()
