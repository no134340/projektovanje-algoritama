"""
Module: Correctness test module.
        Test if the arrays are sorted.
Author: Jasmina Saivić RA40/2017
  Date: 18.03.2020.
"""
if __name__ == '__main__':
    from merge_module import merge_sort
    from quicksort_module import randomized_quicksort, quicksort
    import random

    print("Randomized quick:")
    trues = []
    for i in range(2, 20):
        arr = [random.randint(-50, 150) for x in range(i)]
        randomized_quicksort(arr, 0, len(arr) - 1)
        trues.append(all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1)))

    print("Are all sorted? {}".format(all(trues)))

    print("Regular quick:")
    trues = []
    for i in range(2, 20):
        arr = [random.randint(-50, 150) for x in range(i)]
        quicksort(arr, 0, len(arr) - 1)
        trues.append(all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1)))
    print("Are all sorted? {}".format(all(trues)))

    print("Merge:")
    trues = []
    for i in range(2, 20):
        arr = [random.randint(-50, 150) for x in range(i)]
        merge_sort(arr, 0, len(arr) - 1)
        trues.append(all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1)))
    print("Are all sorted? {}".format(all(trues)))
