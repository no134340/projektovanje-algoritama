def insertion(A):
    for i in range(1, len(A)):
        j = i - 1
        key = A[i]
        while j >= 0 and A[j] > key:
            A[j + 1] = A[j]
            j -= 1
        A[j + 1] = key


if __name__ == '__main__':
    import random

    rand_range = 50
    size = 23
    A = [random.randrange(1, rand_range) for i in range(size)]
    print("Array A: " + str(A))
    insertion(A)
    print("Array A sorted: " + str(A))