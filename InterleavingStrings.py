class InterleavingStrings:

    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:

        m = len(s1)
        n = len(s2)
        o = len(s3)
        if m + n != o:
            return False

        if m == 0 and n == 0 and o == 0:
            return True

        if m == 0:
            return s2 == s3

        if n == 0:
            return s1 == s3

        def f(m, n, o, dp):

            if m == -1 and n == -1 and o == -1:
                return True

            if s3[o] != s1[m] and s3[o] != s2[n]:
                return False

            if m >= 0 and n >= 0 and o >= 0 and dp[m][n][o] != -1:
                print(dp)
                return dp[m][n][o]

            if m >= 0 and n >= 0 and o >= 0 and s3[o] == s1[m] and s3[o] == s2[n]:

                dp[m][n][o] = f(m-1, n, o-1, dp) or f(m, n-1, o-1, dp)
                return dp[m][n][o]

            if m >= 0 and o >= 0 and s3[o] == s1[m]:

                dp[m][n][o] = f(m-1, n, o-1, dp)
                return dp[m][n][o]

            if n >= 0 and o >= 0 and s3[o] == s2[n]:
                dp[m][n][o] = f(m, n-1, o-1, dp)
                return dp[m][n][o]

        dp = [[[-1 for i in range(o)] for j in range(n)] for k in range(m)]
        # print(dp)

        return f(m-1, n-1, o-1, dp)


if __name__ == "__main__":

    ils = InterleavingStrings()

    s1 = "aabcc"
    s2 = "dbbca"
    s3 = "aadbcbbcac"

    print(ils.isInterleave(s1, s2, s3))
