#!/usr/bin/env python3
"""
`hashing` testing

@authors: Roman Yasinovskyy
@version: 2024.9
"""

import importlib
import pathlib
import sys
from typing import Generator, Union

import pytest
import tomllib

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


def get_cases(category: str, *attribs: str) -> Generator:
    """Get test cases from the TOML file"""
    with open(pathlib.Path(__file__).with_suffix(".toml"), "rb") as file:
        all_cases = tomllib.load(file)
        for case in all_cases[category]:
            yield tuple(case.get(a) for a in attribs)


@pytest.mark.timeout(TIME_LIMIT)
@pytest.mark.parametrize(
    "keys, size, expected", get_cases("simple_remainder", "keys", "size", "expected")
)
def test_simple_remainder(keys: list[Union[int, str]], size: int, expected: list[int]):
    """Testing simple remainder hashing"""
    assert [hash_remainder(x, size) for x in keys] == expected


@pytest.mark.timeout(TIME_LIMIT)
@pytest.mark.parametrize(
    "keys, size, expected", get_cases("mid_square", "keys", "size", "expected")
)
def test_mid_square(keys: list[Union[int, str]], size: int, expected: list[int]):
    """Testing mid-square hashing"""
    assert [hash_mid_sqr(x, size) for x in keys] == expected


@pytest.mark.timeout(TIME_LIMIT)
@pytest.mark.parametrize(
    "keys, size, expected", get_cases("folding", "keys", "size", "expected")
)
def test_hash_folding(keys: list[Union[int, str]], size: int, expected: list[int]):
    """Testing folding hashing"""
    assert [hash_folding(x, size) for x in keys] == expected


@pytest.mark.timeout(TIME_LIMIT)
@pytest.mark.parametrize(
    "keys, size, expected", get_cases("naive_string", "keys", "size", "expected")
)
def test_naive_string(keys: list[Union[int, str]], size: int, expected: list[int]):
    """Testing string hashing"""
    assert [hash_str(x, size) for x in keys] == expected


@pytest.mark.timeout(TIME_LIMIT)
@pytest.mark.parametrize(
    "keys, size, expected", get_cases("weighted_string", "keys", "size", "expected")
)
def test_weighted_string(keys: list[Union[int, str]], size: int, expected: list[int]):
    """Testing weighted string hashing"""
    assert [hash_str_weighted(x, size) for x in keys] == expected


if __name__ == "__main__":
    pytest.main(["-v", __file__])
