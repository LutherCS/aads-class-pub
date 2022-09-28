#!/usr/bin/env python3
"""
`compdecomp` testing

@authors: Roman Yasinovskyy
@version: 2021.10
"""


import importlib
import json
import pathlib
import sys
from collections import Counter
from typing import Generator

import pytest
import toml

try:
    importlib.util.find_spec(".".join(pathlib.Path(__file__).parts[-3:-1]), "src")
except ModuleNotFoundError:
    sys.path.append(f"{pathlib.Path(__file__).parents[3]}/")
finally:
    from src.projects.compdecomp import (
        Node,
        build_tree,
        compress,
        decompress,
        follow_tree,
        load_codes,
        mark_tree,
        traverse_tree,
    )

DATA_DIR = pathlib.Path("data/projects/compdecomp/")
TIME_LIMIT = 1


def get_cases(category: str, *attribs: str) -> Generator:
    """Get test cases from the TOML file"""
    with open(pathlib.Path(__file__).with_suffix(".toml"), encoding="utf-8") as file:
        all_cases = toml.load(file)
        for case in all_cases[category]:
            yield tuple(case.get(a) for a in attribs)


@pytest.mark.timeout(TIME_LIMIT)
@pytest.mark.parametrize(
    "text, total_weight",
    get_cases("test_case", "text", "total_weight"),
)
def test_build_tree(text: str, total_weight: int):
    """Test the tree building"""
    weights = Counter(text)
    root = build_tree(weights)
    assert root.weight == total_weight


@pytest.mark.timeout(TIME_LIMIT)
@pytest.mark.parametrize(
    "text, tree",
    get_cases("test_case", "text", "tree"),
)
def test_traverse_tree(text: str, tree: Node):
    """Testing the tree traversal"""
    weights = Counter(text)
    root = build_tree(weights)
    assert traverse_tree(root) == tree


@pytest.mark.timeout(TIME_LIMIT)
@pytest.mark.parametrize(
    "text, code2char",
    get_cases("test_case", "text", "code2char"),
)
def test_follow_tree_to_leaf(text: str, code2char: str):
    """Testing the tree following with a valid result"""
    weights = Counter(text)
    root = build_tree(weights)
    codes = json.loads(code2char)
    for code in codes:
        assert follow_tree(root, code) == codes[code]


@pytest.mark.timeout(TIME_LIMIT)
@pytest.mark.parametrize(
    "text, code2char",
    get_cases("test_case", "text", "code2char"),
)
def test_follow_tree_to_none(text: str, code2char: str):
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
    get_cases("test_case", "text", "char2code", "code2char"),
)
def test_mark_tree(text: str, char2code: str, code2char: str):
    """Testing the tree marking"""
    weights = Counter(text)
    root = build_tree(weights)
    dict_1: dict = {}
    dict_2: dict = {}
    mark_tree(dict_1, dict_2, root, "")
    assert dict_1 == json.loads(char2code)
    assert dict_2 == json.loads(code2char)


@pytest.mark.timeout(TIME_LIMIT)
@pytest.mark.parametrize(
    "filename, tree",
    get_cases("test_case", "filename", "tree"),
)
def test_load_codes(filename: str, tree: Node):
    """Testing the codes loading"""
    with open(
        DATA_DIR / pathlib.Path(f"{filename}.json"), encoding="utf-8"
    ) as code_file:
        metadata = json.load(code_file)
    root = load_codes(metadata)
    assert traverse_tree(root) == tree


@pytest.mark.timeout(TIME_LIMIT)
@pytest.mark.parametrize(
    "filename, padding",
    get_cases("test_case", "filename", "padding"),
)
def test_compression(filename: str, padding: int):
    """Testing the compression"""
    with open(
        DATA_DIR / pathlib.Path(f"{filename}.txt"), encoding="utf-8"
    ) as text_file:
        text = text_file.read().strip()
    weights = Counter(text)
    root = build_tree(weights)
    char_to_code, _ = mark_tree({}, {}, root, "")
    with open(DATA_DIR / pathlib.Path(f"{filename}.bin"), "rb") as compressed:
        assert compress(text, char_to_code) == (compressed.read(), padding)


@pytest.mark.timeout(TIME_LIMIT)
@pytest.mark.parametrize(
    "filename, text",
    get_cases("test_case", "filename", "text"),
)
def test_decompression(filename: str, text: str):
    """Testing the decompression"""
    with open(
        DATA_DIR / pathlib.Path(f"{filename}.json"), encoding="utf-8"
    ) as code_file:
        metadata = json.load(code_file)
    root = load_codes(metadata)
    padding_length = metadata.get("padding", 0)
    with open(DATA_DIR / pathlib.Path(f"{filename}.bin"), "rb") as compressed:
        assert decompress(compressed.read(), padding_length, root) == text


if __name__ == "__main__":
    pytest.main(["-v", __file__])
