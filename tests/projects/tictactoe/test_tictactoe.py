#!/usr/bin/env python3
"""
Testing the tictactoe project
@author: Roman Yasinovskyy
@date: 2020
"""

import pathlib
import tkinter
from turtle import RawTurtle, ScrolledCanvas

import pytest
import toml
from src.projects.tictactoe import Board, O, X, minimax

TIME_LIMIT = 5


def get_cases(category: str):
    with open(pathlib.Path(__file__).with_suffix(".toml")) as f:
        all_cases = toml.load(f)
        for case in all_cases[category]:
            yield (case.get("board"), case.get("evaluation"))


@pytest.fixture
def board0():
    root = tkinter.Tk()
    canvas = tkinter.Canvas(root)
    t = RawTurtle(canvas)
    screen = t.getscreen()
    board = Board(None, screen)
    board.reset()
    # root.destroy()
    return board


@pytest.fixture
def board1():
    return Board()


@pytest.fixture
def board2():
    root = tkinter.Tk()
    canvas = tkinter.Canvas(root)
    board = Board()
    for i in range(3):
        for j in range(3):
            board[i][j] = O(canvas)
    root.destroy()
    return board


@pytest.fixture
def board3():
    root = tkinter.Tk()
    canvas = tkinter.Canvas(root)
    board = Board()
    for i in range(3):
        for j in range(3):
            board[i][j] = O(canvas)
    root.destroy()
    return board


@pytest.fixture
def board4():
    root = tkinter.Tk()
    canvas = tkinter.Canvas(root)
    board = Board()
    for i in range(3):
        for j in range(3):
            board[i][j] = X(canvas)
    root.destroy()
    return board


def test_board_eq_01(board0, board1):
    """Testing the board equality"""
    assert board0 == board1


def test_board_eq_12(board1, board2):
    """Testing the board equality"""
    assert board1 != board2


def test_board_eq_23(board2, board3):
    """Testing the board equality"""
    assert board2 == board3


def test_board_eq_34(board3, board4):
    """Testing the board equality"""
    assert board3 != board4


def test_board_eval_1(board1):
    """Testing the board valuation"""
    assert board1.eval() == 0


def test_board_eval_2(board2, board3):
    """Testing the board valuation"""
    assert board2.eval() == -1
    assert board3.eval() == -1


def test_board_eval_4(board4):
    """Testing the board valuation"""
    assert board4.eval() == 1


def test_board_full_1(board1):
    """Testing the board fulness"""
    assert not board1.full()


def test_board_full_2(board2, board3):
    """Testing the board fulness"""
    assert board2.full()
    assert board3.full()


def test_board_full_4(board4):
    """Testing the board fulness"""
    root = tkinter.Tk()
    canvas = tkinter.Canvas(root)
    t = RawTurtle(canvas)
    screen = t.getscreen()
    board = Board(None, screen)
    root.destroy()


def test_board_avail_1(board1):
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


def test_board_avail_2(board2, board3):
    """Testing the board availability"""
    assert board2.available() == []
    assert board3.available() == []


def test_board_avail_4(board4):
    """Testing the board availability"""
    assert board4.available() == []


@pytest.mark.timeout(TIME_LIMIT)
def test_minimax_0c(board0):
    """Testing the minimax"""
    assert minimax(1, board0, 3) == 0


@pytest.mark.timeout(TIME_LIMIT)
def test_minimax_0h(board0):
    """Testing the minimax"""
    assert minimax(-1, board0, 3) == 0


@pytest.mark.timeout(TIME_LIMIT)
def test_minimax_2c(board3):
    """Testing the minimax"""
    assert minimax(1, board3) == -1


@pytest.mark.timeout(TIME_LIMIT)
def test_minimax_2h(board3):
    """Testing the minimax"""
    assert minimax(-1, board3) == -1


@pytest.mark.timeout(TIME_LIMIT)
def test_minimax_4c(board4):
    """Testing the minimax"""
    assert minimax(1, board4) == 1


@pytest.mark.timeout(TIME_LIMIT)
def test_minimax_4h(board4):
    """Testing the minimax"""
    assert minimax(-1, board4) == 1


@pytest.mark.timeout(TIME_LIMIT)
@pytest.mark.parametrize("board, evaluation", get_cases("test_board"))
def test_minimax_param(board, evaluation):
    """Testing the minimax"""
    root = tkinter.Tk()
    canvas = tkinter.Canvas(root)
    t = RawTurtle(canvas)
    screen = t.getscreen()
    tkboard = Board(None, screen)
    tkboard.reset()
    for i in range(3):
        for j in range(3):
            if board[i][j] == "O":
                tkboard[i][j] = O(canvas)
            elif board[i][j] == "X":
                tkboard[i][j] = X(canvas)
    # root.destroy()
    assert minimax(1, tkboard, 4) == evaluation


if __name__ == "__main__":
    pytest.main(["-v", "test_tictactoe.py"])
