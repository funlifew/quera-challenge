"""Sorted frequencies: O(n + k log k) time, O(k) auxiliary space."""

import sys
from collections import Counter
from itertools import islice


def main():
    values = (int(token) for line in sys.stdin.buffer for token in line.split())
    n = next(values)
    counts = Counter(islice(values, n))
    for value in sorted(counts):
        print(f"{value}:{counts[value]}")


if __name__ == "__main__":
    main()
