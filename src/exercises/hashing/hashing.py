#!/usr/bin/env python3
"""
`hashing` implementation

@authors:
@version: 2022.9
"""


def hash_remainder(key: int, size: int) -> int:
    """Finds hash using remainder

    :param key: key to hash
    :param size: size of the collection
    :return: hash value

    >>> hash_remainder(42, 7)
    0
    >>> hash_remainder(40, 9)
    4
    """
    # TODO: Implement this function
    ...


def hash_mid_sqr(key: int, size: int) -> int:
    """
    Finds hash using mid-square method

    :param key: key to hash
    :param size: size of the collection
    :return: hash value

    >>> hash_mid_sqr(4242, 7)
    3
    >>> hash_mid_sqr(424, 9)
    7
    """
    # TODO: Implement this function
    ...


def hash_folding(key: str, size: int) -> int:
    """
    Finds hash using folding method

    :param key: key to hash
    :param size: size of the collection
    :return: hash value

    >>> hash_folding('(123) 456-7890', 7)
    4
    >>> hash_folding(424-7-23, 8)
    3
    """
    # TODO: Implement this function
    ...


def hash_str(key: str, size: int) -> int:
    """
    Finds hash using sum-of-values method

    :param key: key to hash
    :param size: size of the collection
    :return: hash value

    >>> hash_str('aardvark', 7)
    4
    >>> hash_str('vardakar', 7)
    4
    """
    # TODO: Implement this function
    ...


def hash_str_weighted(key: str, size: int) -> int:
    """
    Finds hash using weighted sum-of-values method

    :param key: key to hash
    :param size: size of the collection
    :return: hash value

    >>> hash_str_weighted('aardvark', 7)
    5
    >>> hash_str_weighted('vardakar', 7)
    2
    """
    # TODO: Implement this function
    ...
