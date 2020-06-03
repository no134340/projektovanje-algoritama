"""
Description:
    Open addressing hash table module.
Author:
    Jasmina Savić RA40/2017
"""

from data import Data
from random import randint
import time


class HashTable:
    c1 = 0.5
    c2 = 0.5
    alpha = 0.6

    def __init__(self, m, hash_function, hash_helper=None, mp=None):
        self.table = [None] * m
        self.m = m
        if not mp:
            self.mp = m - 1
        else:
            self.mp = mp
        self.h = hash_function
        self.hp = hash_helper
        self.cnt = 0
        self.min = m

    def __repr__(self):
        table_string = ""
        for i in range(self.m):
            table_string += f"{i} : {self.table[i]}\n"
        return table_string

    def h_linear(self, k, i):
        return int((self.hp(self, k) + i) % self.m)

    def h_quad(self, k, i):
        return int((self.hp(self, k) + self.c1 * i + self.c2 * (i ** 2)) % self.m)

    def h_double(self, k, i):
        return int((self.h1(k) + i * self.h2(k)) % self.m)

    def h1(self, k):
        return k % self.m

    def h2(self, k):
        return 1 + (k % self.mp)

    # ovo je problem sto del-ove ne slika u del-ove xD
    # mozda zapamtiti koja je to vrednost bila pre del-a
    # nju izhesirati kako bismo nasli poziciju i upisati del
    # inace pretraga kasnije nece raditi
    # sad je kasno (sad je kasno) da se menja
    def rehash(self, new_m):
        self.m = new_m
        self.mp = new_m - 1
        new_table = HashTable(self.m, self.h, self.hp, self.mp)
        for elem in self.table:
            if elem and elem != "del":
                new_table.insert(elem, rehash=False)
        self.table = list(new_table.table)

    def insert(self, data, rehash=True):
        if self.cnt / self.m >= self.alpha and rehash:
            self.rehash(2 * self.m)
        for i in range(self.m):
            pos = self.h(self, data.key, i)
            if not self.table[pos] or self.table[pos] == "del":
                self.table[pos] = data
                self.cnt += 1
                return True
            if self.table[pos].key == data.key:
                return False
        return False

    def search(self, k):
        for i in range(self.m):
            pos = self.h(self, k, i)
            if not self.table[pos]:
                return None
            if self.table[pos] == "del":
                continue
            if self.table[pos].key != k:
                continue
            return self.table[pos]
        return None

    def delete_elem(self, k):
        for i in range(self.m):
            pos = self.h(self, k, i)
            if not self.table[pos]:
                return False
            if self.table[pos] == "del":
                continue
            if self.table[pos].key != k:
                continue
            self.table[pos] = "del"
            self.cnt -= 1
            if self.cnt / self.m <= (1 - self.alpha):
                new_m = self.m // 2
                if new_m >= self.min:
                    self.rehash(new_m)
            return True
        return False


def time_test(n, p, fp, h, hp=None, mp=None):
    # test1: m = n
    m = n
    mp = m - 1
    fp.write(f"n = {n}, p = {p}, m = {m}, mp = {mp}\n")
    table = HashTable(m, hash_function=h, hash_helper=hp, mp=mp)
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

    # test 2 m = n/2
    m = n // 2
    mp = m - 1
    fp.write(f"n = {n}, p = {p}, m = {m}, mp = {mp}\n")
    table = HashTable(m, hash_function=h, hash_helper=hp, mp=mp)
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

    # test 2 m = n/4
    m = n // 4
    mp = m - 1
    fp.write(f"n = {n}, p = {p}, m = {m}, mp = {mp}\n")
    table = HashTable(m, hash_function=h, hash_helper=hp, mp=mp)
    data = [Data(randint(0, p - 1)) for _ in range(n)]
    start = time.time()
    for d in data:
        table.insert(d)
    end = time.time()
    fp.write(f"Time to insert: {end - start}\n")

    start = time.time()
    table.search(randint(0, p - 1))
    end = time.time()
    fp.write(f"Time to search for random element: {end - start}\n\n\n")


if __name__ == '__main__':
    fp = open("zadatak2_log_r2.txt", "a")

    fp.write("****************************************************************\n\n")
    fp.write("Quadratic probing, h2 as helper:\n\n")

    ################################################

    n = 10000
    # p as the range of int key values
    p = 500
    time_test(n, p, fp, HashTable.h_quad, HashTable.h2)

    ################################################

    n = 50000
    # p as the range of int key values
    p = 1000
    time_test(n, p, fp, HashTable.h_quad, HashTable.h2)

    ################################################

    n = 100000
    # p as the range of int key values
    p = 10000
    time_test(n, p, fp, HashTable.h_quad, HashTable.h2)

    fp.close()

    ################################################
    #
    # table1 = HashTable(11, HashTable.h_quad, hash_helper=HashTable.h2, mp=10)
    #
    # tst = [randint(0, 500) for i in range(21)]
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
    #
    # tst2 = [randint(0, 200) for i in range(5)]
    #
    # for sample in tst2:
    #     if table1.insert(Data(sample)):
    #         print(f"Inserted {sample}")
    #         print(f"Table size {table1.m}")
    #     else:
    #         print(f"{sample} wasn't inserted.")
    #
    # i = 0
    # while i < len(tst2):
    #     if table1.search(tst2[i]):
    #         print(f"Found {tst2[i]}")
    #     else:
    #         print(f"{tst2[i]} not found.")
    #     i += 1
    #
    # print("bp")
