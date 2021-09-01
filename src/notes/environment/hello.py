#!/usr/bin/env python3
"""
`hello` implementation and driver

@authors: Roman Yasinovskyy
@version: 2021.9
"""

import argparse
import logging


def greet(audience: str) -> str:
    """
    Greets the audience
    
    :param audience: who should we greet
    :returns: personalized greeting
    :raises: `TypeError` if `audience` is not a string

    >>> greet("World")
    'Hello, World'
    >>> greet("CS360")
    'Hello, CS360'
    """
    if not isinstance(audience, str):
        raise TypeError(f"Please provide a valid string instead of {audience}")
    return "Hello, " + audience


def main():
    """This is the main function"""
    parser = argparse.ArgumentParser(description="Greet the audience")
    parser.add_argument("audience", type=str, help="Audience")
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
    logging.debug(f"About to greet {args.audience}")
    print(greet(args.audience))


if __name__ == "__main__":
    main()
