import math


class SumAsYouGo:
    def sumAsYouGo(self, path, maxLen):

        n = len(path)

        def f(index, dp):
            if index == 0:
                return path[index]

            if index < 0:
                return -math.inf

            if dp[index] != -1:
                return dp[index]

            ans = -math.inf
            for j in range(1, k + 1):
                ans = max(ans, path[index] + f(index - j, dp))

            dp[index] = ans

            return ans

        dp = [0 for i in range(n + 1)]
        dp[0] = -math.inf
        dp[1] = path[0]

        for i in range(2, n + 1):

            ans = -math.inf

            for j in range(1, k + 1):
                if i - j >= 0:
                    ans = max(ans, path[i - 1] + dp[i - j])

            dp[i] = ans

        return dp[n]


if __name__ == "__main__":

    sg = SumAsYouGo()

    path = [100, -70, -90, -80, 100]
    path = [10, -20, -5]
    k = 2

    print(sg.sumAsYouGo(path, k))
