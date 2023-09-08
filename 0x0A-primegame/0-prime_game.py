#!/usr/bin/python3
""" Prime game """


def isWinner(x, nums):
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

    def canWin(n, primes, memo):
        if n in memo:
            return memo[n]

        for prime in primes:
            if prime > n:
                break
            if not canWin(n - prime, primes, memo):
                memo[n] = True
                return True

        memo[n] = False
        return False

    winners = {"Maria": 0, "Ben": 0}
    max_num = max(nums)
    primes = calculate_primes(max_num)

    for n in nums:
        if canWin(n, primes, {}):
            winners["Maria" if n % 2 == 1 else "Ben"] += 1

    if winners["Maria"] > winners["Ben"]:
        return "Maria"
    elif winners["Ben"] > winners["Maria"]:
        return "Ben"
    else:
        return "Ben"