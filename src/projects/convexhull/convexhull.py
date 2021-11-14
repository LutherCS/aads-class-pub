#!/usr/bin/env python3
"""
Convex Hull

@authors: Roman Yasinovskyy
@version: 2021.11
"""


def get_convex(filename: str) -> list:
    """
    Find points on the convex hull

    Calculate the result with p0 as the lowest-rightmost

    :param filename: name of a file with all all points
    :return: list of point in the correct order (starting with the rightmost-lowest)
    """
    # TODO: Implement this function
    ...


def measure_convex(hull_points: list) -> float:
    """
    Calculate the length of the convex hull

    :param hull_points: all points on the convex hull in counter-clockwise order
    :return: length of the convex hull
    """
    # TODO: Implement this function
    ...


def main():
    """Entry point"""
    print(f"{'file':20s}{'points':10s}{'length'}")
    for i in [1, 2, 3]:
        filename = f"convexhull{i}.in"
        hull_points = get_convex("data/projects/convexhull/" + filename)
        hull_length = measure_convex(hull_points)
        print(f"{filename:20s}{len(hull_points):<10d}{hull_length}")


if __name__ == "__main__":
    main()
