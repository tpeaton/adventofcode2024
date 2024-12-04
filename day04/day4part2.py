# Advent of Code 2024 Day 4 part 2

class nowrap_list(list):
    """Prevents index lookups using negative numbers from wrapping around."""
    def __getitem__(self, n):
        if n < 0:
            raise IndexError('Index wrapping not supported')
        return list.__getitem__(self, n)


def is_x_mas(data, a_row, a_col):
    first_diagonal = []
    second_diagonal = []

    try:
        first_diagonal = sorted([
            data[a_row - 1][a_col - 1],
            data[a_row + 1][a_col + 1]
        ])
        second_diagonal = sorted([
            data[a_row + 1][a_col - 1],
            data[a_row - 1][a_col + 1]
        ])

        if first_diagonal == second_diagonal == ['M', 'S']:
            return True
    except IndexError:
        return False
    return False


def count_x_max(data):
    total = 0

    for i, row in enumerate(data):
        for j, letter in enumerate(row):
            if letter == 'A':
                if is_x_mas(data, i, j):
                    total += 1

    return total


def read_file(filename):
    data = nowrap_list()

    with open(filename, 'r') as file:
        for line in file:
            data.append(nowrap_list(line))

    return data


def main():
    data = read_file('input2.txt')
    print('total: ', count_x_max(data))


if __name__ == "__main__":
    main()
