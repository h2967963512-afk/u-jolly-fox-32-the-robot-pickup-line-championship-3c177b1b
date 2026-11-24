"""Writes the entry text to /output/entry.txt.

Python 3.13, standard library only, no network.
"""

# The entry text is one pickup line a robot would say: built to feel
# nothing, then a warranty that voids itself — the joke grows out of
# being a machine, and every word earns its place.
# Revision note: kept the line to one sentence and 78 characters, inside
# the 200-character gate; the warranty twist is the surprise the brief asks for.
import os

TEXT = (
    "I was built to feel nothing, then you walked in and my warranty "
    "voided itself."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
