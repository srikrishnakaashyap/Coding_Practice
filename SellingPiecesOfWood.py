class SellingPiecesOfWood:

    def sellingWood(self, m, n, prices):

        def f(m, n, i, dp):

            if m <= 0 or n <= 0:
                return 0

            if i < 0:
                return 0

            if dp[m][n][i] != -1:
                return dp[m][n][i]

            nopick = f(m, n, i-1, dp)

            pick = 0

            if m >= prices[i][0] and n >= prices[i][1]:
                pick1 = prices[i][2] + f(m - prices[i][0], n, i, dp) + \
                    f(prices[i][0], n - prices[i][1], i, dp)

                pick2 = prices[i][2] + f(m, n - prices[i][1], i, dp) + \
                    f(m - prices[i][0], prices[i][1], i, dp)

                pick = max(pick1, pick2)

            dp[m][n][i] = max(pick, nopick)

            return max(pick, nopick)

        dp = [[[0 for i in range(len(prices))]
               for j in range(n + 1)] for k in range(m + 1)]

        # print(dp)

        # answer = f(m, n, len(prices) - 1, dp)
        # return answer

        M = m
        N = n

        for m in range(1, M + 1):
            for n in range(1, N + 1):
                for i in range(len(prices)):
                    nopick = dp[m][n][i-1]

                    pick = 0

                    if m >= prices[i][0] and n >= prices[i][1]:

                        pick1 = 0
                        if m - prices[i][0] >= 0 and n - prices[i][1] >= 0:
                            pick1 = prices[i][2] + dp[m - prices[i][0]
                                                      ][n][i] + dp[prices[i][0]][n - prices[i][1]][i]

                        pick2 = 0

                        if n - prices[i][1] >= 0 and m - prices[i][0] >= 0:

                            pick2 = prices[i][2] + dp[m][n-prices[i][1]
                                                         ][i] + dp[m - prices[i][0]][prices[i][1]][i]

                        pick = max(pick1, pick2)

                    dp[m][n][i] = max(pick, nopick)

        return dp[m][n][len(prices) - 1]


if __name__ == "__main__":

    spw = SellingPiecesOfWood()

    m = 4
    n = 6
    prices = [[3, 2, 10], [1, 4, 2], [4, 1, 3]]

    print(spw.sellingWood(m, n, prices))
