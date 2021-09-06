#!/usr/bin/env python3
"""
A Classy Problem
"""

# from typing import Dict, List


def classify(people: dict) -> list[str]:
    """
    Classify people
    
    Return the ordered (highest to lowest) list
    """
    raise NotImplementedError


def read_file(filename: str) -> dict[str, str]:
    """
    Read data from the file into a dictionary

    Return the {person: class} mapping
    """
    raise NotImplementedError



def main():
    """Entry point"""
    people = read_file("data/projects/classy/classy01.txt")
    print(classify(people))


if __name__ == "__main__":
    main()
