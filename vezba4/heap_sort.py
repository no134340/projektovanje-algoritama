"""
Zadatak 1 - Heap sort
Autor:
    Jasmina Savić RA40/2017
Datum:
    24.03.2020.
"""


def left(i):
    return 2 * i + 1


def right(i):
    return 2 * i + 2


def parent(i):
    return (i - 1) // 2


def build_max_heap(arr):
    global heap_size
    for i in range(heap_size // 2, -1, -1):
        max_heapify(arr, i)


def max_heapify(arr, i):
    global heap_size
    l = left(i)
    r = right(i)

    largest = i

    if l <= (heap_size - 1) and arr[l] > arr[i]:
        largest = l
    if r <= (heap_size - 1) and arr[r] > arr[largest]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        max_heapify(arr, largest)


def heap_sort(arr):
    global heap_size
    build_max_heap(arr)

    # test if the heap is built correctly
    print(f"Max heap: {arr}")
    is_true = all(
        [arr[parent(i)] >= arr[left(i)] and arr[parent(i)] >= arr[right(i)]] for i in range(len(arr) // 2 - 1))
    print(f"Heap? {is_true}")

    for i in range(heap_size - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heap_size -= 1
        max_heapify(arr, 0)


if __name__ == '__main__':
    import random
    import time

    print("*****Heap sort*****")
    rand_range = 500
    arr_size = 100
    arr = [random.randint(1, rand_range) for i in range(arr_size)]
    heap_size = len(arr)
    print(f"Original array:\n{arr}")
    start = time.time()
    heap_sort(arr)
    end = time.time()
    print(f"Sorted increasing order using heap sort on max heap:\n{arr}")
    print(f"Execution time: {end - start}")

    is_true = all(
        [arr[i] <= arr[i + 1] for i in range(len(arr) - 1)])
    print(f"Sorted? {is_true}")
