#!/usr/bin/env python3
"""
Testing Dijkstra's algorithm implementation
@author: Roman Yasinovskyy
@date: 2020
"""

import pathlib
import pytest
import toml
from src.exercises.dijkstra import read_toml, find_path

TIME_LIMIT = 1


def get_cases(category: str):
    with open(pathlib.Path(__file__).with_suffix(".toml")) as f:
        all_cases = toml.load(f)
        for case in all_cases[category]:
            yield (case.get("vertex"), case.get("distance"))


@pytest.mark.timeout(TIME_LIMIT)
@pytest.mark.parametrize("vertex, distance", get_cases("distance_to_t"))
def test_dijkstra_1(vertex, distance):
    """Testing the output"""
    g = read_toml("data/exercises/dijkstra/network.toml")
    find_path(g, "t")
    assert g.get_vertex(vertex).distance == distance


@pytest.mark.timeout(TIME_LIMIT)
@pytest.mark.parametrize("vertex, distance", get_cases("distance_to_v"))
def test_dijkstra_2(vertex, distance):
    """Testing the output"""
    g = read_toml("data/exercises/dijkstra/network.toml")
    find_path(g, "v")
    assert g.get_vertex(vertex).distance == distance


@pytest.mark.timeout(TIME_LIMIT)
@pytest.mark.parametrize("vertex, distance", get_cases("distance_to_y"))
def test_dijkstra_3(vertex, distance):
    """Testing the output"""
    g = read_toml("data/exercises/dijkstra/network.toml")
    find_path(g, "y")
    assert g.get_vertex(vertex).distance == distance


if __name__ == "__main__":
    pytest.main(["test_dijkstra.py"])
