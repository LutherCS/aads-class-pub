#!/usr/bin/env python3
"""
`classy` implementation and driver

@authors:
@version: 2022.9
"""


def classify(people: dict) -> list[str]:
    """
    Classify people by class

    :param people: group to classify
    :return list of people sorted by class
    """
    # TODO: Implement this function
    ...


def read_file(filename: str) -> dict[str, str]:
    """
    Read data from the file into a dictionary

    :param filename: file to sort
    :return the {person: class} mapping
    """
    # TODO: Implement this function
    ...


def main():
    """Entry point"""
    people = read_file("data/projects/classy/classy01.txt")
    print(classify(people))


if __name__ == "__main__":
    main()
