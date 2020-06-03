"""
Module: Merge sort.
        Correctness test on a random number array (uniform distribution).
        Merge sort execution time test on random numbers (uniform distribution).
Author: Jasmina Savić RA40/2017
  Date: 18.03.2020.
"""

import math


def merge(arr, p, q, r):
    left = list(arr[p:r + 1])
    left.append(math.inf)
    right = list(arr[r + 1:q + 1])
    right.append(math.inf)
    lind, rind = 0, 0
    for i in range(p, q + 1):
        if left[lind] > right[rind]:
            arr[i] = right[rind]
            rind += 1
        else:
            arr[i] = left[lind]
            lind += 1


def merge_sort(arr, p, q):
    if p < q:
        div = (q + p) // 2
        merge_sort(arr, p, div)
        merge_sort(arr, div + 1, q)
        merge(arr, p, q, div)


if __name__ == '__main__':
    import random
    import time
    from matplotlib import pyplot as plt

    n = list(range(13, 10010, 100))
    times = []
    rand_range = 20000

    arr = [random.randint(-50, 125) for x in range(13)]
    print("The original array is: {}".format(arr))
    merge_sort(arr, 0, len(arr) - 1)
    print("The sorted array is: {}".format(arr))

    print("Wait for the plot...")
    for i in range(len(n)):
        test_arr = [random.randint(1, rand_range) for x in range(n[i])]
        # print("The original array is: {}".format(test_arr))
        start = time.clock()
        merge_sort(test_arr, 0, len(test_arr) - 1)
        end = time.clock()
        times.append(end - start)
        # print("The sorted array is: {}".format(test_arr))
        # print(n[i])

    plt.plot(n, times, 'b')
    plt.ylabel('Time')
    plt.xlabel('Number of elements')
    # plt.show()
    figname = 'merge_sort.png'
    plt.savefig(figname)
    print('Plot saved as: ' + figname)
