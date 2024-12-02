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


def did_direction_change(num1, num2):
    """Will return True if the numbers are on opposite sides of zero."""
    return (num1 * num2) < 0

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

        if did_direction_change(previous_direction, difference):
            if verbose:
                print('ERROR: direction changed')
            return False

        previous_direction = difference

    return True


def main():

    total_count = 0
    safe_count = 0

    with open('input2.txt', 'r') as file:
        for record in file:
            record = [int(x) for x in record.split()]
            total_count += 1

            print('***************************************************')
            print()
            print('analyzing record:', record)
            if is_safe(record, verbose=True):
                safe_count += 1
                print('SAFE')
            else:
                print('NOT SAFE')
            print()

    print('total records: ', total_count)
    print('safe records: ', safe_count)

if __name__ == "__main__":
    main()
