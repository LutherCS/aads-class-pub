#!/usr/bin/env python3
"""
`avl_tree` implementation

@authors:
@version: 2022.10
"""

from typing import Any

from .binary_search_tree import BinarySearchTree, BinaryTreeNode


class AVLTree(BinarySearchTree):
    """AVL tree implementation"""

    class AVLTreeNode(BinaryTreeNode):
        """AVL Tree Node"""

        def __init__(self, key, val, balance, left=None, right=None, parent=None):
            """Create an AVL tree node"""
            BinaryTreeNode.__init__(self, key, val, left, right, parent)
            self._balance = balance

        def get_balance(self):
            """Get the node balance factor"""
            return self._balance

        def set_balance(self, value):
            """Set the node balance factor"""
            self._balance = value

        balance = property(get_balance, set_balance)

    def __init__(self):
        """Create a new AVL tree"""
        BinarySearchTree.__init__(self)

    def put(self, key: Any, value: Any) -> None:
        """Add new node"""
        if self._root:
            self._put(key, value, self._root)
        else:
            self._root = self.AVLTreeNode(key, value, 0)
        self._size = self._size + 1

    def _put(self, key: Any, value: Any, current_node: AVLTreeNode) -> None:
        """Add a new node to the tree (helper function)"""
        if key < current_node.key:
            if current_node.get_left_child():
                self._put(key, value, current_node.left_child)
            else:
                current_node.left_child = self.AVLTreeNode(
                    key, value, 0, parent=current_node
                )
                self.update_balance(current_node.left_child)
        else:
            if current_node.get_right_child():
                self._put(key, value, current_node.right_child)
            else:
                current_node.right_child = self.AVLTreeNode(
                    key, value, 0, parent=current_node
                )
                self.update_balance(current_node.right_child)

    def update_balance(self, node: AVLTreeNode) -> None:
        """Update the tree balance"""
        # TODO: Fix this method
        if node.balance > 1 or node.balance < -1:
            self.rebalance(node)
            return
        if node.parent:
            if node.is_right_child():
                node.parent.balance += 1
            elif node.is_left_child():
                node.parent.balance -= 1

            if node.parent.balance != 0:
                self.update_balance(node.parent)

    def rebalance(self, node: AVLTreeNode) -> None:
        """Rebalance the tree"""
        # TODO: Implement this method considering all cases
        if node.balance < 0:
            if node.left_child.balance < 0:
                ...
        elif node.balance > 0:
            if node.right_child.balance > 0:
                ...

    def rotate_left(self, rotation_root: AVLTreeNode) -> None:
        """Left rotation"""
        # TODO: Implement this method
        new_root = rotation_root.right_child
        rotation_root.right_child = new_root.left_child
        if new_root.left_child:
            new_root.left_child.parent = rotation_root
        new_root.parent = rotation_root.parent
        if rotation_root.is_root():
            self._root = new_root
        else:
            if rotation_root.is_left_child():
                rotation_root.parent.left_child = new_root
            else:
                rotation_root.parent.right_child = new_root
        new_root.left_child = rotation_root
        rotation_root.parent = new_root
        # TODO: update rotation_root.balance
        ...
        # TODO: update new_root.balance
        ...

    def rotate_right(self, rotation_root: AVLTreeNode) -> None:
        """Right rotation"""
        # TODO: Implement this method
        ...
        new_root = rotation_root.left_child
        rotation_root.left_child = new_root.right_child
        if new_root.right_child:
            new_root.right_child.parent = rotation_root
        new_root.parent = rotation_root.parent
        if rotation_root.is_root():
            self._root = new_root
        else:
            if rotation_root.is_right_child():
                rotation_root.parent.right_child = new_root
            else:
                rotation_root.parent.left_child = new_root
        new_root.right_child = rotation_root
        rotation_root.parent = new_root
        # TODO: update rotation_root.balance
        ...
        # TODO: update new_root.balance
        ...
