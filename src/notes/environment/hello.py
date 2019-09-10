#!/usr/bin/env python3
# encoding: UTF-8
"""
Implementation of Hello, World
@author: Roman Yasinovskyy
@date: 2019
"""

# import random
# import time


def hello(audience: str) -> str:
    """Greet the audience"""
    # time.sleep(random.randint(0, 1))
    if not isinstance(audience, str):
        raise TypeError(f"Please provide a valid string instead of {audience}")
    return "Hello, " + audience


def main():
    """This is the main function"""
    print(hello("World"))


if __name__ == "__main__":
    main()
