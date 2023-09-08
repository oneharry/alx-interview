#!/usr/bin/python3
""" Prime game """


def isWinner(x, nums):
    """ determoine who is the winner"""
    def calculate_primes(n):
        is_prime = [True] * (n + 1)
        is_prime[0] = is_prime[1] = False
        p = 2
        while p * p <= n:
            if is_prime[p]:
                for i in range(p * p, n + 1, p):
                    is_prime[i] = False
            p += 1
        primes = [i for i in range(2, n + 1) if is_prime[i]]
        return primes

    max_num = max(nums)
    primes = calculate_primes(max_num)

    dp = [0] * (max_num + 1)

    for i in range(2, max_num + 1):
        can_win = False
        for prime in primes:
            if i - prime >= 0 and dp[i - prime] == 0:
                can_win = True
                break
        dp[i] = 1 if can_win else 0

    winners = {"Maria": 0, "Ben": 0}
    for n in nums:
        winners["Maria" if dp[n] == 1 else "Ben"] += 1

    if winners["Maria"] > winners["Ben"]:
        return "Ben"
    elif winners["Ben"] > winners["Maria"]:
        return "Maria"
    else:
        return None
