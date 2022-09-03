import math


class SumAsYouGo:
    def sumAsYouGo(self, path, maxLen):

        n = len(path)
        dp = [-1 for i in range(n)]

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

        return f(n - 1, dp)


if __name__ == "__main__":

    sg = SumAsYouGo()

    path = [100, -70, -90, -80, 100]
    k = 3

    print(sg.sumAsYouGo(path, k))
