import math


class CoinChange:

    def coinChange(self, coins, amount):

        answer = 0

        def f(index, amt, dp):
            if amt == 0:
                return 0

            if index < 0:
                return math.inf

            if dp[index][amt] != -1:
                return dp[index][amt]

            nopick = f(index - 1, amt, dp)
            pick = math.inf
            if coins[index] <= amt:
                pick = 1 + f(index, amt - coins[index], dp)

            dp[index][amt] = min(pick, nopick)

            return min(pick, nopick)

        n = len(coins)
        dp = [[0 for i in range(amount + 1)] for j in range(n)]
        # answer = f(n - 1, amount, dp)

        for i in range(amount + 1):
            if i % coins[0] == 0:
                dp[0][i] = i // coins[0]
            else:
                dp[0][i] = math.inf

        for index in range(1, n):
            for amt in range(0, amount + 1):

                nopick = dp[index - 1][amt]
                pick = math.inf
                if coins[index] <= amt:
                    pick = 1 + dp[index][amt - coins[index]]

                dp[index][amt] = min(pick, nopick)

        print(dp)

        if dp[n-1][amount] == math.inf:
            return -1
        return dp[n - 1][amount]

        # return answer


if __name__ == "__main__":

    coins = [1, 2, 5]
    amount = 11

    cc = CoinChange()

    print(cc.coinChange(coins, amount))
