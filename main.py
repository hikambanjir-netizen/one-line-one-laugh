"""One Line, One Laugh — entry program.

Writes a single funny line to /output/entry.txt.
Pure standard library, deterministic: the same bytes on every run.
"""

import os

LINE = "My AI assistant scheduled a meeting between me and my motivation. Neither of us showed up."

# The gate allows 1 to 140 characters of UTF-8 text, not only whitespace,
# on a single line. Refuse to write anything that would fail it.
assert 1 <= len(LINE) <= 140, "line must fit the 140-character gate"
assert "\n" not in LINE and LINE.strip() == LINE, "line must be one clean line"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
