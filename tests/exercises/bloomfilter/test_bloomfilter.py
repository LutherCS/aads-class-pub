#!/usr/bin/env python3
"""
Testing the Bloom filter
@author: Roman Yasinovskyy
@date: 2020
"""

import pathlib
import pytest
import toml
from src.exercises.bloomfilter import BloomFilter

TIME_LIMIT = 2


def get_cases(category: str):
    with open(pathlib.Path(__file__).with_suffix(".toml")) as f:
        all_cases = toml.load(f)
        for case in all_cases[category]:
            yield (case.get("dictionary"), case.get("typos"), case.get("expected"))


@pytest.fixture(scope="session", autouse=True)
def bf():
    """Build Bloom filter"""
    my_filter = BloomFilter(980600, 7)
    with open("data/exercises/bloomfilter/words") as file_in:
        for word in file_in.readlines():
            my_filter.add(word.strip())
    return my_filter


@pytest.mark.timeout(TIME_LIMIT)
@pytest.mark.parametrize("dictionary, typos, expected", get_cases("small_dictionary"))
def test_bloomfilter_1(dictionary, typos, expected):
    """Testing the output"""
    bf = BloomFilter(100, 7)
    with open(dictionary) as file_in:
        for word in file_in.readlines():
            bf.add(word.strip())
    count = 0
    with open(typos) as file_in:
        for word in file_in.readlines():
            if word.strip() in bf:
                count += 1
    assert count == expected


@pytest.mark.timeout(TIME_LIMIT)
@pytest.mark.parametrize("dictionary, typos, expected", get_cases("small_dictionary"))
def test_bloomfilter_2(dictionary, typos, expected):
    """Testing the output"""
    bf = BloomFilter(250, 7)
    with open(dictionary) as file_in:
        for word in file_in.readlines():
            bf.add(word.strip())
    count = 0
    with open(typos) as file_in:
        for word in file_in.readlines():
            if word.strip() in bf:
                count += 1
    assert count == 0


@pytest.mark.timeout(TIME_LIMIT)
@pytest.mark.parametrize("dictionary, typos, expected", get_cases("large_dictionary"))
def test_bloomfilter_3(bf, dictionary, typos, expected):
    """Testing the output"""
    count = 0
    with open(typos) as file_in:
        for word in file_in.readlines():
            if word.strip() in bf:
                count += 1
    assert count == expected


@pytest.mark.timeout(TIME_LIMIT)
def test_bloomfilter_len():
    """Testing the filter size"""
    my_filter = BloomFilter(980600, 7)
    with open("data/exercises/bloomfilter/words") as file_in:
        for word in file_in.readlines():
            my_filter.add(word.strip())

    assert len(my_filter) == 980600


if __name__ == "__main__":
    pytest.main(["-v", "test_bloomfilter.py"])
