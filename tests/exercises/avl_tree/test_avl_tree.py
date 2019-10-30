#!/usr/bin/env python3
"""
AVL tree test
"""


import pytest
from src.exercises.avl_tree import AVLTree


class TestBalancedBinarySearchTreeMethods:
    @pytest.fixture(autouse=True)
    def setup_class(self):
        """Setting up"""
        self.avl_tree = AVLTree()

    def test_init(self):
        """Testing __init__() method"""
        assert self.avl_tree.root is None
        self.avl_tree.put(30, "a")
        assert self.avl_tree.root is not None

    def test_len(self):
        """Testing __len__() method"""
        assert self.avl_tree.size() == 0
        self.avl_tree.put(30, "a")
        assert len(self.avl_tree) == 1

    def test_auto_1(self):
        """Testing case 1: RL rotation"""
        self.avl_tree.put(30, "a")
        self.avl_tree.put(50, "b")
        self.avl_tree.put(40, "c")
        assert self.avl_tree.root.key == 40
        assert self.avl_tree.root.balance == 0
        assert "30 40 50" == " ".join([str(x) for x in self.avl_tree])

    def test_auto_2(self):
        """Testing case 2: LR rotation"""
        self.avl_tree.put(50, "a")
        self.avl_tree.put(30, "b")
        self.avl_tree.put(40, "c")
        assert self.avl_tree.root.key == 40
        assert self.avl_tree.root.balance == 0
        assert "30 40 50" == " ".join([str(x) for x in self.avl_tree])

    def test_auto_3(self):
        """Testing case 3: L rotation"""
        self.avl_tree.put(50, "a")
        self.avl_tree.put(30, "b")
        self.avl_tree.put(70, "c")
        self.avl_tree.put(80, "c")
        self.avl_tree.put(60, "d")
        self.avl_tree.put(90, "e")
        assert self.avl_tree.root.key == 70
        assert self.avl_tree.root.balance == 0
        assert "30 50 60 70 80 90" == " ".join([str(x) for x in self.avl_tree])

    def test_auto_4(self):
        """Testing case 4: R rotation"""
        self.avl_tree.put(50, "a")
        self.avl_tree.put(30, "b")
        self.avl_tree.put(70, "c")
        self.avl_tree.put(10, "c")
        self.avl_tree.put(20, "d")
        self.avl_tree.put(5, "e")
        assert self.avl_tree.root.key == 20
        assert self.avl_tree.root.balance == 0
        assert "5 10 20 30 50 70" == " ".join([str(x) for x in self.avl_tree])

    def test_auto_5(self):
        """Testing case 4: RL rotation"""
        self.avl_tree.put(40, "a")
        self.avl_tree.put(30, "b")
        self.avl_tree.put(50, "c")
        self.avl_tree.put(45, "d")
        self.avl_tree.put(60, "e")
        self.avl_tree.put(43, "f")
        assert self.avl_tree.root.key == 45
        assert self.avl_tree.root.balance == 0
        assert self.avl_tree.root.child_left.key == 40
        assert self.avl_tree.root.child_left.balance == 0
        assert self.avl_tree.root.child_right.key == 50
        assert self.avl_tree.root.child_right.balance == 1
        assert "30 40 43 45 50 60" == " ".join([str(x) for x in self.avl_tree])

    def test_auto_6(self):
        """Testing case 6: LR rotation"""
        self.avl_tree.put(40, "a")
        self.avl_tree.put(30, "b")
        self.avl_tree.put(50, "c")
        self.avl_tree.put(10, "d")
        self.avl_tree.put(35, "e")
        self.avl_tree.put(37, "f")
        assert self.avl_tree.root.key == 35
        assert self.avl_tree.root.balance == 0
        assert self.avl_tree.root.child_left.key == 30
        assert self.avl_tree.root.child_left.balance == -1
        assert self.avl_tree.root.child_right.key == 40
        assert self.avl_tree.root.child_right.balance == 0
        assert "10 30 35 37 40 50" == " ".join([str(x) for x in self.avl_tree])


if __name__ == "__main__":
    pytest.main(["test_avl_tree.py"])
