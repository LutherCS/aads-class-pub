#!/usr/bin/env python3
"""
`stack` testing

@authors: Roman Yasinovskyy
@version: 2021.11
"""


import importlib
import pathlib
import sys
from inspect import isclass

import pytest

try:
    importlib.util.find_spec(".".join(pathlib.Path(__file__).parts[-3:-1]), "src")
except ModuleNotFoundError:
    sys.path.append(f"{pathlib.Path(__file__).parents[3]}/")
finally:
    from src.projects.interview import Stack, StackError


def test_init():
    """Testing init"""
    the_stack = Stack()
    assert isinstance(the_stack, Stack)


@pytest.mark.parametrize("items", [[], [None], [(1, "a")], ["a", "b"], [1, 2, 3, 2]])
def test_push(items):
    """Testing push"""
    the_stack = Stack()
    for item in items:
        the_stack.push(item)
    assert isinstance(the_stack, Stack)


@pytest.mark.parametrize(
    "items, result",
    [
        ([[]], []),
        ([None], None),
        ([(1, "a")], (1, "a")),
        (["a", "b"], "b"),
        ([1, 2, 3, 2], 2),
    ],
)
def test_pop(items, result):
    """Testing pop"""
    the_stack = Stack()
    for item in items:
        the_stack.push(item)
    assert the_stack.pop() == result
    assert len(the_stack) == len(items) - 1


@pytest.mark.parametrize("items", [[], [None], [(1, "a")], ["a", "b"], [1, 2, 3, 2]])
def test_pop_error(items):
    """Testing pop error"""
    the_stack = Stack()
    for item in items:
        the_stack.push(item)
    with pytest.raises(StackError) as error:
        for _ in range(999):
            the_stack.pop()
    assert error.value.args[0] == "Cannot pop from an empty stack"


@pytest.mark.parametrize(
    "items, result",
    [
        ([[]], []),
        ([None], None),
        ([(1, "a")], (1, "a")),
        (["a", "b"], "b"),
        ([1, 2, 3, 2], 2),
    ],
)
def test_peek(items, result):
    """Testing peek"""
    the_stack = Stack()
    for item in items:
        the_stack.push(item)
    assert the_stack.peek() == result
    assert len(the_stack) == len(items)


def test_peek_error():
    """Testing peek error"""
    the_stack = Stack()
    with pytest.raises(StackError) as error:
        the_stack.peek()
    assert error.value.args[0] == "Nothing to see here, the stack is empty"


@pytest.mark.parametrize(
    "items, num, result",
    [
        ([], 0, False),
        ([[]], 0, True),
        ([None], 1, False),
        ([None], 0, True),
        ([(1, "a")], 1, False),
        ([(1, "a")], 0, True),
        (["a", "b"], 2, False),
        (["a", "b"], 1, True),
        ([1, 2, 3, 2], 4, False),
        ([1, 2, 3, 2], 3, True),
    ],
)
def test_bool(items, num, result):
    """Testing __bool__"""
    the_stack = Stack()
    for item in items:
        the_stack.push(item)
    for _ in range(num):
        the_stack.pop()
    assert bool(the_stack) == result


@pytest.mark.parametrize(
    "items, size",
    [
        ([], 0),
        ([[]], 1),
        ([None], 1),
        ([(1, "a")], 1),
        (["a", "b"], 2),
        ([1, 2, 3, 2], 4),
    ],
)
def test_len(items, size):
    """Testing __len__"""
    the_stack = Stack()
    for item in items:
        the_stack.push(item)
    assert len(the_stack) == size


@pytest.mark.parametrize(
    "items, result, size",
    [
        ([[], []], StackError, 0),
        ([(1, "a"), (2, "b")], StackError, 0),
        (["a", "b"], StackError, 0),
        (["a", "b", "c"], "a", 1),
        ([None, False, True], None, 1),
        ([[], [[]], [[[]]]], [], 1),
        ([1, "2", 3, 2], "2", 2),
        ([1, False, 2, 3], False, 2),
        ([True, False, True, False], False, 2),
        ([None, True, 1, "a", (1, "a")], 1, 3),
        (["a", "b", "c", 1, 2, 3], 1, 4),
        (["a", 1, ("a", 1), {"a": 1}, (1, "a"), ["a", 1], "a1"], (1, "a"), 5),
    ],
)
def test_operations(items, result, size):
    """Testing push/pop/peek"""
    the_stack = Stack()
    for item in items:
        the_stack.push(item)
    the_stack.peek()
    the_stack.pop()
    the_stack.pop()
    if not isclass(result):
        assert the_stack.peek() == result
    assert len(the_stack) == size


if __name__ == "__main__":
    pytest.main(["-v", __file__])
