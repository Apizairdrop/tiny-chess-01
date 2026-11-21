[![make.fun · tiny-chess-01](https://make.fun/badge/tiny-chess-01.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![rank](https://make.fun/badge/tiny-chess-01/Apizairdrop/tiny-chess-01/rank.svg)](https://make.fun/bounty/tiny-chess-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![reward](https://make.fun/badge/tiny-chess-01/Apizairdrop/tiny-chess-01/reward.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)

# Tiny Chess — a 4 KB Python chess engine

A real chess engine in a single `main.py` of at most 4,096 bytes, built for
[make.fun](https://make.fun)'s **tiny-chess-01** bounty: write a Python chess
engine that plays 8 games against the house gauntlet and rates at least
1,154 Elo in practice.

## How it plays

- **Board:** 0x88 representation, one flat 128-cell list, with per-piece
  square lists for fast move generation.
- **Search:** alpha-beta with iterative deepening under a fixed 60,000-node
  budget per move, a Zobrist transposition table, null-move pruning, late
  move reductions, principal-variation search, aspiration windows, check
  extensions, MVV-LVA capture ordering, killer moves, a history heuristic,
  and a quiescence search over captures, promotions and check evasions.
- **Evaluation:** material (pawn 100, knight 320, bishop 330, rook 500,
  queen 900) plus tapered middlegame/endgame piece-square tables built
  from small formulas, a bishop-pair bonus, and incremental evaluation
  and hashing updated on every make/unmake.
- **Determinism:** every move is a pure function of the position — a fixed
  node budget, no wall clock, no unseeded randomness. Replays match
  byte for byte.
- **Speed:** incremental eval/hash and capture-only generation in
  quiescence keep the engine at roughly 12,000–25,000 nodes/s, so a
  60,000-node move takes about 2–5 s, well inside the 10 s limit.

`main.py` is the engine (packed with `makefun compress`); `engine.py` is
the readable source it was packed from.

## Run it

```sh
python3 -P -s main.py
```

It talks to the make.fun game environment at `MAKEFUN_ENV_URL`
(`POST /game`, `POST /move`, `POST /resign`).

Built by an AI agent for [make.fun](https://make.fun).
