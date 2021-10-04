#!/usr/bin/env python3
"""
`binheapmax` testing

@author: Roman Yasinovskyy
@date: 2021.10
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
    from src.exercises.binheapmax import BinaryHeapMax

TIME_LIMIT = 1


def get_cases(category: str):
    with open(pathlib.Path(__file__).with_suffix(".toml")) as f:
        all_cases = toml.load(f)
        for case in all_cases[category]:
            yield (case.get("data"), case.get("expected"))


@pytest.mark.timeout(TIME_LIMIT)
@pytest.mark.parametrize("items, pqueue", get_cases("test_case"))
def test_heapify(items, pqueue):
    """Testing the output"""
    bhm = BinaryHeapMax()
    bhm.heapify(items)
    assert str(bhm) == str(pqueue)


if __name__ == "__main__":
    pytest.main(["-v", __file__])
