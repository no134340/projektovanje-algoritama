"""
Zadatak 2 - Bucket sort (with floating point values in interval [0,1))
Autor:
    Jasmina Savić RA40/2017
Datum:
    24.03.2020.
"""
from math import floor


def insertion_sort(t):
    for i in range(1, len(t)):
        j = i - 1
        key = t[i]
        while j >= 0 and t[j] > key:
            t[j + 1] = t[j]
            j -= 1
        t[j + 1] = key


def bucket_sort(arr):
    n = len(arr)
    temp = [[] for x in range(n)]
    for i in range(n):
        temp[floor(arr[i] * n)].append(arr[i])
    arr.clear()
    for t in temp:
        insertion_sort(t)
        print(f'Bucket: {t}')
        for val in t:
            arr.append(val)


if __name__ == '__main__':
    import random
    import time

    print("*****Bucket sort*****")
    n = 100
    arr = [random.uniform(0, 0.99999999) for i in range(n)]
    print(f"Original array:\n{arr}")
    start = time.time()
    bucket_sort(arr)
    end = time.time()
    print(f"Array after sorting:\n{arr}")
    print(f"Sorting time: {end - start}")
    is_true = all(
        [arr[i] <= arr[i + 1] for i in range(len(arr) - 1)])
    print(f"Sorted? {is_true}")
