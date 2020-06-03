def generate_string(arr):
    res = ''
    for val in arr:
        if val == 0:
            res += ''
        else:
            # formula za ispis "trougla" utvrđena: eksperimentalno
            res += str(val) + ' ' * (len(arr) // 10 + 1)
    return res


def make_pascal_triangle(height):
    arr = [0] * (height + 1)
    arr[-2] = 1
    cnt = height
    while cnt != 0:
        out_str = generate_string(arr)
        # formula za ispis "trougla" utvrđena: eksperimentalno
        print(f'{out_str:^{height*(height // 2)}}')
        tmp = list(arr)
        arr = [tmp[i] + tmp[i+1] for i in range(len(tmp) - 1)]
        arr.append(0)
        cnt -= 1


if __name__ == '__main__':
    try:
        while True:
            height = int(input('Unesite visinu Paskalovog trougla: '))
            if(height < 1):
                print(f'Unesite ceo broj veći od 0.')
                continue
            print()
            make_pascal_triangle(height)
            break
    except ValueError:
        print(f'Nevalidan unos.')
