#!/usr/bin/env python3
"""
`binheapmax` testing

@authors: Roman Yasinovskyy
@version: 2022.9
"""

import importlib
import pathlib
import sys
from typing import Generator, Union

import pytest
import toml

try:
    importlib.util.find_spec(".".join(pathlib.Path(__file__).parts[-3:-1]), "src")
except ModuleNotFoundError:
    sys.path.append(f"{pathlib.Path(__file__).parents[3]}/")
finally:
    from src.exercises.binheapmax import BinaryHeapMax

TIME_LIMIT = 1


def get_cases(category: str, *attribs: str) -> Generator:
    """Get test cases from the TOML file"""
    with open(pathlib.Path(__file__).with_suffix(".toml"), encoding="utf-8") as file:
        all_cases = toml.load(file)
        for case in all_cases[category]:
            yield tuple(case.get(a) for a in attribs)


@pytest.mark.timeout(TIME_LIMIT)
@pytest.mark.parametrize("items, pqueue", get_cases("test_heapify", "data", "expected"))
def test_heapify(items: list[Union[int, str]], pqueue: list[Union[int, str]]):
    """Testing the heap after list is heapified"""
    bhm = BinaryHeapMax()
    bhm.heapify(items)
    assert str(bhm) == str(pqueue)


@pytest.mark.timeout(TIME_LIMIT)
@pytest.mark.parametrize("items, pqueue", get_cases("test_add", "data", "expected"))
def test_add(items: list[Union[int, str]], pqueue: list[Union[int, str]]):
    """Testing the heap after items are added"""
    bhm = BinaryHeapMax()
    for i in items:
        bhm.add(i)
    assert str(bhm) == str(pqueue)


@pytest.mark.timeout(TIME_LIMIT)
@pytest.mark.parametrize("items, pqueue", get_cases("test_remove", "data", "expected"))
def test_remove(items: list[Union[int, str]], pqueue: list[Union[int, str]]):
    """Testing the heap after items are removed"""
    bhm = BinaryHeapMax()
    bhm.heapify(items)
    bhm.remove()
    assert str(bhm) == str(pqueue)


if __name__ == "__main__":
    pytest.main(["-v", __file__])
