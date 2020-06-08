#!/usr/bin/env python3
"""Hashing functions"""


def hash_remainder(key: int, size: int) -> int:
    """Find hash using remainder"""
    raise NotImplementedError


def hash_mid_sqr(key: int, size: int) -> int:
    """Find hash using mid-square method"""
    raise NotImplementedError


def hash_folding(key: int, size: int) -> int:
    """Find hash using folding method"""
    raise NotImplementedError


def hash_str(key: str, size: int) -> int:
    """Find string hash using simple sum-of-values method"""
    raise NotImplementedError


def hash_str_weighted(key: str, size: int) -> int:
    """Find string hash using character positions as weights"""
    raise NotImplementedError

