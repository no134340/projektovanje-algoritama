"""
Zadatak 3 - Counting sort
Autor:
    Jasmina Savić RA40/2017
Datum:
    24.03.2020.
"""


def counting_sort(arr, ret, k):
    temp = [0 for i in range(k + 1)]
    for val in arr:
        temp[val] += 1
    for i in range(1, len(temp)):
        temp[i] += temp[i - 1]
    for i in range(len(arr) - 1, -1, -1):
        ret[temp[arr[i]] - 1] = arr[i]
        temp[arr[i]] -= 1


if __name__ == '__main__':
    import random
    import time

    print("*****Counting sort*****")
    n, k = 1000, 2000
    sorted_arr = [0 for i in range(n)]
    arr = [random.randint(0, k) for i in range(n)]
    print(f"Original array:\n{arr}")
    start = time.time()
    counting_sort(arr, sorted_arr, k)
    end = time.time()
    print(f"Array after sorting:\n{sorted_arr}")
    print(f"Sorting time: {end - start}")
    is_true = all(
        [sorted_arr[i] <= sorted_arr[i + 1] for i in range(len(arr) - 1)])
    print(f"Sorted? {is_true}")
