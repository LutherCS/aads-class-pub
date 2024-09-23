#!/usr/bin/env python3
"""
`tictactoe` testing

@authors: Roman Yasinovskyy
@version: 2024.9
"""

import importlib
import pathlib
import sys
import tkinter
from turtle import RawTurtle
from typing import Generator

import pytest
import tomllib

try:
    importlib.util.find_spec(".".join(pathlib.Path(__file__).parts[-3:-1]), "src")
except ModuleNotFoundError:
    sys.path.append(f"{pathlib.Path(__file__).parents[3]}/")
finally:
    from src.projects.tictactoe import Board, MarkO, MarkX, minimax


TIME_LIMIT = 5


def get_cases(category: str, *attribs: str) -> Generator:
    """Get test cases from the TOML file"""
    with open(pathlib.Path(__file__).with_suffix(".toml"), "rb") as file:
        all_cases = tomllib.load(file)
        for case in all_cases[category]:
            yield tuple(case.get(a) for a in attribs)


@pytest.fixture(name="board0")
def fixture_board0():
    """An empty board"""
    root = tkinter.Tk()
    canvas = tkinter.Canvas(root)
    raw_t = RawTurtle(canvas)
    screen = raw_t.getscreen()
    board = Board(None, screen)
    board.reset()
    # root.destroy()
    return board


@pytest.fixture(name="board1")
def fixture_board1():
    """An empty board"""
    return Board()


@pytest.fixture(name="board2")
def fixture_board2():
    """Board of all 0"""
    root = tkinter.Tk()
    canvas = tkinter.Canvas(root)
    board = Board()
    for i in range(3):
        for j in range(3):
            board[i][j] = MarkO(canvas)
    root.destroy()
    return board


@pytest.fixture(name="board3")
def fixture_board3():
    """Board of all 0"""
    root = tkinter.Tk()
    canvas = tkinter.Canvas(root)
    board = Board()
    for i in range(3):
        for j in range(3):
            board[i][j] = MarkO(canvas)
    root.destroy()
    return board


@pytest.fixture(name="board4")
def fixture_board4():
    """Board of all X"""
    root = tkinter.Tk()
    canvas = tkinter.Canvas(root)
    board = Board()
    for i in range(3):
        for j in range(3):
            board[i][j] = MarkX(canvas)
    root.destroy()
    return board


def test_board_eq_01(board0: Board, board1: Board):
    """Testing the board equality"""
    assert board0 == board1


def test_board_eq_12(board1: Board, board2: Board):
    """Testing the board equality"""
    assert board1 != board2


def test_board_eq_23(board2: Board, board3: Board):
    """Testing the board equality"""
    assert board2 == board3


def test_board_eq_34(board3: Board, board4: Board):
    """Testing the board equality"""
    assert board3 != board4


def test_board_eval_1(board1: Board):
    """Testing the board valuation"""
    assert board1.eval() == 0


def test_board_eval_2(board2: Board, board3: Board):
    """Testing the board valuation"""
    assert board2.eval() == -1
    assert board3.eval() == -1


def test_board_eval_4(board4: Board):
    """Testing the board valuation"""
    assert board4.eval() == 1


def test_board_full_1(board1: Board):
    """Testing the board fulness"""
    assert not board1.full()


def test_board_full_2(board2: Board, board3: Board):
    """Testing the board fulness"""
    assert board2.full()
    assert board3.full()


def test_board_full_4(board4: Board):
    """Testing the board fulness"""
    assert board4.full()


def test_board_avail_1(board1: Board):
    """Testing the board availability"""
    assert board1.available() == [
        (0, 0),
        (0, 1),
        (0, 2),
        (1, 0),
        (1, 1),
        (1, 2),
        (2, 0),
        (2, 1),
        (2, 2),
    ]


def test_board_avail_2(board2: Board, board3: Board):
    """Testing the board availability"""
    assert board2.available() == []
    assert board3.available() == []


def test_board_avail_4(board4: Board):
    """Testing the board availability"""
    assert board4.available() == []


@pytest.mark.timeout(TIME_LIMIT)
def test_minimax_0c(board0: Board):
    """Testing the minimax"""
    assert minimax(1, board0, 3) == 0


@pytest.mark.timeout(TIME_LIMIT)
def test_minimax_0h(board0: Board):
    """Testing the minimax"""
    assert minimax(-1, board0, 3) == 0


@pytest.mark.timeout(TIME_LIMIT)
def test_minimax_2c(board3: Board):
    """Testing the minimax"""
    assert minimax(1, board3) == -1


@pytest.mark.timeout(TIME_LIMIT)
def test_minimax_2h(board3: Board):
    """Testing the minimax"""
    assert minimax(-1, board3) == -1


@pytest.mark.timeout(TIME_LIMIT)
def test_minimax_4c(board4: Board):
    """Testing the minimax"""
    assert minimax(1, board4) == 1


@pytest.mark.timeout(TIME_LIMIT)
def test_minimax_4h(board4: Board):
    """Testing the minimax"""
    assert minimax(-1, board4) == 1


@pytest.mark.timeout(TIME_LIMIT)
@pytest.mark.parametrize(
    "board, evaluation", get_cases("test_case", "board", "evaluation")
)
def test_minimax_param(board: Board, evaluation: int):
    """Testing the minimax"""
    root = tkinter.Tk()
    canvas = tkinter.Canvas(root)
    raw_t = RawTurtle(canvas)
    screen = raw_t.getscreen()
    tkboard = Board(None, screen)
    tkboard.reset()
    for i in range(3):
        for j in range(3):
            if board[i][j] == "O":
                tkboard[i][j] = MarkO(canvas)
            elif board[i][j] == "X":
                tkboard[i][j] = MarkX(canvas)
    # root.destroy()
    assert minimax(1, tkboard, 4) == evaluation


if __name__ == "__main__":
    pytest.main(["-v", __file__])
