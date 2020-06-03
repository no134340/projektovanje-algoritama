import random
import time
from matplotlib import pyplot as plt


def LCS(S, n, T, m):
    if n == -1 or m == -1:
        return 0
    if S[n] == T[m]:
        return 1 + LCS(S, n - 1, T, m - 1)
    else:
        return max(LCS(S, n - 1, T, m), LCS(S, n, T, m - 1))


def random_char():
    return chr(random.randint(65, 90))


def lcs_length(X, Y):
    m = len(X)
    n = len(Y)
    b = []
    for j in range(m + 1):
        h = list()
        b.append(h)
        for i in range(n + 1):
            h.append(0)
    c = []
    for j in range(m + 1):
        h = list()
        c.append(h)
        for i in range(n + 1):
            h.append(0)
    # print(b)
    # print(c)
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                c[i][j] = c[i - 1][j - 1] + 1
                row = b[i]
                row[j] = "diag"
            elif c[i - 1][j] >= c[i][j - 1]:
                c[i][j] = c[i - 1][j]
                row = b[i]
                row[j] = "up"
            else:
                c[i][j] = c[i][j - 1]
                row = b[i]
                row[j] = "left"
    return c, b


def print_lcs(b, X, i, j):
    if i == 0 or j == 0:
        return
    if b[i][j] == "diag":
        print_lcs(b, X, i - 1, j - 1)
        print(X[i-1])
    elif b[i][j] == "up":
        print_lcs(b, X, i - 1, j)
    else:
        print_lcs(b, X, i, j - 1)

def plot_time(fun, filename, beg, stop):
    times = []
    lens = []
    cnt = stop
    for i in range(beg, cnt):
        S = [random_char() for _ in range(1, i)]
        T = S[random.randint(0, len(S) // 5): len(S) - random.randint(0, len(S) // 8) - 1]
        if len(T) > 3:
            for _ in range(0, 2):
                T.remove(T[random.randint(len(T) // 4, len(T) // 4 * 3)])
        for _ in range(0, 4):
            T.insert(random.randint(len(T) // 4, len(T) // 4 * 3), random_char())
        print(f"S: {S}")
        print(f"T: {T}")
        lens.append([f"({len(S)},{len(T)})"])
        start, end = 0, 0
        if fun == LCS:
            start = time.time()
            print(fun(S, len(S) - 1, T, len(T) - 1))
            end = time.time()
        else:
            start = time.time()
            print(fun(S, T))
            end = time.time()
        times.append(end - start)

    fig = plt.figure(figsize=(10, 10), dpi=200)
    plt.rc('xtick', labelsize=5)
    ax = fig.add_subplot(1, 1, 1)  # create an axes object in the figure
    ax.set_xlim(0, stop - beg)
    ax.set_xticks(range(0, 100))
    plt.xticks(range(0, (stop - beg) * 10, 10), lens, rotation='vertical')
    plt.ylabel('Vreme trazenja LCS')
    plt.xlabel('Duzine stringova ')

    plt.plot(range(0, (stop - beg) * 10, 10), times)
    plt.savefig(filename + '.png', dpi=200)


if __name__ == '__main__':
    # Zadatak 1
    # plot_time(LCS, 'zadatak1', 10, 20)

    # Zadatak 2
    # plot_time(lcs_length, 'zadatak2', 20, 100)

    # Zadatak 3
    X = "abcbdab"
    Y = "bdcaba"
    c, b = lcs_length(X, Y)
    print_lcs(b, X, len(X), len(Y))