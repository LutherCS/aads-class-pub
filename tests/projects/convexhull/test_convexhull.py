#!/usr/bin/env python3
"""
`convexhull` testing

@authors: Roman Yasinovskyy
@version: 2021.11
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
    from src.projects.convexhull import get_convex, measure_convex


DATA_DIR = pathlib.Path("data/projects/convexhull/")
TIME_LIMIT = 2


def get_cases(category: str, *attribs: str) -> Generator:
    """Get test cases from the TOML file"""
    with open(pathlib.Path(__file__).with_suffix(".toml"), encoding="utf-8") as file:
        all_cases = toml.load(file)
        for case in all_cases[category]:
            yield tuple(case.get(a) for a in attribs)


@pytest.mark.timeout(TIME_LIMIT)
@pytest.mark.parametrize(
    "filename, points", get_cases("test_case", "filename", "points")
)
def test_convex_points(filename: str, points: int):
    """Test the hull points"""
    assert points == len(get_convex(DATA_DIR / pathlib.Path(filename)))


@pytest.mark.timeout(TIME_LIMIT)
@pytest.mark.parametrize("filename, first", get_cases("test_case", "filename", "first"))
def test_first_point(filename: str, first: list):
    """Test the hull first point"""
    points = get_convex(DATA_DIR / pathlib.Path(filename))
    assert first == [points[0][0], points[0][1]]


@pytest.mark.timeout(TIME_LIMIT)
@pytest.mark.parametrize("filename, last", get_cases("test_case", "filename", "last"))
def test_first_point(filename: str, last: list):
    """Test the hull last point"""
    points = get_convex(DATA_DIR / pathlib.Path(filename))
    assert last == [points[-1][0], points[-1][1]]


@pytest.mark.timeout(TIME_LIMIT)
@pytest.mark.parametrize(
    "filename, length", get_cases("test_case", "filename", "length")
)
def test_convex_length(filename: str, length: float):
    """Test the hull length"""
    hull_points = get_convex(DATA_DIR / filename)
    assert length == pytest.approx(measure_convex(hull_points), 0.001)


if __name__ == "__main__":
    pytest.main(["-v", __file__])
