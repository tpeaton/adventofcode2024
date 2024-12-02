data = [
    [7, 6, 4, 2, 1],  # Safe
    [1, 2, 7, 8, 9],  # Not Safe
    [9, 7, 6, 2, 1],  # Not Safe
    [1, 3, 2, 4, 5],  # Not Safe
    [8, 6, 4, 4, 1],  # Not Safe
    [1, 3, 6, 7, 9],  # Safe
]


def is_safe(record, verbose=False):
    is_descending = False
    is_ascending = False
    position = 0

    for pair in zip(record, record[1:]):

        difference = pair[0] - pair[1]
        if verbose:
            print(pair, 'diff:', difference)

        if abs(difference) > 3:
            if verbose:
                print('FAIL: difference > 3')
            return False
        if difference == 0:
            if verbose:
                print('FAIL: difference == 0')
            return False
        if difference > 0:
            if verbose:
                print('Descending numbers')
            is_descending = True
        else:
            if verbose:
                print('Ascending numbers')
            is_ascending = True

        if is_descending and is_ascending:
            if verbose:
                print('FAIL: direction switched')
            return False

    return True


def main():
    for row in data:
        print('analyzing row:', row)
        print('safe row:', is_safe(row))
        print()


if __name__ == "__main__":
    main()
