#!/usr/bin/env python3
"""Turning in-order and post-order tree traversals into pre-order"""


def get_preorder(inorder: str, postorder: str) -> str:
    """Return pre-order traversal of a tree based on its in-order and post-order traversals"""
    raise NotImplementedError


def main():
    """This is the main function"""
    print(get_preorder(inorder="UOMELBARTKGSNI", postorder="UMELABORSGNIKT"))


if __name__ == "__main__":
    main()
