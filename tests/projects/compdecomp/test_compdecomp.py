#!/usr/bin/env python3
"""
Testing the compress/decompress project
@author: Roman Yasinovskyy
@date: 2020
"""

import json
import pathlib
from collections import Counter

import pytest
import toml
from src.projects.compdecomp import (
    build_tree,
    traverse_tree,
    follow_tree,
    mark_tree,
    compress,
    decompress,
    load_codes,
)

DATA_DIR = pathlib.Path("data/projects/compdecomp/")
TIME_LIMIT = 1


def get_cases(category: str, attribs: tuple):
    with open(pathlib.Path(__file__).with_suffix(".toml")) as f:
        all_cases = toml.load(f)
        for case in all_cases[category]:
            yield [case.get(a) for a in attribs]


@pytest.mark.timeout(TIME_LIMIT)
@pytest.mark.parametrize(
    "text, total_weight",
    get_cases("test_case", ("text", "total_weight")),
)
def test_build_tree(text, total_weight):
    """Test the tree building"""
    weights = Counter(text)
    root = build_tree(weights)
    assert root.weight == total_weight


@pytest.mark.timeout(TIME_LIMIT)
@pytest.mark.parametrize(
    "text, tree",
    get_cases("test_case", ("text", "tree")),
)
def test_traverse_tree(text, tree):
    """Testing the tree traversal"""
    weights = Counter(text)
    root = build_tree(weights)
    assert traverse_tree(root) == tree


@pytest.mark.timeout(TIME_LIMIT)
@pytest.mark.parametrize(
    "text, code2char",
    get_cases("test_case", ("text", "code2char")),
)
def test_follow_tree_to_leaf(text, code2char):
    """Testing the tree following with a valid result"""
    weights = Counter(text)
    root = build_tree(weights)
    codes = json.loads(code2char)
    for code in codes:
        assert follow_tree(root, code) == codes[code]


@pytest.mark.timeout(TIME_LIMIT)
@pytest.mark.parametrize(
    "text, code2char",
    get_cases("test_case", ("text", "code2char")),
)
def test_follow_tree_to_none(text, code2char):
    """Testing the tree following with no result"""
    weights = Counter(text)
    root = build_tree(weights)
    codes = json.loads(code2char)
    if "0" not in codes:
        assert follow_tree(root, "0") is None
    if "1" not in codes:
        assert follow_tree(root, "1") is None


@pytest.mark.timeout(TIME_LIMIT)
@pytest.mark.parametrize(
    "text, char2code, code2char",
    get_cases("test_case", ("text", "char2code", "code2char")),
)
def test_mark_tree(text, char2code, code2char):
    """Testing the tree marking"""
    weights = Counter(text)
    root = build_tree(weights)
    d1 = {}
    d2 = {}
    mark_tree(d1, d2, root, "")
    assert d1 == json.loads(char2code)
    assert d2 == json.loads(code2char)


@pytest.mark.timeout(TIME_LIMIT)
@pytest.mark.parametrize(
    "filename, tree",
    get_cases("test_case", ("filename", "tree")),
)
def test_load_codes(filename, tree):
    """Testing the codes loading"""
    with open(DATA_DIR / pathlib.Path(f"{filename}.json"), "r") as code_file:
        metadata = json.load(code_file)
    root = load_codes(metadata)
    assert traverse_tree(root) == tree


@pytest.mark.timeout(TIME_LIMIT)
@pytest.mark.parametrize(
    "filename, padding",
    get_cases("test_case", ("filename", "padding")),
)
def test_compression(filename, padding):
    """Testing the compression"""
    with open(DATA_DIR / pathlib.Path(f"{filename}.txt"), "r") as text_file:
        text = text_file.read().strip()
    weights = Counter(text)
    root = build_tree(weights)
    char_to_code, _ = mark_tree({}, {}, root, "")
    with open(
        pathlib.Path(f"data/projects/compdecomp/{filename}.bin"), "rb"
    ) as compressed:
        assert compress(text, char_to_code) == (compressed.read(), padding)


@pytest.mark.timeout(TIME_LIMIT)
@pytest.mark.parametrize(
    "filename, text",
    get_cases("test_case", ("filename", "text")),
)
def test_decompression(filename, text):
    """Testing the decompression"""
    with open(DATA_DIR / pathlib.Path(f"{filename}.json"), "r") as code_file:
        metadata = json.load(code_file)
    root = load_codes(metadata)
    padding_length = metadata.get("padding", 0)
    with open(
        pathlib.Path(f"data/projects/compdecomp/{filename}.bin"), "rb"
    ) as compressed:
        assert decompress(compressed.read(), padding_length, root) == text


if __name__ == "__main__":
    pytest.main(["-v", "test_compdecomp.py"])
