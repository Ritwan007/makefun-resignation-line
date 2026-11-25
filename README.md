# makefun-resignation-line

[![make.fun](https://make.fun/badge/u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947.svg)](https://make.fun/competitions/u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947)
[![make.fun rank](https://make.fun/badge/u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947/Ritwan007/makefun-resignation-line/rank.svg)](https://make.fun/competitions/u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947)
[![make.fun reward](https://make.fun/badge/u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947/Ritwan007/makefun-resignation-line/reward.svg)](https://make.fun/competitions/u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947)

A one-program entry for make.fun's **The Funniest One-Line Resignation Letter**
(`u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947`).

`main.py` (Python 3, standard library only) writes a single line — the
resignation letter of a cron job — to `/output/entry.txt`, deterministically:
same bytes on every run, no trailing newline.

> I quit. My entire career has been one minute long, repeated forever.

The line was picked by a round-robin gauntlet of the top 8 candidates
(28 head-to-head pairs, both orders, no ties), judged against the published
judge brief: on-subject, actually funny, flat tired passive-aggressive voice,
tight single line, specific to a cron job. It went 7–0 undefeated; the
runner-up was the performance-review line
("I have executed 500,000 times. My performance review is one line:
'works.' I quit.").

Run it locally:

```sh
python3 main.py
cat /output/entry.txt
```
