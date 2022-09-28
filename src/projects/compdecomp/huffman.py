#!/usr/bin/env python3
"""
`compdecomp` implementation

@authors:
@version: 2022.9
"""

import argparse
import heapq
import json
import logging
import pathlib
from collections import Counter
from typing import Any

DATA_DIR = pathlib.Path("data/projects/compdecomp/")


class Node:
    """Class Node"""

    def __init__(self, value: Any, weight: int, left=None, right=None) -> None:
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

    def __lt__(self, other: "Node") -> bool:
        """Node comparison"""
        if not isinstance(other, Node):
            raise TypeError("Can only compare two nodes")
        return self.weight < other.weight

    def __repr__(self) -> str:
        """Node representation"""
        return f"Node({self.value}, {self.weight}, {self.left}, {self.right})"


def build_tree(all_freq: dict) -> Node:
    """
    Construct a Huffman tree from the text

    :param all_freq: frequency table
    :return tuple the tree root
    """
    heap: list[Node] = []
    # NOTE: Use list comprehension to build a list of Nodes and then heapify it
    # TODO: Implement this function
    ...


def traverse_tree(root: Node) -> str:
    """
    Traverse a tree pre-order and return the result

    :param root: tree root
    :return values of a tree
    """
    # TODO: Implement this function
    ...


def follow_tree(tree: Node, code: str) -> str | None:
    """
    Follow the code through the tree

    :param tree: tree root
    :param code: code to find
    :return node value or None
    """
    # TODO: Implement this function
    ...


def mark_tree(d1: dict, d2: dict, root: Node, path: str) -> tuple[dict, dict] | None:
    """
    Generate code for each letter in the text

    :param d1: character-to-code mapping
    :param d2: code-to-character mapping
    :param root: tree root
    :param path: path to the current node
    :return (d1, d2) tuple
    """
    # TODO: Implement this function
    ...


def print_codes(d: dict, weights: dict) -> None:
    """
    Print letters of the text and their codes. The output is ordered by the letter weight.

    :param d: character-to-code mapping
    :param weights: character-to-frequency mapping
    """
    print(f"{'Letter':10s}{'Weight':^10s}{'Code':^10s}{'Length':^5s}")
    # TODO: Implement this function
    ...


def load_codes(codes: dict) -> Node:
    """
    Build the Huffman tree from the stored code-to-character mapping

    :param codes: code-to-character mapping
    :return root of the Huffman tree
    """
    # TODO: Implement this function
    ...


def compress(text: str, codes: dict) -> tuple[bytes, int]:
    """
    Compress text using Huffman coding

    :param text: text to compress
    :param codes: character-to-code mapping
    :return (packed text, padding length) tuple
    """
    # TODO: Implement this function
    ...


def decompress(bytestream: bytes, padding: int, tree: Node) -> str:
    """
    Decompress binary data using Huffman coding

    :param bytestream: bytes from the archived file
    :param padding: padding length
    :param tree: root of the Huffman tree
    :return decompressed (decoded) text
    """
    # TODO: Implement this function
    ...


def main():
    """Main function"""
    parser = argparse.ArgumentParser(description="Greet the audience")
    parser.add_argument(
        "-d",
        "--debug",
        help="Enable debug mode",
        action="store_const",
        dest="loglevel",
        const=logging.DEBUG,
        default=logging.WARNING,
    )
    parser.add_argument(
        "-v",
        "--verbose",
        help="Enable verbose mode",
        action="store_const",
        dest="loglevel",
        const=logging.INFO,
    )
    args = parser.parse_args()
    logging.basicConfig(format="%(levelname)s: %(message)s", level=args.loglevel)
    logging.info("Starting up")

    input_files = ["dead_dad", "alphabet", "example", "preamble"]

    for filename in input_files:
        logging.info("Building the tree")
        with open(
            DATA_DIR / pathlib.Path(f"{filename}.txt"), "r", encoding="utf-8"
        ) as text_file:
            text = text_file.read().strip()
        weights = Counter(text)
        root = build_tree(weights)
        char_to_code, code_to_char = mark_tree({}, {}, root, "")

        logging.info("Text statistics")
        print(f"\n{text}")
        print_codes(char_to_code, weights)
        logging.debug(char_to_code)
        logging.debug(code_to_char)
        logging.debug(traverse_tree(root))

        logging.info("Compressing the text")
        archive, padding_length = compress(text, char_to_code)
        code_to_char["padding"] = padding_length
        print(
            f"Text: {text[:5]} ... {text[-5:]}. Compression ratio: {len(archive) / len(text):.3f}"
        )
        logging.debug(archive)

        logging.info("Loading codes from the file")
        with open(
            DATA_DIR / pathlib.Path(f"{filename}.json"), "r", encoding="utf-8"
        ) as code_file:
            metadata = json.load(code_file)
        root = load_codes(metadata)
        padding_length = metadata.get("padding", 0)
        logging.debug(traverse_tree(root))

        logging.info("Decompressing the archive")
        with open(DATA_DIR / pathlib.Path(f"{filename}.bin"), "rb") as data_file:
            result = decompress(data_file.read(), padding_length, root)
        print(result)


if __name__ == "__main__":
    main()
