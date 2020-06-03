"""
DESCRIPTION:
    Tree node module.
"""


class Node:

    def __init__(self, key, data):
        self.key = key
        self.data = data
        self.left = None
        self.right = None
        self.parent = None

    def __repr__(self):
        rep = f"{self.data}"
        return rep

    def set_left_child(self, left):
        self.left = left

    def set_right_child(self, right):
        self.right = right

    def set_parent(self, parent):
        self.parent = parent
