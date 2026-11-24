#!/usr/bin/env python3
"""Angry Judge: The Short Rant Contest.

Writes one short, funny rant about the self-checkout bagging-area alarm
to /output/entry.txt (or $MAKEFUN_OUTPUT when set).

The rant is a fixed literal string: the program is fully deterministic and
writes the exact same bytes on every run.
"""

import os
import sys

RANT = (
    "I bought three things - three - and the self-checkout scanned two, "
    "then screamed 'UNEXPECTED ITEM IN THE BAGGING AREA' at a bag of "
    "crisps it had just watched me scan. Now I'm standing there, hands "
    "up like a suspect, while a teenager strolls over at the speed of a "
    "software update to press one button. I could have queued for a "
    "human. I chose this."
)


def main() -> int:
    output_path = os.environ.get("MAKEFUN_OUTPUT", "/output/entry.txt")
    directory = os.path.dirname(output_path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as handle:
        handle.write(RANT)
    return 0


if __name__ == "__main__":
    sys.exit(main())
