# Advent of Code 2024 Day 3

import re


pattern = r'mul\(\d+,\d+\)'


def multiply_and_add(data):
    total = 0
    for line in data:
        for equation in line:
            factors = re.findall(r'\d+', equation)
            total += int(factors[0]) * int(factors[1])

    return total


def filter_input(data):
    matches = []
    for line in data:
        matches.append(re.findall(pattern, line))

    return matches


def read_file(filename):
    with open(filename, 'r') as file:
        return file.readlines()


def main():
    data = read_file('input2.txt')
    matches = filter_input(data)
    total = multiply_and_add(matches)

    print('total: ', total)


if __name__ == "__main__":
    main()
