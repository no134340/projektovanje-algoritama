"""
DESCRIPTION:
    Custom min heap.
    Elements of heap are objects of Data type.
"""

from math import floor
from math import log2
from math import inf


def left(i):
    return 2 * i + 1


def right(i):
    return 2 * i + 2


def parent(i):
    return (i - 1) // 2


class MinHeap():

    def __init__(self):
        self.heap = []
        self.height = 0
        self.length = len(self.heap)

    def __len__(self):
        return len(self.heap)

    def __str__(self):
        return str(self.heap)

    def get_height(self):
        return floor(log2(self.length))

    def build_heap(self, arr):
        self.heap = list(arr)
        self.length = len(self.heap)
        self.height = self.get_height()
        for i in range(self.length // 2 + 1, -1, -1):
            self.heapify(i)

    def heapify(self, i):
        l = left(i)
        r = right(i)
        smallest = i

        if l <= (self.length - 1) and self.heap[l].key <= self.heap[i].key:
            smallest = l
        if r <= (self.length - 1) and self.heap[r].key <= self.heap[smallest].key:
            smallest = r

        if smallest != i:
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            self.heapify(smallest)

    def decrease_key(self, i, key):
        if key <= self.heap[i].key:
            self.heap[i].key = key
            while i > 0 and self.heap[i].key <= self.heap[parent(i)].key:
                self.heap[i], self.heap[parent(i)] = self.heap[parent(i)], self.heap[i]
                i = parent(i)

    def heap_insert(self, elem):
        key = elem.key
        self.length += 1
        elem.key = inf
        self.heap.append(elem)
        self.decrease_key(self.length - 1, key)
        self.height = self.get_height()

    def heap_delete(self, i):
        deleted = self.heap[i]
        self.decrease_key(i, -inf)
        self.extract_top()
        self.height = self.get_height()
        return deleted

    def extract_top(self):
        top_node = None
        if len(self.heap) > 0:
            top_node = self.heap[0]
            new_top = self.heap[self.length - 1]
            self.heap[0] = new_top
            self.heap.pop(self.length - 1)
            self.length -= 1
            self.heapify(0)
        return top_node
