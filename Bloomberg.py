def collatz(num, dp):
    if num == 1:
        return 0

    if num in dp:
        return dp[num]

    if num % 2:
        res = 1 + collatz(3 * num + 1, dp)
    else:
        res = 1 + collatz(num // 2, dp)

    dp[num] = res

    return res


dp = {}
print(collatz(5, dp))
print(dp)
