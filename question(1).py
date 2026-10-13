"""Trailing zeroes of n!: O(log_5(n)) time and O(1) space."""


def trailing_zeroes(n):
    # Each factor of 5 pairs with an available factor of 2 to make 10.
    total = 0
    while n >= 5:
        n //= 5
        total += n
    return total


if __name__ == "__main__":
    print(trailing_zeroes(int(input())))
