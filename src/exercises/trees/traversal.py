#!/usr/bin/env python3
"""
`trees` implementation and driver
Turning in-order and post-order tree traversals into pre-order


@authors: Roman Yasinovskyy
@version: 2021.9
"""


def get_preorder(inorder: str, postorder: str) -> str:
    """
    Returns pre-order traversal of a tree based on its in-order and post-order traversals

    :param inorder: in-order tree traversal
    :param postorder: post-order tree traversal
    :return: pre-order tree traversal
    >>> get_preorder("UOMELBARTKGSNI", "UMELABORSGNIKT")
    'TROUBLEMAKINGS'
    """
    # TODO: Implement this function
    ...


def main():
    """This is the main function"""
    print("Pre-order tree traversal")
    print(get_preorder(inorder="UOMELBARTKGSNI", postorder="UMELABORSGNIKT"))


if __name__ == "__main__":
    main()
