#!/usr/bin/env python3
""" Minimum operation """


def minOperations(n: int) -> int:
    if n == 1:
        return 0

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return minOperations(i) + (n // i)

    return n
