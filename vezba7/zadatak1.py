"""
Description:
    Chaining hash table module.
Author:
    Jasmina Savić RA40/2017
"""

from math import floor, sqrt
from random import randint
from data import Data
from collections import deque
import time


class HashTable:

    factor = 0.75

    def __init__(self, m, p, hash_function):
        self.table = [None] * m
        self.m = m
        self.h = hash_function
        self.p = p
        self.a = randint(1, self.p - 1)
        self.b = randint(0, self.p - 1)
        self.cnt = 0
        self.min = m

    def __repr__(self):
        table_string = ""
        for i in range(self.m):
            table_string += f"{i} : {self.table[i]}\n"
        return table_string

    def h_division(self, k):
        return k % self.m

    def h_multiplication(self, k):
        A = (sqrt(5) - 1) / 2
        return floor(self.m * ((k * A) - floor(k * A)))

    def h_universal(self, k):
        return ((self.a * k + self.b) % self.p) % self.m

    def rehash(self, new_m):
        self.m = new_m
        new_table = HashTable(self.m, self.p, self.h)
        for d in self.table:
            if d:
                for i in range(len(d)):
                    elem = deque.popleft(d)
                    new_table.insert(elem, rehash=False)
        self.table = list(new_table.table)

    def insert(self, data, rehash=True):
        if self.cnt / self.m >= self.factor and rehash:
            self.rehash(2 * self.m)
        pos = self.h(self, data.key)
        if not self.table[pos]:
            self.table[pos] = deque()
            self.table[pos].insert(0, data)
        else:
            for elem in self.table[pos]:
                if elem.key == data.key:
                    return False
            self.table[pos].insert(0, data)
        self.cnt += 1
        return True

    def search(self, k):
        pos = self.h(self, k)
        if self.table[pos]:
            for elem in self.table[pos]:
                if elem.key == k:
                    return elem
        return None

    def delete_elem(self, key):
        pos = self.h(self, key)
        if self.table[pos]:
            for elem in self.table[pos]:
                if elem.key == key:
                    self.table[pos].remove(elem)
                    self.cnt -= 1
                    if self.cnt / self.m <= (1 - self.factor):
                        new_m = self.m // 2
                        if new_m >= self.min:
                            self.rehash(new_m)
                    return True
        return False


def time_test(n, p, fp, h):
    # test1: m = p
    m = p
    fp.write(f"n = {n}, p = {p}, m = {m}\n")
    table = HashTable(m, p, h)
    data = [Data(randint(0, p - 1)) for _ in range(n)]
    start = time.time()
    for d in data:
        table.insert(d)
    end = time.time()
    fp.write(f"Time to insert: {end - start}\n")

    start = time.time()
    table.search(randint(0, p - 1))
    end = time.time()
    fp.write(f"Time to search for random element: {end - start}\n\n")

    # test 2 m = p/2
    m = p // 2
    fp.write(f"n = {n}, p = {p}, m = {m}\n")
    table = HashTable(m, p, h)
    data = [Data(randint(0, p - 1)) for _ in range(n)]
    start = time.time()
    for d in data:
        table.insert(d)
    end = time.time()
    fp.write(f"Time to insert: {end - start}\n")

    start = time.time()
    table.search(randint(0, p - 1))
    end = time.time()
    fp.write(f"Time to search for random element: {end - start}\n\n")

    # test 2 m = p/4
    m = p // 4
    fp.write(f"n = {n}, p = {p}, m = {m}\n")
    table = HashTable(m, p, h)
    data = [Data(randint(0, p - 1)) for _ in range(n)]
    start = time.time()
    for d in data:
        table.insert(d)
    end = time.time()
    fp.write(f"Time to insert: {end - start}\n")

    start = time.time()
    table.search(randint(0, p - 1))
    end = time.time()
    fp.write(f"Time to search for random element: {end - start}\n\n")


if __name__ == '__main__':
    fp = open("zadatak1_log.txt", "w")

    fp.write("****************************************************************\n\n")
    fp.write("Division method:\n\n")

    ################################################

    n = 10000
    p = 23
    time_test(n, p, fp, HashTable.h_division)

    ################################################

    n = 50000
    p = 9973
    time_test(n, p, fp, HashTable.h_division)

    ################################################

    n = 100000
    p = 99991
    time_test(n, p, fp, HashTable.h_division)

    fp.write("****************************************************************\n\n")

    fp.write("Multiplication method:\n\n")

    ################################################

    n = 10000
    p = 23
    time_test(n, p, fp, HashTable.h_multiplication)

    ################################################

    n = 50000
    p = 9973
    time_test(n, p, fp, HashTable.h_multiplication)

    ################################################

    n = 100000
    p = 99991
    time_test(n, p, fp, HashTable.h_multiplication)

    fp.write("****************************************************************\n\n")

    fp.write("Universal hashing:\n\n")

    ################################################

    n = 10000
    p = 23
    time_test(n, p, fp, HashTable.h_universal)

    ################################################

    n = 50000
    p = 9973
    time_test(n, p, fp, HashTable.h_universal)

    ################################################

    n = 100000
    p = 99991
    time_test(n, p, fp, HashTable.h_universal)

    fp.write("****************************************************************\n\n")

    fp.close()

    # table1 = HashTable(31//4, 31, HashTable.h_division)
    #
    # tst = [randint(0, 30) for i in range(50)]
    #
    # print(tst)
    #
    # for sample in tst:
    #     print(f"Trying to insert {sample}")
    #     if table1.insert(Data(sample)):
    #         print(f"Inserted {sample}")
    #         print(f"Table size {table1.m}")
    #     else:
    #         print(f"{sample} wasn't inserted.")
    #
    # print(f"\n {table1}\n")
    #
    # i = 0
    # while i < len(tst):
    #     if table1.delete_elem(tst[i]):
    #         print(f"Deleted {tst[i]}")
    #         print(f"Table size {table1.m}")
    #     else:
    #         print(f"{tst[i]} not deleted.")
    #     i += 2
    #
    # i = 0
    # while i < len(tst):
    #     if table1.search(tst[i]):
    #         print(f"Found {tst[i]}")
    #     else:
    #         print(f"{tst[i]} not found.")
    #     i += 2

