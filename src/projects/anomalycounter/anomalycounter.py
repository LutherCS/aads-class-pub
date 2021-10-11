#!/usr/bin/env python3
"""
`anomalycounter` implementation

@authors: Roman Yasinovskyy
@version: 2021.10
"""

from pathlib import Path


def count(filename: str) -> int:
    """Count number of anomalies/blobs in an image

    :param filename: name of the file to process
    :return: number of anomalies/blobs in the file
    """
    # TODO: Implement this function
    # NOTE: You may define an auxillary function to implement the algorithm
    ...


def main():
    """Entry point"""
    data_dir = "data/projects/anomalycounter/"
    for f in Path(data_dir).glob("*.in"):
        print(f"{f.name}: {count(f)}")


if __name__ == "__main__":
    main()
