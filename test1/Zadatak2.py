from random import randint
# python doc says:
# randint(a, b) method of random.Random instance
#     Return random integer in range [a, b], including both end points.

def ChooseNumbers(cnt):
    cnt += 1
    arr = [randint(1, 100) for x in range(3)]
    same = all([arr[i] == arr[i + 1] for i in range(2)])
    if same:
        print(f'Finally the same numbers were picked after {cnt} iterations.')
        print(f'The numbers are {arr}')
    return same, cnt


if __name__ == '__main__':
    cnt = 0
    same = False
    while not same:
        same, cnt = ChooseNumbers(cnt)
