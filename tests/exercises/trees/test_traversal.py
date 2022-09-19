#!/usr/bin/env python3
"""
`trees` testing

@authors: Roman Yasinovskyy
@version: 2022.9
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
    from src.exercises.trees import get_preorder

TIME_LIMIT = 1


def get_cases(category: str):
    with open(pathlib.Path(__file__).with_suffix(".toml"), encoding="utf-8") as f:
        all_cases = toml.load(f)
        for case in all_cases[category]:
            yield (case.get("inorder"), case.get("postorder"), case.get("preorder"))


@pytest.mark.timeout(TIME_LIMIT)
@pytest.mark.parametrize("inorder, postorder, preorder", get_cases("test_case"))
def test_traversal(inorder, postorder, preorder):
    """Testing the output"""
    assert get_preorder(inorder, postorder) == preorder


if __name__ == "__main__":
    pytest.main(["-v", __file__])
