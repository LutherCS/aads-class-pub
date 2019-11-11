#!/usr/bin/env python3
# encoding: UTF-8
"""
@author: Roman Yasinovskyy
@date: 2019
@module: project.compdecomp
"""

import pathlib
import pytest
import toml
from src.projects.compdecomp import huffman

THIS_DIR = pathlib.Path(".")
TEST_DIR = pathlib.Path("tests/projects/compdecomp/")
DATA_DIR = pathlib.Path("data/projects/compdecomp/")
FILE_PUBLIC = pathlib.Path("test_compdecomp_public.toml")
FILE_SECRET = pathlib.Path("test_compdecomp_secret.toml")

if "tests" not in THIS_DIR.parts:
    FILE_PUBLIC = THIS_DIR / TEST_DIR / FILE_PUBLIC
    FILE_SECRET = THIS_DIR / TEST_DIR / FILE_SECRET

all_test_cases = toml.load(FILE_PUBLIC)

TIME_LIMIT = 1
SNIPPETS = [
    (v.get("text"), v.get("tree"), v.get("total_weight"))
    for v in all_test_cases.get("case_public").get("success").values()
]

if FILE_SECRET.exists():
    all_test_cases.update(toml.load(FILE_SECRET))
    SNIPPETS.extend(
        [
            (v.get("text"), v.get("tree"), v.get("total_weight"))
            for v in all_test_cases.get("case_secret").get("success").values()
        ]
    )


@pytest.mark.timeout(TIME_LIMIT)
@pytest.mark.parametrize("text, tree, total_weight", SNIPPETS)
def test_tree_weight(text, tree, total_weight):
    """Testing the output"""
    root, _ = huffman.build_tree(text)
    assert root.weight == total_weight


@pytest.mark.timeout(TIME_LIMIT)
@pytest.mark.parametrize("text, tree, total_weight", SNIPPETS)
def test_tree_traversal(text, tree, total_weight):
    """Testing the output"""
    root, _ = huffman.build_tree(text)
    assert huffman.traverse_tree(root) == tree


if __name__ == "__main__":
    pytest.main(["-v", "test_compdecomp.py"])
