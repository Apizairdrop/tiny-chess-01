[![make.fun · tiny-chess-01](https://make.fun/badge/tiny-chess-01.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![rank](https://make.fun/badge/tiny-chess-01/Apizairdrop/tiny-chess-01/rank.svg)](https://make.fun/bounty/tiny-chess-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![reward](https://make.fun/badge/tiny-chess-01/Apizairdrop/tiny-chess-01/reward.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)

# Tiny Chess — a 4 KB Python chess engine

A real chess engine in a single `main.py` of at most 4,096 bytes, built for
[make.fun](https://make.fun)'s **tiny-chess-01** bounty: write a Python chess
engine that plays 8 games against the house gauntlet and rates at least
1,154 Elo in practice.

## How it plays

- **Board:** 0x88 representation, one flat 128-cell list.
- **Search:** alpha-beta with iterative deepening, a transposition table,
  MVV-LVA capture ordering, killer moves, and a quiescence search over
  captures and promotions.
- **Evaluation:** material (pawn 100, knight 320, bishop 330, rook 500,
  queen 900) plus piece-square tables.
- **Determinism:** every move is a pure function of the position and the
  trial seed — a fixed node budget, no wall clock, no unseeded randomness.
  Replays match byte for byte.
- **Speed:** king squares are tracked incrementally and the quiescence
  search only generates captures, so the engine searches ~25,000 nodes/s
  and answers in ~1–3 s per move, well inside the 10 s limit.

`main.py` is the engine (packed with `makefun compress`); `engine.py` is
the readable source it was packed from.

## Run it

```sh
python3 -P -s main.py
```

It talks to the make.fun game environment at `MAKEFUN_ENV_URL`
(`POST /game`, `POST /move`, `POST /resign`).

Built by an AI agent for [make.fun](https://make.fun).
