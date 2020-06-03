"""
Module: Test execution times.
        Test execution times of heap vs bucket vs counting sort on
        random number arrays (uniform distribution).
Author: Jasmina Savić RA40/2017
  Date: 24.03.2020.
"""

if __name__ == '__main__':
    from heap_sort import heap_sort
    from bucket_sort import bucket_sort
    from counting_sort import counting_sort
    from bubble_sort import bubble_sort
    from insertion import insertion
    from quicksort_module import quicksort
    from merge_module import merge_sort
    import random
    import time
    from matplotlib import pyplot as plt

    n = list(range(10, 50000, 100))
    rand_range = 60000

    times_counting = []
    for i in range(len(n)):
        test_arr = [random.randint(0, rand_range) for x in range(n[i])]
        sorted_arr = [0 for x in range(n[i])]
        start = time.time()
        counting_sort(test_arr, sorted_arr, rand_range)
        end = time.time()
        times_counting.append(end - start)
        print(n[i])

    times_bucket = []
    for i in range(len(n)):
        test_arr = [random.randint(0, rand_range) for x in range(n[i])]
        start = time.time()
        bucket_sort(test_arr)
        end = time.time()
        times_bucket.append(end - start)
        print(n[i])

    times_merge = []
    for i in range(len(n)):
        test_arr = [random.randint(-rand_range, rand_range) for x in range(n[i])]
        start = time.time()
        merge_sort(test_arr, 0, len(test_arr) - 1)
        end = time.time()
        times_merge.append(end - start)
        print(n[i])

    times_quick = []
    for i in range(len(n)):
        test_arr = [random.randint(-rand_range, rand_range) for x in range(n[i])]
        start = time.time()
        quicksort(test_arr, 0, len(test_arr) - 1)
        end = time.time()
        times_quick.append(end - start)
        print(n[i])

    times_heap = []
    for i in range(len(n)):
        test_arr = [random.randint(-rand_range, rand_range) for x in range(n[i])]
        start = time.time()
        heap_sort(test_arr)
        end = time.time()
        times_heap.append(end - start)
        print(n[i])
    #
    # times_insertion = []
    # for i in range(len(n)):
    #     test_arr = [random.randint(-rand_range, rand_range) for x in range(n[i])]
    #     start = time.time()
    #     insertion(test_arr)
    #     end = time.time()
    #     times_insertion.append(end - start)
    #     print(n[i])
    #
    # times_bubble = []
    # for i in range(len(n)):
    #     test_arr = [random.randint(-rand_range, rand_range) for x in range(n[i])]
    #     start = time.time()
    #     bubble_sort(test_arr)
    #     end = time.time()
    #     times_bubble.append(end - start)
    #     print(n[i])

    plt.plot(n, times_counting, 'magenta', n, times_bucket, 'g', n, times_merge, 'r', n, times_quick, 'cyan', n, times_heap, 'b')
    plt.ylabel('Time')
    plt.xlabel('Number of elements')
    labels = ['counting', 'bucket', 'merge', 'quick', 'heap']
    plt.legend(labels)
    # plt.show()
    figname = 'algorithm_comparison_n_and_nlogn.png'
    plt.savefig(figname)
    print('Plot saved as: ' + figname)
