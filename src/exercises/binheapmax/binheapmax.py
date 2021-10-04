#!/usr/bin/env python3
"""Binary Heap implementation"""


from typing import Any


class BinaryHeapMax:
    """Heap class implementation"""

    def __init__(self):
        """Initializer"""
        self._heap = []
        self._size = 0

    def _perc_up(self, cur_idx: int) -> None:
        """Move a node up"""
        # TODO: Implement this function
        ...

    def _perc_down(self, cur_idx: int) -> None:
        """Move a node down"""
        # TODO: Implement this function
        ...

    def add(self, item: Any) -> None:
        """Add a new item"""
        # TODO: Implement this function
        ...

    def remove(self) -> Any:
        """Remove an item from the heap"""
        # TODO: Implement this function
        ...

    def heapify(self, not_a_heap: list) -> None:
        """Turn a list into a heap"""
        # TODO: Implement this function
        ...

    def _get_max_child(self, parent_idx: int) -> int:
        """Get index of the greater child"""
        # TODO: Implement this function
        ...

    def __len__(self) -> int:
        """Get heap size"""
        return self._size

    def __str__(self) -> str:
        """Heap as a string """
        return str(self._heap)
