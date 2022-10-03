#!/usr/bin/env python3
"""Leftist heap exercise"""

from graphviz import render


def main():
    """This is the main function"""
    render("dot", "png", "src/exercises/leftist_heap/leftist_heap_1.gv")
    render("dot", "png", "src/exercises/leftist_heap/leftist_heap_2.gv")
    render("dot", "png", "src/exercises/leftist_heap/leftist_heap_answer.gv")


if __name__ == "__main__":
    main()
