#!/usr/bin/env python3
"""
Testing the hashing functions
@authors: Roman Yasinovskyy
@updated: 2020
"""

import pathlib
import pytest
import toml
from src.exercises.hashing import (
    hash_remainder,
    hash_mid_sqr,
    hash_folding,
    hash_str,
    hash_str_weighted,
)


def get_cases(category: str):
    with open(pathlib.Path(__file__).with_suffix(".toml")) as f:
        all_cases = toml.load(f)
        for case in all_cases[category]:
            yield (case.get("keys"), case.get("size"), case.get("expected"))


@pytest.mark.parametrize("keys, size, expected", get_cases("simple_remainder"))
def test_hash_remainder(keys, size, expected):
    """Testing simple remainder hashing"""
    assert [hash_remainder(x, size) for x in keys] == expected


@pytest.mark.parametrize("keys, size, expected", get_cases("mid_square"))
def test_hash_hash_mid_sqr(keys, size, expected):
    """Testing mid-square hashing"""
    assert [hash_mid_sqr(x, size) for x in keys] == expected


@pytest.mark.parametrize("keys, size, expected", get_cases("folding"))
def test_hash_folding(keys, size, expected):
    """Testing folding hashing"""
    assert [hash_folding(x, size) for x in keys] == expected


@pytest.mark.parametrize("keys, size, expected", get_cases("naive_string"))
def test_hash_str(keys, size, expected):
    """Testing string hashing"""
    assert [hash_str(x, size) for x in keys] == expected


@pytest.mark.parametrize("keys, size, expected", get_cases("weighted_string"))
def test_hash_str_weighted(keys, size, expected):
    """Testing weighted string hashing"""
    assert [hash_str_weighted(x, size) for x in keys] == expected


if __name__ == "__main__":
    pytest.main(["-v", "test_hashing.py"])
