#!/usr/bin/env python3
"""Binary Heap implementation"""


class BinaryHeapMax:
    """Heap class implementation"""

    def __init__(self):
        """Initializer"""
        self._heap = []
        self._size = 0

    def _perc_up(self, cur_idx):
        """Move a node up"""
        raise NotImplementedError

    def _perc_down(self, cur_idx):
        """Move a node down"""
        raise NotImplementedError

    def insert(self, item):
        """Add a new item. Optional for this exercise"""
        pass

    def delete(self):
        """Remove an item from the heap. Optional for this exercise"""
        pass

    def heapify(self, not_a_heap):
        """Turn a list into a heap"""
        raise NotImplementedError

    def get_max_child(self, parent_idx):
        """Get the greater child"""
        raise NotImplementedError

    def __len__(self):
        """Get heap size"""
        return self._size

    def __str__(self):
        """Heap as a string """
        return str(self._heap)
