#!/usr/bin/env python3
"""
`trees` testing

@authors: Roman Yasinovskyy
@version: 2024.9
"""

import importlib
import pathlib
import sys
from typing import Generator

import pytest
import tomllib

try:
    importlib.util.find_spec(".".join(pathlib.Path(__file__).parts[-3:-1]), "src")
except ModuleNotFoundError:
    sys.path.append(f"{pathlib.Path(__file__).parents[3]}/")
finally:
    from src.exercises.trees import get_preorder

TIME_LIMIT = 1


def get_cases(category: str, *attribs: str) -> Generator:
    """Get test cases from the TOML file"""
    with open(pathlib.Path(__file__).with_suffix(".toml"), "rb") as file:
        all_cases = tomllib.load(file)
        for case in all_cases[category]:
            yield tuple(case.get(a) for a in attribs)


@pytest.mark.timeout(TIME_LIMIT)
@pytest.mark.parametrize(
    "inorder, postorder, preorder",
    get_cases("test_case", "inorder", "postorder", "preorder"),
)
def test_traversal(inorder: str, postorder: str, preorder: str):
    """Testing the output"""
    assert get_preorder(inorder, postorder) == preorder


if __name__ == "__main__":
    pytest.main(["-v", __file__])
