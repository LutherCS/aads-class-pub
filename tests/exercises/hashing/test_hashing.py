#!/usr/bin/env python3
"""
`hashing` testing

@authors: Roman Yasinovskyy
@version: 2021.9
"""

import importlib
import pathlib
import sys

import pytest
import toml

try:
    importlib.util.find_spec(".".join(pathlib.Path(__file__).parts[-3:-1]), "src")
except ModuleNotFoundError:
    sys.path.append(f"{pathlib.Path(__file__).parents[3]}/")
finally:
    from src.exercises.hashing import (
        hash_remainder,
        hash_mid_sqr,
        hash_folding,
        hash_str,
        hash_str_weighted,
    )

TIME_LIMIT = 1


def get_cases(category: str):
    with open(pathlib.Path(__file__).with_suffix(".toml")) as f:
        all_cases = toml.load(f)
        for case in all_cases[category]:
            yield (case.get("keys"), case.get("size"), case.get("expected"))


@pytest.mark.timeout(TIME_LIMIT)
@pytest.mark.parametrize("keys, size, expected", get_cases("simple_remainder"))
def test_simple_remainder(keys, size, expected):
    """Testing simple remainder hashing"""
    assert [hash_remainder(x, size) for x in keys] == expected


@pytest.mark.timeout(TIME_LIMIT)
@pytest.mark.parametrize("keys, size, expected", get_cases("mid_square"))
def test_mid_square(keys, size, expected):
    """Testing mid-square hashing"""
    assert [hash_mid_sqr(x, size) for x in keys] == expected


@pytest.mark.timeout(TIME_LIMIT)
@pytest.mark.parametrize("keys, size, expected", get_cases("folding"))
def test_hash_folding(keys, size, expected):
    """Testing folding hashing"""
    assert [hash_folding(x, size) for x in keys] == expected


@pytest.mark.timeout(TIME_LIMIT)
@pytest.mark.parametrize("keys, size, expected", get_cases("naive_string"))
def test_naive_string(keys, size, expected):
    """Testing string hashing"""
    assert [hash_str(x, size) for x in keys] == expected


@pytest.mark.timeout(TIME_LIMIT)
@pytest.mark.parametrize("keys, size, expected", get_cases("weighted_string"))
def test_weighted_string(keys, size, expected):
    """Testing weighted string hashing"""
    assert [hash_str_weighted(x, size) for x in keys] == expected


if __name__ == "__main__":
    pytest.main(["-v", __file__])
