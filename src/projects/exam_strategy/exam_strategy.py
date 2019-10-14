#!/usr/bin/env python3
"""
Exam strategy
"""

from collections import namedtuple
from typing import List, Tuple

Item = namedtuple("Item", ["value", "weight"])


def knapsack(capacity: int, items: List[Item]) -> List[int]:
    """
    General Knapsack solution.

    This function takes the knapsack capacity and the list of items (named tuples) to consider.
    The function returns a list of chosen indices.
    This function is optional but highly recommended.
    Use of the named tuple Item is optional but encouraged.
    """
    pass


def pick_questions_to_answer(filename: str) -> Tuple[List[int], int]:
    """
    Main selection function

    This function takes file name as an argument.
    The function returns a tuple of two items: the list of chosen indices and total point value of all selected questions.
    """
    raise NotImplementedError


def main():
    """Entry point"""
    for i in range(1, 6):
        filename = f"data/projects/exam_strategy/questions{i}.in"
        selection = pick_questions_to_answer(filename)
        print(
            f"Case {i}: Items {sorted(selection[0])} sum up to {selection[1]}"
        )


if __name__ == "__main__":
    main()
