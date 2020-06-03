"""
Module: Test execution times.
        Test execution times of randomized quicksort vs merge sort on
        random number arrays (uniform distribution).
Author: Jasmina Savić RA40/2017
  Date: 18.03.2020.
"""

if __name__ == '__main__':
    from merge_module import merge_sort
    from quicksort_module import randomized_quicksort
    import random
    import time
    from matplotlib import pyplot as plt

    n = list(range(10, 50010, 200))
    times_quick = []
    rand_range = 30000

    for i in range(len(n)):
        test_arr = [random.randint(-rand_range, rand_range) for x in range(n[i])]
        start = time.clock()
        randomized_quicksort(test_arr, 0, len(test_arr) - 1)
        end = time.clock()
        times_quick.append(end - start)
        print(n[i])

    times_merge = []
    for i in range(len(n)):
        test_arr = [random.randint(-rand_range, rand_range) for x in range(n[i])]
        start = time.clock()
        merge_sort(test_arr, 0, len(test_arr) - 1)
        end = time.clock()
        times_merge.append(end - start)
        print(n[i])

    plt.plot(n, times_quick, 'b', n, times_merge, 'g')
    plt.ylabel('Time')
    plt.xlabel('Number of elements')
    labels = ['uniform distribution - quick']
    labels.append('uniform distribution - merge')
    plt.legend(labels)
    # plt.show()
    figname = 'quick_vs_merge.png'
    plt.savefig(figname)
    print('Plot saved as: ' + figname)
