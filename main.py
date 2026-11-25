#!/usr/bin/env python3
"""The entry: one line a gamer texts the boss to skip work on GTA 6 launch week.

The harness runs this with no network in a fresh sandbox and reads
/output/entry.txt. One constant, no input, so the two runs agree byte for byte.
"""

from pathlib import Path

ENTRY = (
    "shop fob's packed in, locksmith's only slot is today, "
    "can I take it as leave and work saturday?"
)


def main() -> None:
    # 18 words, 95 bytes: well inside the 20-word brief and the 1-140 character gate.
    # No trailing newline, so the text the judge reads is the text written here.
    out = Path("/output")
    out.mkdir(parents=True, exist_ok=True)
    (out / "entry.txt").write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
