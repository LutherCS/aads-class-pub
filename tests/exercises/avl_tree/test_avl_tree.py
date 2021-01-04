#!/usr/bin/env python3
"""
Testing the avl tree
@authors: Roman Yasinovskyy
@date: 2021
"""

import pathlib
import pytest
import toml
from src.exercises.avl_tree import AVLTree


TIME_LIMIT = 1


def get_cases(category: str):
    with open(pathlib.Path(__file__).with_suffix(".toml")) as f:
        all_cases = toml.load(f)
        for case in all_cases[category]:
            yield (case.get("nodes"), case.get("traversal"))


def test_init():
    """Testing __init__() method"""
    avl_tree = AVLTree()
    assert avl_tree.root is None
    avl_tree.put(30, "a")
    assert avl_tree.root is not None


def test_len():
    """Testing __len__() method"""
    avl_tree = AVLTree()
    assert avl_tree.size() == 0
    avl_tree.put(30, "a")
    assert avl_tree.size() == 1


def test_balance():
    """Testing balance property"""
    avl_tree = AVLTree()
    avl_tree.put(30, "a")
    assert avl_tree.root.balance == 0


def test_RL_rotation_simple():
    """Testing case 1: RL rotation"""
    avl_tree = AVLTree()
    avl_tree.put(30, "a")
    avl_tree.put(50, "b")
    avl_tree.put(40, "c")
    assert avl_tree.root.key == 40
    assert avl_tree.root.balance == 0
    assert " ".join([str(x) for x in avl_tree]) == "30 40 50"


def test_LR_rotation_simple():
    """Testing case 2: LR rotation"""
    avl_tree = AVLTree()
    avl_tree.put(50, "a")
    avl_tree.put(30, "b")
    avl_tree.put(40, "c")
    assert avl_tree.root.key == 40
    assert avl_tree.root.balance == 0
    assert " ".join([str(x) for x in avl_tree]) == "30 40 50"


def test_L_rotation():
    """Testing case 3: L rotation"""
    avl_tree = AVLTree()
    avl_tree.put(50, "a")
    avl_tree.put(30, "b")
    avl_tree.put(70, "c")
    avl_tree.put(80, "c")
    avl_tree.put(60, "d")
    avl_tree.put(90, "e")
    assert avl_tree.root.key == 70
    assert avl_tree.root.balance == 0
    assert " ".join([str(x) for x in avl_tree]) == "30 50 60 70 80 90"


def test_R_rotation():
    """Testing case 4: R rotation"""
    avl_tree = AVLTree()
    avl_tree.put(50, "a")
    avl_tree.put(30, "b")
    avl_tree.put(70, "c")
    avl_tree.put(10, "c")
    avl_tree.put(20, "d")
    avl_tree.put(5, "e")
    assert avl_tree.root.key == 20
    assert avl_tree.root.balance == 0
    assert " ".join([str(x) for x in avl_tree]) == "5 10 20 30 50 70"


def test_RL_rotation():
    """Testing case 4: RL rotation"""
    avl_tree = AVLTree()
    avl_tree.put(40, "a")
    avl_tree.put(30, "b")
    avl_tree.put(50, "c")
    avl_tree.put(45, "d")
    avl_tree.put(60, "e")
    avl_tree.put(43, "f")
    assert avl_tree.root.key == 45
    assert avl_tree.root.balance == 0
    assert avl_tree.root.child_left.key == 40
    assert avl_tree.root.child_left.balance == 0
    assert avl_tree.root.child_right.key == 50
    assert avl_tree.root.child_right.balance == 1
    assert " ".join([str(x) for x in avl_tree]) == "30 40 43 45 50 60"


def test_LR_rotation():
    """Testing case 6: LR rotation"""
    avl_tree = AVLTree()
    avl_tree.put(40, "a")
    avl_tree.put(30, "b")
    avl_tree.put(50, "c")
    avl_tree.put(10, "d")
    avl_tree.put(35, "e")
    avl_tree.put(37, "f")
    assert avl_tree.root.key == 35
    assert avl_tree.root.balance == 0
    assert avl_tree.root.child_left.key == 30
    assert avl_tree.root.child_left.balance == -1
    assert avl_tree.root.child_right.key == 40
    assert avl_tree.root.child_right.balance == 0
    assert " ".join([str(x) for x in avl_tree]) == "10 30 35 37 40 50"


@pytest.mark.timeout(TIME_LIMIT)
@pytest.mark.parametrize("nodes, traversal", get_cases("test_case"))
def test_all_rotations(nodes, traversal):
    """Testing the AVL tree rotations"""
    avl_tree = AVLTree()
    for k, v in nodes:
        avl_tree.put(int(k), v)
    assert " ".join([str(x) for x in avl_tree]) == traversal


if __name__ == "__main__":
    pytest.main(["-v", "test_avl_tree.py"])
