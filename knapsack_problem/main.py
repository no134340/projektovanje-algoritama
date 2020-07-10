from math import inf


def knapsack(v, w, n, W):
    W += 1
    n += 1
    V = [-inf] * (W * n)
    for i in range(W):
        V[i] = 0
    for i in range(1, n):
        for j in range(W):
            if w[i] <= j:
                V[i * W + j] = max(V[(i - 1) * W + j], v[i] + V[(i - 1) * W + (j - w[i])])
            else:
                V[i * W + j] = V[(i - 1) * W + j]
    return V[(n - 1) * W + W - 1]


if __name__ == '__main__':
    # value and weight at index 0 are auxiliary and needed for this implementation to work
    # maybe one day when i remember that this problem exists and actually have the will to
    # debug this i will solve it and have it work without those. but today is not the day.

    v = [0, 10, 40, 30, 50]
    w = [inf, 5, 4, 6, 3]
    n = 4
    W = 10
    print(knapsack(v, w, n, W))
