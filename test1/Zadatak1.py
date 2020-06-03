def GetHistogram(char_list):
    histogram = {}
    for char in char_list:
        histogram[char] = histogram.get(char, 0) + 1
    return histogram


if __name__ == '__main__':
    char_list = ['a', 'a', 'a', 'b', 'b', 'c', 'a', 'c', 'd']
    histogram = GetHistogram(char_list)
    print(histogram)
