#!/usr/bin/env python
# coding: utf-8
from collections import Counter

if __name__ == "__main__":
    data = [
        15, 14, 14, 18, 13, 3, 1, 3, 7, 23, 17, 20, 2, 22, 21, 12, 10, 22, 9, 6,
        25, 21, 1, 19, 23, 22, 21, 7, 25, 19, 23, 22, 18, 9, 2, 18, 6, 16, 13, 19,
        6, 11, 17, 8, 11, 7, 18, 13, 9, 14, 18, 17, 20, 22, 13, 17, 4, 19, 1, 13,
        24, 7, 13, 11, 21, 5, 2, 25, 11, 15, 24, 23, 4, 21, 24, 22, 4, 9, 12, 20,
        9, 11, 19, 15, 17, 14, 19, 1, 21, 25, 4, 13, 4, 19, 21, 14, 12, 9, 12, 3,
        5, 15, 18, 25, 25, 18
    ]

    most_common = Counter(data).most_common(5)
    print("5 numbers that occur most often in the set:")
    for number, count in most_common:
        print(f"{number}: {count} occurrences")
