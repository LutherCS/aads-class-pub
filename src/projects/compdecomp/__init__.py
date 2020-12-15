#!/usr/bin/env python3
"""
compdecomp import statement
"""

from .huffman import (
    build_tree,
    traverse_tree,
    follow_tree,
    mark_tree,
    print_codes,
    load_codes,
    compress,
    decompress,
)

__all__ = [
    "build_tree",
    "traverse_tree",
    "follow_tree",
    "mark_tree",
    "print_codes",
    "load_codes",
    "compress",
    "decompress",
]
