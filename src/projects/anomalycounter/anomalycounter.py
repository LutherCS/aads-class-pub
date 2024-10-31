#!/usr/bin/env python3
"""
`anomalycounter` implementation and driver

@authors:
@version: 2024.10
"""

import argparse
from pathlib import Path


def count(filename: Path, sides: int) -> int:
    """Count number of anomalies/blobs in an image

    :param filename: name of the file to process
    :return: number of anomalies/blobs in the file
    """
    # TODO: Implement this function
    # NOTE: You may define an auxillary function to implement the algorithm
    ...


def main():
    """Entry point"""
    parser = argparse.ArgumentParser(
        description="Specify adjacency rule (4 or 8 sides)"
    )
    parser.add_argument("--sides", type=int, choices=[4, 8], required=True)
    args = parser.parse_args()
    data_dir = "data/projects/anomalycounter/"
    for file in sorted(Path(data_dir).glob("*.in")):
        print(f"{file.name}: {count(file, args.sides)}")


if __name__ == "__main__":
    main()
