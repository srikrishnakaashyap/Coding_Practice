class EditDistance:

    def match(self, a, b):
        if a == b:
            return 0
        return 3

    def editDistance(self, str1, str2):

        m = len(str1)
        n = len(str2)
        dp = [[0 for i in range(n)]for j in range(m)]

        for i in range(1, m):
            dp[0][i] = i

        for j in range(1, n):
            dp[j][0] = j

        dp[0][0] = 0

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = min(1 + dp[i-1][j], 1 + dp[i][j - 1],
                               self.match(str1[i], str2[j]) + dp[i-1][j-1])

        for i in dp:
            print(i)
        return dp[m-1][n-1]


if __name__ == "__main__":

    ed = EditDistance()

    str1 = "startrek"
    str2 = "starwars"

    print(ed.editDistance(str2, str1))
