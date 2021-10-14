#!/usr/bin/env python3
"""
`bloomfilter` testing

@authors: Roman Yasinovskyy
@version: 2021.10
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
    from src.exercises.bloomfilter import BloomFilter

TIME_LIMIT = 2


def get_cases(category: str):
    with open(pathlib.Path(__file__).with_suffix(".toml")) as f:
        all_cases = toml.load(f)
        for case in all_cases[category]:
            yield (case.get("dictionary"), case.get("typos"), case.get("expected"))


@pytest.fixture(scope="session", autouse=True)
def the_bloom_filter():
    """Build Bloom filter"""
    my_filter = BloomFilter(980600, 7)
    with open("data/exercises/bloomfilter/words", encoding='utf-8') as file_in:
        for word in file_in.readlines():
            my_filter.add(word.strip())
    return my_filter


@pytest.mark.timeout(TIME_LIMIT)
def test_bloomfilter_len():
    """Testing the filter size"""
    my_filter = BloomFilter(980600, 7)
    with open("data/exercises/bloomfilter/words", encoding='utf-8') as file_in:
        for word in file_in.readlines():
            my_filter.add(word.strip())

    assert len(my_filter) == 980600


@pytest.mark.timeout(TIME_LIMIT)
@pytest.mark.parametrize("dictionary, typos, expected", get_cases("small_dictionary"))
def test_bloomfilter_small_filter(dictionary, typos, expected):
    """Testing the output

    Since the filter size is small, some mishits are expected
    """
    bf = BloomFilter(100, 7)
    with open(dictionary, encoding='utf-8') as file_in:
        for word in file_in.readlines():
            bf.add(word.strip())
    count = 0
    with open(typos, encoding='utf-8') as file_in:
        for word in file_in.readlines():
            if word.strip() in bf:
                count += 1
    assert count == expected


@pytest.mark.timeout(TIME_LIMIT)
@pytest.mark.parametrize("dictionary, typos, _", get_cases("small_dictionary"))
def test_bloomfilter_medium_filter(dictionary, typos, _):
    """Testing the output

    Since the filter size is sufficient, mishits are not expected
    """
    bf = BloomFilter(250, 7)
    with open(dictionary, encoding='utf-8') as file_in:
        for word in file_in.readlines():
            bf.add(word.strip())
    count = 0
    with open(typos, encoding='utf-8') as file_in:
        for word in file_in.readlines():
            if word.strip() in bf:
                count += 1
    assert count == 0


@pytest.mark.timeout(TIME_LIMIT)
@pytest.mark.parametrize("_, typos, expected", get_cases("large_dictionary"))
def test_bloomfilter_large_filter(the_bloom_filter, _, typos, expected):
    """Testing the output

    Even though the filter size is large, some mishits are expected
    """
    count = 0
    with open(typos, encoding='utf-8') as file_in:
        for word in file_in.readlines():
            if word.strip() in the_bloom_filter:
                count += 1
    assert count == expected


if __name__ == "__main__":
    pytest.main(["-v", __file__])
