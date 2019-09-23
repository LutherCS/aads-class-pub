#!/usr/bin/env python3
# encoding: UTF-8
"""
@author: Roman Yasinovskyy
@date: 2019
@module: exercises.binheapmax
"""

import pathlib
import pytest
import toml
from src.exercises.binheapmax import BinaryHeapMax

THIS_DIR = pathlib.Path(".")
TEST_DIR = pathlib.Path("tests/exercises/binheapmax/")
FILE_PUBLIC = pathlib.Path("test_binheapmax_public.toml")
FILE_SECRET = pathlib.Path("test_binheapmax_secret.toml")

if "tests" not in THIS_DIR.parts:
    FILE_PUBLIC = THIS_DIR / TEST_DIR / FILE_PUBLIC
    FILE_SECRET = THIS_DIR / TEST_DIR / FILE_SECRET

ALL_TEST_CASES = toml.load(FILE_PUBLIC)

TIME_LIMIT = 1
INPUTS = [
    (v.get("data"), v.get("expected"))
    for v in ALL_TEST_CASES.get("case_public").get("success").values()
]

if FILE_SECRET.exists() and FILE_SECRET.stat().st_size > 0:
    ALL_TEST_CASES.update(toml.load(FILE_SECRET))
    INPUTS.extend(
        [
            (v.get("data"), v.get("expected"))
            for v in ALL_TEST_CASES.get("case_secret").get("success").values()
        ]
    )


@pytest.mark.timeout(TIME_LIMIT)
@pytest.mark.parametrize("items, pqueue", INPUTS)
def test_traversal(items, pqueue):
    """Testing the output"""
    bhm = BinaryHeapMax()
    bhm.heapify(items)
    assert str(bhm) == str(pqueue)


if __name__ == "__main__":
    pytest.main(["-v", "test_traversal.py"])
