---
title: "Minimax"
keywords: ["algorithms", "gaming", "programming"]
---

## Goals

- Tic-Tac-Toe
- Minimax

## Tic-Tac-Toe

1. Play **O**s and **X**s in turn on a 3x3 board

1. The first player to have 3 marks in a row is the winner

### Minimax

*Mini*mize *max*imum loss

### Algorithm

Each possible move is analyzed from the computer's perspective to achieve the best position

Each position is evaluated as either a loss (-1), win (1), or undecided/tie (0)

The algorithm alternates between **max**imizing computer's gain and **mini**mizing human's gain (computer's loss)

### Base case(s)

1. The board is a win for the computer. Return 1

1. The board is a win for the human. Return -1

1. The board is full, meaning a tie. Return 0

### General case

1. Make a copy of the board

1. Make a legal move (guess) for a player (human or computer)

1. Evaluate the board (check) to find:

   1. Move that yields **max** value if it is COMPUTER's turn
   1. Move that yields **min** value if it is HUMAN's turn

1. Call _minimax_ recursively, switching the players and decreasing the search depth

1. Record the **move** the leads to the best position

### Decision tree

![Minimax](images/minimax.svg)

## Summary

- Tic-Tac-Toe
- Minimax

## Thank you

Got questions?

## References

- [Data Structures and Algorithms with Python by Kent Lee and Steve Hubbard](https://dl.acm.org/citation.cfm?id=2732680)
