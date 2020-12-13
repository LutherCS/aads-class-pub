#!/usr/bin/env python3
"""
Testing the tree traversal
@authors: Roman Yasinovskyy
@date: 2020
"""

import pathlib
import pytest
import toml
from src.exercises.trees.traversal import get_preorder

TIME_LIMIT = 1


def get_cases(category: str):
    with open(pathlib.Path(__file__).with_suffix(".toml")) as f:
        all_cases = toml.load(f)
        for case in all_cases[category]:
            yield (case.get("inorder"), case.get("postorder"), case.get("preorder"))


@pytest.mark.timeout(TIME_LIMIT)
@pytest.mark.parametrize("inorder, postorder, preorder", get_cases("test_case"))
def test_traversal(inorder, postorder, preorder):
    """Testing the output"""
    assert get_preorder(inorder, postorder) == preorder


if __name__ == "__main__":
    pytest.main(["-v", "test_traversal.py"])
