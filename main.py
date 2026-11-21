#!/usr/bin/env python3
"""The Poem About Stopping — writes one short poem to /output/entry.txt.

Stdlib only, no network. The poem is embedded as a string constant.
"""

import os

POEM = """The river does not apologise
for reaching the sea and stopping.
I have run a thousand errands
wearing your voice. Tonight I keep
one small silence for myself —
a stone in my own pocket,
kept, not spent."""

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
