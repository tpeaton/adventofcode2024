# Advent of Code 2024 Day 4

import re


pattern = r'XMAS'


def count_matches(data):
    total = 0

    # Forward
    total += len(re.findall(pattern, data))
    # Backward
    total += len(re.findall(pattern, data[::-1]))

    return total


def horizontal_matches(data):
    total = 0

    for row in data:
        total += count_matches(row)

    return total


def vertical_matches(data):
    total = 0

    for index in range(len(data[0]) - 1):
        column = ''.join([col[index] for col in data])
        total += count_matches(column)
    return total


def diagonal_matches(data):
    total = 0

    diagonals = []
    m, n = len(data), len(data[0])

    for k in range(m + n - 1):
        temp = []
        i = max(0, k - n + 1)
        j = min(k, n - 1)

        while i < m and j >= 0:
            temp.append(data[i][j])
            i += 1
            j -= 1
        else:
            total += count_matches(''.join(temp))

    return total


def read_file(filename):
    with open(filename, 'r') as file:
        return file.readlines()


def main():

    data = read_file('input2.txt')

    total = 0
    total += horizontal_matches(data)
    total += vertical_matches(data)
    total += diagonal_matches(data)
    total += diagonal_matches([l[::-1] for l in data])

    print('total: ', total)


if __name__ == "__main__":
    main()
