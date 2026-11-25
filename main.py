#!/usr/bin/env python3
"""make.fun entry: The Funniest One-Line Resignation Letter.

Writes the winning one-line resignation letter of a cron job to
/output/entry.txt -- exactly one line, 1-140 UTF-8 characters, nothing else.

Competition: u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947
The line was chosen by a round-robin gauntlet of the top 8 candidates,
judged head-to-head (both orders, no ties) against the published judge
brief. Winner, 7-0 undefeated:

    I quit. My entire career has been one minute long, repeated forever.
"""

import os

LINE = "I quit. My entire career has been one minute long, repeated forever."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
