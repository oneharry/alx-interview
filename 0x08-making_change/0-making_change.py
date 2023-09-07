#!/usr/bin/python3
"""Interview project"""


def makeChange(coins, total):
    """Implementation of makechange"""
    if total <= 0:
        return 0

    coins.sort(reverse=True)
    change = 0

    for i in range(len(coins)):
        coin = coins[i]
        while coin <= total:
            total -= coin
            change += 1

        if total == 0:
            return change

    return -1
