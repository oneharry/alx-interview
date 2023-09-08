#!/usr/bin/python3
""" Prime game """


def isWinner(x, nums):
    """Determine winner"""
    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def canWin(n, memo):
        if n in memo:
            return memo[n]

        if n == 1:
            memo[n] = False
        else:
            memo[n] = False
            for i in range(2, n):
                if is_prime(i) and n % i == 0 and not canWin(n - i, memo):
                    memo[n] = True
                    break

        return memo[n]

    winners = {"Maria": 0, "Ben": 0}

    for n in nums:
        if canWin(n, {}):
            winners["Maria" if n % 2 == 0 else "Ben"] += 1

    if winners["Maria"] > winners["Ben"]:
        return "Maria"
    elif winners["Ben"] > winners["Maria"]:
        return "Ben"
    else:
        return None