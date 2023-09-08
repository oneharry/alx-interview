def isWinner(x, nums):
    def sieve_erathosthenes(n):
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

    def canWin(num, primes):
        if num in primes:
            return True
        for prime in primes:
            if num % prime == 0:
                return True
        return False

    max_num = max(nums)
    primes = sieve_erathosthenes(max_num)

    dp = [0] * (max_num + 1)
    dp[0] = 0
    dp[1] = 0

    for i in range(2, max_num + 1):
        if canWin(i, primes):
            dp[i] = 1

    winners = {"Maria": 0, "Ben": 0}
    for n in nums:
        winners["Maria" if dp[n] == 1 else "Ben"] += 1

    if winners["Maria"] > winners["Ben"]:
        return "Maria"
    elif winners["Ben"] > winners["Maria"]:
        return "Ben"
    else:
        return None
