from math import inf


def cut_rod(p, n, cuts):
    if n == 0:
        return 0
    q = -inf
    ind = 0
    for i in range(n):
        cut = p[i] + cut_rod(p, n - i - 1, cuts)
        if q < cut:
            q = cut
            ind = n - i - 1
    cuts[n - 1] = ind
    return q


def memoized_cut_rod_aux(p, n, r, cuts):
    if r[n - 1] >= 0:
        return r[n - 1]
    ind = 0
    if n == 0:
        q = 0
    else:
        q = -inf
        for i in range(n):
            price = p[i] + memoized_cut_rod_aux(p, n - i - 1, r, cuts)
            if price > q:
                q = price
                ind = n - i - 1
    cuts[n - 1] = ind
    r[n - 1] = q
    return q


def memoized_cut_rod(p, n):
    r = [-inf] * (n + 1)
    cuts = [0] * n
    price = memoized_cut_rod_aux(p, n, r, cuts)
    return price, cuts


def bottom_up_cut_rod(p, n):
    r = [-inf] * (n + 1)
    cuts = [0] * n
    r[0] = 0
    cuts[0] = 0
    for j in range(1, n + 1):
        q = -inf
        ind = 0
        for i in range(j):
            price = p[i] + r[j - i - 1]
            if price > q:
                q = price
                ind = j - i - 1
        cuts[j - 1] = ind
        r[j] = q
    return r[n], cuts


def cut_rod_original(pieces, n):
    cuts = [0] * n
    price = cut_rod(pieces, n, cuts)
    return price, cuts


def find_cuts_place(cuts, n):
    chunks = []
    m = n
    while m > 0:
        if cuts[m - 1] != m - 1:
            chunks.append(cuts[m - 1])
        m = cuts[m - 1]
    chunks.reverse()
    m = cuts[n - 1]
    div = n - m
    while m != m + cuts[div - 1]:
        if cuts[div] != div:
            chunks.append(div + cuts[m - 1])

    return chunks


if __name__ == '__main__':
    pieces = [1, 5, 8, 9, 10, 12, 13, 20, 21, 22]
    price, cuts = 0, None

    # visualize the problem a bit
    print(f"Find the places to cut a rod at to get the maximum price.\n")
    print(f"The rod is of length {len(pieces)}.")
    print(f"It can be cut at following places:\n")
    rod = "|    "
    cuts_indices = "0"
    for i in range(len(pieces)):
        rod += f"{'|':5}"
        cuts_indices += f"{i + 1:5}"
    print(rod)
    print(cuts_indices)
    print()

    print("Prices of the chunks with their respective length are:\n")
    indices = f"{'Index |':>15}"
    prices = f"{'Chunk size |':>15}"
    for i, price in enumerate(pieces):
        indices += f"{i:5}"
        prices += f"{pieces[i]:5}"
    print(indices)
    print("-" * len(indices))
    print(prices)
    print()

    # regular recursive approach:
    print("Regular recursive approach:")
    price, cuts = cut_rod_original(pieces, len(pieces))
    print(f"Price for n = {len(pieces)}: {price}. Cuts prices list: {pieces}\n")

    # memoized top-bottom approach
    print("Top-bottom with memoization:")
    price, cuts = memoized_cut_rod(pieces, len(pieces))
    print(f"Price for n = {len(pieces)}: {price}. Cuts prices list: {pieces}\n")

    # dynamic programming approach - memoization bottom-top
    print("Bottom-top with memoization:")
    price, cuts = bottom_up_cut_rod(pieces, len(pieces))
    print(f"Price for n = {len(pieces)}: {price}. Cuts prices list: {pieces}\n")

    print("The rod should be cut at places:")
    print(find_cuts_place(cuts, len(pieces)))
