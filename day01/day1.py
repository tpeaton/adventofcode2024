# Advent of Code 2024 Day 1


def calculate_similarity_score(list1, list2):
    score = 0
    for num in list1:
        score += num * list2.count(num)

    return score


def sum_difference(list1, list2):
    total_difference = 0
    for i, j in zip(list1, list2):
        total_difference += abs(i - j)

    return total_difference


def read_file(filename, verbose=False):
    list1 = []
    list2 = []

    with open(filename, 'r') as file:
        for record in file:
            record = [int(x) for x in record.split()]
            list1.append(record[0])
            list2.append(record[1])

    return sorted(list1), sorted(list2)


def main():
    list1, list2 = read_file('input.txt')

    # Part One
    total_difference = sum_difference(list1, list2)
    print('total difference: ', total_difference)

    # Part Two
    similarity_score = calculate_similarity_score(list1, list2)
    print('similarity score: ', similarity_score)


if __name__ == "__main__":
    main()
