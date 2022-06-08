class BestTimeStock:

    def maxProfit(self, prices):

        def f(i, canbuy, dp):

            if i == len(prices):

                return 0

            if dp[i][canbuy] != -1:
                return dp[i][canbuy]
            if canbuy:
                profit = max(-prices[i] +
                             f(i + 1, False, dp), f(i+1, True, dp))

            else:
                profit = max(prices[i] + f(i + 1, True, dp), f(i+1, False, dp))

            dp[i][canbuy] = profit

            return profit

        dp = [[-1 for i in range(2)] for j in range(len(prices))]
        return f(0, True, dp)
        # return answer

    def maxProfitTabulation(self, prices):
        n = len(prices)
        dp = [[-1 for i in range(2)] for j in range(n + 1)]

        dp[n][0] = 0
        dp[n][1] = 0

        for ind in range(n-1, -1, -1):

            for canbuy in range(0, 2):

                if canbuy:
                    profit = max(-prices[ind] + dp[ind+1][0], dp[ind+1][1])

                else:
                    profit = max(prices[ind] + dp[ind+1][1], dp[ind+1][0])

                dp[ind][canbuy] = profit

        return dp[0][1]

    def maxProfitSpace(self, prices):

        n = len(prices)
        prev = [0, 0]

        for ind in range(n-1, -1, -1):
            temp = [-1, -1]

            for canbuy in range(0, 2):

                if canbuy:
                    profit = max(-prices[ind] + prev[0], prev[1])

                else:
                    profit = max(prices[ind] + prev[1], prev[0])

                temp[canbuy] = profit

            prev = temp

        return prev[1]


if __name__ == "__main__":

    s = BestTimeStock()

    prices = [7, 1, 5, 3, 6, 4]

    # print(s.maxProfit(prices))

    print(s.maxProfitSpace(prices))
