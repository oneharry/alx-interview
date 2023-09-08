#!/usr/bin/python3
""" Prime game """


def isWinner(x, nums):
    """Determines the winner of the game"""
    def is_prime(num):
        if num <= 1:
            return False
        if num <= 3:
            return True
        if num % 2 == 0 or num % 3 == 0:
            return False
        i = 5
        while i * i <= num:
            if num % i == 0 or num % (i + 2) == 0:
                return False
            i += 6
        return True

    def find_primes_up_to_n(n):
        primes = []
        for i in range(2, n + 1):
            if is_prime(i):
                primes.append(i)
        return primes

    def play_round(n):
        primes = find_primes_up_to_n(n)
        maria_turn = True
        while n > 0:
            can_remove = False
            for prime in primes:
                if prime <= n:
                    n -= prime
                    can_remove = True
                    break
            if not can_remove:
                break
            maria_turn = not maria_turn
        return "Maria" if maria_turn else "Ben"

    winners = {"Maria": 0, "Ben": 0}
    for n in nums:
        round_winner = play_round(n)
        winners[round_winner] += 1

    if winners["Maria"] > winners["Ben"]:
        return "Maria"
    elif winners["Ben"] > winners["Maria"]:
        return "Ben"
    else:
        return None
