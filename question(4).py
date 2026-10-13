"""Sum 12-digit palindromes p for which p + 1 is a perfect square.

Only 124,323 candidate roots; O(1) space for the fixed 12-digit bound.
"""

from math import isqrt


def palindrome_sum():
    # 10^11 <= root^2 - 1 <= 10^12 - 1. Integer roots avoid rounding.
    lower = isqrt(10**11) + 1
    upper = isqrt(10**12)
    total = 0

    # Every even-length decimal palindrome is divisible by 11.
    # Thus root^2 == 1 (mod 11), so root == 1 or -1 (mod 11).
    for residue in (1, 10):
        first = lower + (residue - lower) % 11
        for root in range(first, upper + 1, 11):
            candidate = root * root - 1
            digits = str(candidate)
            if digits == digits[::-1]:
                total += candidate
    return total


if __name__ == "__main__":
    print(palindrome_sum())
