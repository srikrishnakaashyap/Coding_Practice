class UniquePaths:

    def f(self, m, n, dp):
        if m == 0 and n == 0:
            return 1
        if m < 0 or n < 0:
            return 0

        if dp[m][n] != -1:
            return dp[m][n]

        top = self.f(m - 1, n, dp)
        left = self.f(m, n - 1, dp)
        dp[m][n] = top + left
        return dp[m][n]

    def uniquePaths(self, m, n):

        dp = [0 for i in range(n)]

        # dp[0] = 1

        for i in range(0, m):
            temp = [0 for k in range(n)]
            for j in range(0, n):
                if i == 0 and j == 0:
                    temp[0] = 1
                else:

                    top = 0
                    left = 0
                    if i > 0:
                        top = dp[j]
                    if j > 0:
                        left = temp[j - 1]
                    temp[j] = top + left
            dp = temp

        return dp[n-1]
        # pass


if __name__ == "__main__":

    m = 3
    n = 7

    up = UniquePaths()

    print(up.uniquePaths(m, n))
