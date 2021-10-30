#!/usr/bin/env python3
"""
`exam_strategy` implementation and driver

@authors: Roman Yasinovskyy
@version: 2021.10
"""

from collections import namedtuple

Item = namedtuple("Item", ["value", "weight"])


def knapsack(capacity: int, items: list[Item]) -> list[int]:
    """
    General Knapsack solution.

    :param capacity: total knapsack capacity
    :param items: the list of items (named tuples) to consider
    :return: a list of chosen indices
    """
    # TODO: Implement this function
    ...


def pick_questions_to_answer(filename: str) -> tuple[list[int], int]:
    """
    Main selection function

    :param filename: file to process
    :return: the list of chosen indices and total point value of all selected questions
    """
    # TODO: Implement this function
    ...


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
