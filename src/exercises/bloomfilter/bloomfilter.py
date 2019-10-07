#!/usr/bin/env python3
"""Bloom filter implementation"""


from zlib import crc32


class BloomFilter:
    def __init__(self, size: int = 11, k: int = 3):
        """Initialize the filter"""
        raise NotImplementedError

    def _hash(self, word: str) -> tuple:
        """Return a tuple of k indices"""
        raise NotImplementedError

    def add(self, word: str):
        """Add a dictionary word to the filter"""
        raise NotImplementedError

    def __contains__(self, word: str) -> bool:
        """Check if a word in in the filter"""
        raise NotImplementedError

    def __str__(self):
        """Return string representation of the filter"""
        return str(self._filter)

    def __len__(self):
        """Return size of the filter"""
        return len(self._filter)
