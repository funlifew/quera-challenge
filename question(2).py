"""Magic square: O(n^2) time and O(n) auxiliary space."""

import sys


def is_magic(n, values):
    columns = [0] * n
    main_diagonal = other_diagonal = 0
    target = None
    for row in range(n):
        row_sum = 0
        for col in range(n):
            value = next(values)
            row_sum += value
            columns[col] += value
            if row == col:
                main_diagonal += value
            if row + col == n - 1:
                other_diagonal += value
        if target is None:
            target = row_sum
        elif row_sum != target:
            return False
    return (
        main_diagonal == other_diagonal == target
        and all(total == target for total in columns)
    )


def main():
    # Accept arbitrary whitespace without retaining the whole matrix.
    values = (int(token) for line in sys.stdin.buffer for token in line.split())
    n = next(values)
    print("YES" if is_magic(n, values) else "NO")


if __name__ == "__main__":
    main()
