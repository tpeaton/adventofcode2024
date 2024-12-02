# Advent of Code 2024 Day 2


def is_difference_too_great(num, max_difference=3, verbose=False):
    if abs(num) > max_difference:
        if verbose:
            print('ERROR: difference too great')
        return True
    return False


def are_numbers_equal(num, verbose=False):
    if num == 0:
        if verbose:
            print('ERROR: adjacent numbers are equal')
        return True
    return False


def did_direction_change(num1, num2, verbose=False):
    """Will return True if the numbers are on opposite sides of zero."""
    direction_changed = (num1 * num2) < 0

    if verbose and direction_changed:
        print('ERROR: direction changed')

    return direction_changed


def is_safe(record, verbose=False):
    previous_direction = record[0] - record[1]

    for pair in zip(record, record[1:]):
        difference = pair[0] - pair[1]

        if verbose:
            print(pair, 'diff:', difference)

        if is_difference_too_great(difference, verbose=verbose):
            return False

        if are_numbers_equal(difference, verbose=verbose):
            return False

        if did_direction_change(previous_direction, difference, verbose=verbose):
            return False

        previous_direction = difference

    return True


def read_file(filename, verbose=False):
    total_count = 0
    safe_count = 0

    with open(filename, 'r') as file:
        for record in file:
            record = [int(x) for x in record.split()]
            total_count += 1

            if verbose:
                print('***************************************************')
                print()
                print('analyzing record:', record)

            if is_safe(record, verbose):
                safe_count += 1
                if verbose:
                    print('SAFE')
            else:
                if problem_dampener(record):
                    safe_count += 1
                if verbose:
                    print('NOT SAFE')

            if verbose:
                print()

    print('total records: ', total_count)
    print('safe records: ', safe_count)


def problem_dampener(record):
    """Retry failing records by removing a single level."""
    for i, r in enumerate(record):
        new_record = record.copy()
        del new_record[i]
        if is_safe(new_record):
            return True
    return False


def main():
    read_file('input.txt', verbose=True)


if __name__ == "__main__":
    main()
