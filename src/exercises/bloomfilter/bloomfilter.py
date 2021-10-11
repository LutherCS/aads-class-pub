#!/usr/bin/env python3
"""
`bloomfilter` implementation and driver

@authors:
@version: 2021.10
"""


from zlib import crc32


class BloomFilter:
    def __init__(self, size: int = 11, k: int = 3) -> None:
        """Initialize the filter"""
        # TODO: Implement this method
        ...

    def hash(self, word: str) -> tuple[int, ...]:
        """Return a tuple of k indices"""
        # TODO: Implement this method
        ...

    def add(self, word: str) -> None:
        """Add a dictionary word to the filter"""
        # TODO: Implement this method
        ...

    def __contains__(self, word: str) -> bool:
        """Check if a word in in the filter"""
        # TODO: Implement this method
        ...

    def __str__(self) -> str:
        """Return string representation of the filter"""
        return str(self._filter)

    def __len__(self) -> int:
        """Return size of the filter"""
        return len(self._filter)


def main():
    bf = BloomFilter()
    dictionary = ["cat", "cow", "dog"]
    for word in dictionary:
        bf.add(word)
    for word in dictionary:
        print(f"{word:10s}{bf.hash(word)} in bf: {word in bf}")
    dictionary2 = ["aardvark", "beaver", "cheetah", "deer", "elephant", "squirrell"]
    for word in dictionary2:
        print(f"{word:10s}{bf.hash(word)} in bf: {word in bf}")


if __name__ == "__main__":
    main()
