#!/usr/bin/env python3
"""
AVL tree implementation
"""

from .binary_search_tree import BinarySearchTree
from .binary_search_tree import BinaryTreeNode


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


class AVLTree(BinarySearchTree):
    """AVL tree implementation"""

    def __init__(self):
        """Create a new AVL tree"""
        BinarySearchTree.__init__(self)

    def put(self, key, value):
        """Add new node"""
        if self._root:
            self._put(key, value, self._root)
        else:
            self._root = AVLTreeNode(key, value, 0)
        self._size = self._size + 1

    def _put(self, key, value, current_node: AVLTreeNode) -> None:
        """Add a new node to the tree (helper function)"""
        if key < current_node.key:
            if current_node.get_child_left():
                self._put(key, value, current_node.child_left)
            else:
                current_node.child_left = AVLTreeNode(
                    key, value, 0, parent=current_node
                )
                self.update_balance(current_node.child_left)
        else:
            if current_node.get_child_right():
                self._put(key, value, current_node.child_right)
            else:
                current_node.child_right = AVLTreeNode(
                    key, value, 0, parent=current_node
                )
                self.update_balance(current_node.child_right)

    def update_balance(self, node: AVLTreeNode) -> None:
        """Update the tree balance"""
        # TODO: Fix this method
        if node.balance > 1 or node.balance < -1:
            self.rebalance(node)
            return
        if node.parent:
            if node.is_child_left():
                node.parent.balance += 1
            elif node.is_child_right():
                node.parent.balance -= 1

            if node.parent.balance != 0:
                self.update_balance(node.parent)

    def rebalance(self, node: AVLTreeNode) -> None:
        """Rebalance the tree"""
        # TODO: consider all cases
        if node.balance < 0:
            if node.child_left.balance < 0:
                raise NotImplementedError
        elif node.balance > 0:
            if node.child_right.balance > 0:
                raise NotImplementedError

    def rotate_left(self, rotation_root: AVLTreeNode) -> None:
        """Left rotation"""
        new_root = rotation_root.child_right
        rotation_root.child_right = new_root.child_left
        if new_root.child_left:
            new_root.child_left.parent = rotation_root
        new_root.parent = rotation_root.parent
        if rotation_root.is_root():
            self._root = new_root
        else:
            if rotation_root.is_child_left():
                rotation_root.parent.child_left = new_root
            else:
                rotation_root.parent.child_right = new_root
        new_root.child_left = rotation_root
        rotation_root.parent = new_root
        # TODO: update rotation_root.balance
        # TODO: update new_root.balance

    def rotate_right(self, rotation_root: AVLTreeNode) -> None:
        """Right rotation"""
        new_root = rotation_root.child_left
        rotation_root.child_left = new_root.child_right
        if new_root.child_right:
            new_root.child_right.parent = rotation_root
        new_root.parent = rotation_root.parent
        if rotation_root.is_root():
            self._root = new_root
        else:
            if rotation_root.is_child_right():
                rotation_root.parent.child_right = new_root
            else:
                rotation_root.parent.child_left = new_root
        new_root.child_right = rotation_root
        rotation_root.parent = new_root
        # TODO: update rotation_root.balance
        # TODO: update new_root.balance
