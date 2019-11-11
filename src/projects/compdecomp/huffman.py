#!/usr/bin/env python3
"""Huffman coding"""


import heapq
from collections import Counter
from typing import List, Union


class Node:
    """Class Node"""

    def __init__(self, value, weight: int, left=None, right=None):
        """
        value: letter in the text
        weight: number of times the letter appears in the text
        left: left child in the Huffman tree
        right: right child in the Huffman tree
        """
        self.value = value
        self.weight = weight
        self.left = left
        self.right = right

    def __lt__(self, other):
        return self.weight < other.weight

    def __repr__(self):
        return f"Node({self.value}, {self.weight}, {self.left}, {self.right})"


def build_tree(text: str) -> tuple:
    """
    Construct a Huffman tree from the text using the following algorithm:
        1. Calculate frequency of each letter in the text and store the result in a frequency table
        2. Turn each letter into an object of type Node and add to a heap
        3. While the heap contains 2 or more items:
            3.1 Remove two items (i1 and i2) from the heap
            3.2 Make a new node with the weight equal to the sum of weight of the two items from 3.1
            3.3 Assign i1 and i2 as left and right children of the new node
            3.4 Add the new node to the heap
        4. Remove the only remaining node from the heap. This is the root of the Huffman tree
        5. Return the (root, frequency table) tuple
    """
    raise NotImplementedError


def traverse_tree(root: Node) -> str:
    """Traverse a tree pre-order and return the result"""
    raise NotImplementedError


def mark_nodes(d1: dict, d2: dict, root: Node, path: str) -> Union[None, tuple]:
    """
    Generate code for each letter in the text using the following algorithm:
        1. If the root is empty, return
        2. If the value of the root is a valid character:
            2.1 Add the value: path mapping to d1
            2.2 Add the path: value mapping to d2
            2.3 return
        3. Recursively mark nodes in the left subtree (add 0 to the path)
        4. Recursively mark nodes in the right subtree (add 1 to the path)
        5. Return (d1, d2) tuple
    """
    raise NotImplementedError


def print_codes(d: dict, weights: dict) -> None:
    """Print letters of the text and their codes. The output is ordered by the letter weight."""
    print(f"{'Letter':10s}{'Weight':^10s}{'Code':^10s}{'Length':^5s}")
    raise NotImplementedError


def main():
    snippets = [
        "A_DEAD_DAD_CEDED_A_BAD_BABE_A_BEADED_ABACA_BED",
        "AAAAAAAAAAAAAAABBBBBBBCCCCCCDDDDDDEEEEE",
        "this is an example of a huffman tree",
    ]

    for text in snippets:
        root, weights = build_tree(text)
        char_to_code, code_to_char = mark_nodes({}, {}, root, "")

        print(f"\n{text}")
        print_codes(char_to_code, weights)


if __name__ == "__main__":
    main()
