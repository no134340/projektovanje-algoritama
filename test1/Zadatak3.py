from math import sqrt, ceil


def CalculateSum(number):
    sum = 0
    number = abs(number)
    while number != 0:
        sum += number % 10
        number //= 10
    return sum


def IsPrime(number):
    # 0 i 1 po definiciji nisu prosti brojevi (takođe, prosti brojevi su po definiciji pozitivni)
    if number < 1:
        return False
    for x in range(2, ceil(sqrt(number)) + 1):
        if number % x == 0 and number != x:  # ovo number!=x tu stoji zbog broja 2
            return False
    return True


if __name__ == '__main__':
    number_dict = {}
    try:
        while True:
            number = int(input())
            digit_sum = CalculateSum(number)
            is_prime = IsPrime(number)
            number_dict[number] = tuple([digit_sum, is_prime])
    except ValueError:
        print(number_dict)
