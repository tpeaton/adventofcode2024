# Advent of Code 2024 Day 2


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
    total_count = 0
    safe_count = 0

    with open('input.txt', 'r') as file:
        for record in file:
            record = [int(x) for x in record.split()]
            total_count += 1

            print('analyzing record:', record)
            if is_safe(record, verbose=False):
                safe_count += 1
                print('SAFE')
            else:
                print('NOT SAFE')

    print('total records: ', total_count)
    print('safe records: ', safe_count)

if __name__ == "__main__":
    main()
