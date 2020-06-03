def bubble_sort(A):
    change = True
    for i in range(len(A) - 1, -1, -1):
        if not change:
            break
        change = False
        for j in range(i):
            if A[j] > A[j + 1]:
                A[j], A[j + 1] = A[j + 1], A[j]
                change = True


if __name__ == '__main__':
    import random

    rand_range = 50
    size = 23
    A = [random.randrange(1, rand_range) for i in range(size)]
    print("Array A: " + str(A))
    bubble_sort(A)
    print("Array A sorted: " + str(A))
