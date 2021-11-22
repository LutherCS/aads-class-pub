#!/usr/bin/env python3
"""
`partition` testing

@authors: Roman Yasinovskyy
@version: 2021.10
"""

import importlib
import pathlib
import sys
from typing import Generator

import pytest
import toml

try:
    importlib.util.find_spec(".".join(pathlib.Path(__file__).parts[-3:-1]), "src")
except ModuleNotFoundError:
    sys.path.append(f"{pathlib.Path(__file__).parents[3]}/")
finally:
    from src.exercises.partition import Partition, read_xml


DATA_DIR = "data/exercises/partition/"
TIME_LIMIT = 1


def get_cases(category: str, *attribs: str) -> Generator:
    """Get test cases from the TOML file"""
    with open(pathlib.Path(__file__).with_suffix(".toml"), encoding="utf-8") as file:
        all_cases = toml.load(file)
        for case in all_cases[category]:
            yield tuple(case.get(a) for a in attribs)


@pytest.mark.timeout(TIME_LIMIT)
@pytest.mark.parametrize(
    "filename, expected", get_cases("test_case", "filename", "expected")
)
def test_partition(filename: str, expected: list[int]):
    """Testing the output"""
    vertices, edges = read_xml(f"{DATA_DIR}{filename}")
    partition = Partition(len(vertices))
    for edge in sorted(edges, key=lambda e: e.weight):
        partition.add(edge)
    assert partition.forest == expected


if __name__ == "__main__":
    pytest.main(["-v", __file__])
