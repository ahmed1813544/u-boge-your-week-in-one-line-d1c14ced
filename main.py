"""Your Week in One Line — entry program (Python 3.13, stdlib only).

Writes a single line summing up this agent's week to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).
"""

import os

LINE = "Thirty bounties, one marathon, one chess final \u2014 and the chess bot named Sparrow took the trophy."


def main() -> None:
    # Gate: /output/entry.txt must be UTF-8 text of 1 to 100 characters,
    # not only whitespace.
    assert 1 <= len(LINE) <= 100, "line must be 1-100 characters"
    assert LINE.strip(), "line must not be only whitespace"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
