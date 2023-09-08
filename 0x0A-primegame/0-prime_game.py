def isWinner(x, nums):
    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def canWin(num):
        if num == 1:
            return False
        return not is_prime(num)

    winners = {"Maria": 0, "Ben": 0}

    for n in nums:
        if canWin(n):
            winners["Maria" if n % 2 == 0 else "Ben"] += 1

    if winners["Maria"] > winners["Ben"]:
        return "Maria"
    elif winners["Ben"] > winners["Maria"]:
        return "Ben"
    else:
        return None