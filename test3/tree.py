class Node:

    def __init__(self, key, data):
        self.right = None
        self.left = None
        self.parent = None
        self.key = key
        self.data = data

    def __repr__(self):
        return  f"({self.key} : {self.data})"

    def inorder(self, in_order):
        if self.left:
            self.left.inorder(in_order)

        in_order.append(self)

        if self.right:
            self.right.inorder(in_order)

class Tree:

    def __init__(self):
        self.root = None
        self.cnt = 0
        self.in_order = []

    def insert(self, node):
        self.cnt += 1
        if self.root:
            curr = self.root
            p = self.root
            while curr:
                p = curr
                if curr.key >= node.key:
                    curr = curr.left
                else:
                    curr = curr.right
            node.parent = p
            if node.key >= p.key:
                p.right = node
            else:
                p.left = node
        else:
            self.root = node


    def inorder(self):
        if self.root:
            self.root.inorder(self.in_order)
        return self.in_order

    def encode(self, key):
        ret = ""
        curr = self.root
        while curr.key != key:
            if key < curr.key:
                ret += "."
                curr = curr.left
            else:
                ret += "-"
                curr = curr.right
        return ret

    def decode(self, seq):
        curr = self.root
        for char in seq:
            if char == ".":
                curr = curr.left
            elif char == "-":
                curr = curr.right
            else:
                return None
            if not curr:
                return None
            if not curr.data:
                return None
        if curr.data == '*':
            return None
        return curr.data