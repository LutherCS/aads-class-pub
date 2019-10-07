#!/usr/bin/env python3
# encoding: UTF-8
"""
@author: Roman Yasinovskyy
@date: 2019
@module: project.bloomfilter
"""

import pathlib
import pytest
import toml
from src.exercises.bloomfilter import BloomFilter

THIS_DIR = pathlib.Path(".")
TEST_DIR = pathlib.Path("tests/exercises/bloomfilter/")
DATA_DIR = pathlib.Path("data/exercises/bloomfilter/")
FILE_PUBLIC = pathlib.Path("test_bloomfilter_public.toml")
FILE_SECRET = pathlib.Path("test_bloomfilter_secret.toml")

if "tests" not in THIS_DIR.parts:
    FILE_PUBLIC = THIS_DIR / TEST_DIR / FILE_PUBLIC
    FILE_SECRET = THIS_DIR / TEST_DIR / FILE_SECRET

all_test_cases = toml.load(FILE_PUBLIC)

TIME_LIMIT = 1
WORDS = [
    (v.get("data")[0], v.get("data")[1], v.get("expected"))
    for v in all_test_cases.get("case_public").get("success").values()
]

if FILE_SECRET.exists():
    all_test_cases.update(toml.load(FILE_SECRET))
    WORDS.extend(
        [
            (v.get("data")[0], v.get("data")[1], v.get("expected"))
            for v in all_test_cases.get("case_secret").get("success").values()
        ]
    )


@pytest.mark.timeout(TIME_LIMIT)
@pytest.mark.parametrize("dictionary, typos, expected", WORDS)
def test_bloomfilter(dictionary, typos, expected):
    """Testing the output"""
    bf = BloomFilter(250, 7)
    with open(DATA_DIR / pathlib.Path(dictionary)) as file_in:
        for word in file_in.readlines():
            bf.add(word.strip())
    count = 0
    with open(DATA_DIR / pathlib.Path(typos)) as file_in:
        for word in file_in.readlines():
            if word.strip() in bf:
                count += 1
    assert count <= expected


if __name__ == "__main__":
    pytest.main(["-v", "test_bloomfilter.py"])
