#!/usr/bin/env python3
# encoding: UTF-8
"""
@author: Roman Yasinovskyy
@date: 2019
@module: exercises.trees
"""

import pathlib
import pytest
import toml
from src.exercises.trees.traversal import get_preorder

THIS_DIR = pathlib.Path(".")
TEST_DIR = pathlib.Path("tests/exercises/trees/")
FILE_PUBLIC = pathlib.Path("test_traversal_public.toml")
FILE_SECRET = pathlib.Path("test_traversal_secret.toml")

if "tests" not in THIS_DIR.parts:
    FILE_PUBLIC = THIS_DIR / TEST_DIR / FILE_PUBLIC
    FILE_SECRET = THIS_DIR / TEST_DIR / FILE_SECRET

ALL_TEST_CASES = toml.load(FILE_PUBLIC)

TIME_LIMIT = 1
TRAVERSALS = [
    (v.get("data")[0], v.get("data")[1], v.get("expected"))
    for v in ALL_TEST_CASES.get("case_public").get("success").values()
]

if FILE_SECRET.exists() and FILE_SECRET.stat().st_size > 0:
    ALL_TEST_CASES.update(toml.load(FILE_SECRET))
    TRAVERSALS.extend(
        [
            (v.get("data")[0], v.get("data")[1], v.get("expected"))
            for v in ALL_TEST_CASES.get("case_secret").get("success").values()
        ]
    )


@pytest.mark.timeout(TIME_LIMIT)
@pytest.mark.parametrize("inorder, postorder, preorder", TRAVERSALS)
def test_traversal(inorder, postorder, preorder):
    """Testing the output"""
    assert get_preorder(inorder, postorder) == preorder


if __name__ == "__main__":
    pytest.main(["-v", "test_traversal.py"])
