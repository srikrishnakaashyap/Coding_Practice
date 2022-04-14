class DistinctSubsequences:

    def distinctSubsequences(self, s, t):

        def f(i, j, dp):

            if j < 0:
                return 1
            if i < 0:
                return 0

            if dp[i][j] != -1:
                return dp[i][j]

            if s[i] == t[j]:
                dp[i][j] = f(i-1, j-1, dp) + f(i-1, j, dp)
                return dp[i][j]
            else:
                dp[i][j] = f(i-1, j, dp)
                return dp[i][j]

        m = len(s)
        n = len(t)

        dp = [[0 for i in range(n + 1)] for j in range(m + 1)]

        for i in range(m+1):
            dp[i][0] = 1

        print(dp)

        for i in range(1, m+1):
            for j in range(1, n+1):

                if s[i-1] == t[j-1]:
                    dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j]

        return dp[m][n]


if __name__ == "__main__":
    str1 = "rabbbit"
    str2 = "rabbit"

    ds = DistinctSubsequences()

    print(ds.distinctSubsequences(str1, str2))
