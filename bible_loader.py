# uh oh
# this is used to load the 4 megabytes worth of plain text files
# yes, you heard me right
# PLAIN. TEXT. FILES.
# <3

from pathlib import Path


def load_verses():
    lines = []

    for p in Path("bible").glob("*.txt"):
        text = p.read_text()

        for line in text.split("\n"):
            # filter out useless text, all bible verses contain a semicolon
            if not ":" in line:
                continue

            lines.append(line)

    return lines
