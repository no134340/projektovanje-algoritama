"""
Module: Quicksort module.
        Randomized quicksort and regular quicksort.
        Correctness test of both on a random number array (uniform distribution).
        Execution time test on random numbers (uniform distribution).
Author: Jasmina Savić RA40/2017
  Date: 18.03.2020.
"""
import random


def partition(arr, p, r):
    pivot = arr[r]
    i = p - 1
    for j in range(p, r):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    i += 1
    arr[i], arr[r] = arr[r], arr[i]
    return i


def randomized_partition(arr, p, r):
    i = random.randint(p, r)
    arr[i], arr[r] = arr[r], arr[i]
    return partition(arr, p, r)


def randomized_quicksort(arr, p, r):
    if p < r:
        q = randomized_partition(arr, p, r)
        randomized_quicksort(arr, p, q - 1)
        randomized_quicksort(arr, q + 1, r)


def quicksort(arr, p, r):
    if p < r:
        q = partition(arr, p, r)
        quicksort(arr, p, q - 1)
        quicksort(arr, q + 1, r)


if __name__ == '__main__':
    import time
    from matplotlib import pyplot as plt

    n = list(range(10, 10010, 100))
    times = []
    rand_range = 25000

    print("Randomized quicksort test:\n")
    arr = [random.randint(- 50, 125) for x in range(13)]
    print("The original array is: {}".format(arr))
    randomized_quicksort(arr, 0, len(arr) - 1)
    print("The sorted array is: {}\n".format(arr))

    print("Regular quicksort test:\n")
    arr = [random.randint(1, 125) for x in range(13)]
    print("The original array is: {}".format(arr))
    quicksort(arr, 0, len(arr) - 1)
    print("The sorted array is: {}\n".format(arr))

    print("Wait for the plot...")
    for i in range(len(n)):
        test_arr = [random.randint(1, rand_range) for x in range(n[i])]
        # print("The original array is: {}".format(test_arr))
        start = time.clock()
        randomized_quicksort(test_arr, 0, len(test_arr) - 1)
        end = time.clock()
        times.append(end - start)
        # print("The sorted array is: {}".format(test_arr))
        # print(n[i])

    plt.plot(n, times, 'b')
    plt.ylabel('Time')
    plt.xlabel('Number of elements')
    # plt.show()
    figname = 'quicksort.png'
    plt.savefig(figname)
    print('Plot saved as: ' + figname)
