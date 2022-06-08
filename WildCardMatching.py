class WildCardMatching:

    def wildcardMatching(self, text, pattern):

        i = len(text)
        j = len(pattern)

        def f(i, j, dp):

            if i < 0 and j < 0:
                return True
            if i >= 0 and j < 0:
                return False

            if i < 0 and j >= 0:

                if pattern[0: j+1] == "*"*(j+1):
                    return True
                else:
                    return False

            if dp[i][j] != -1:
                return dp[i][j]

            if text[i] == pattern[j] or pattern[j] == "?":
                dp[i][j] = f(i - 1, j - 1, dp)
                return

            if pattern[j] == "*":

                dp[i][j] = f(i - 1, j, dp) or f(i, j - 1, dp)
                return dp[i][j]
            return False

        dp = [[-1 for x in range(j)] for y in range(i)]

        if i == 0 and j == 0:
            return True

        if len(text) == 0 and len(pattern) >= 0:
            if "*"*len(pattern) == pattern:
                return True
            return False

        if len(pattern) == 0 and len(text) > 0:
            return False

        f(i-1, j-1, dp)

        print("HERE")

        print(dp)

        return dp[i-1][j-1]

    def wildcardMatchingTabulation(self, text, pattern):

        i = len(pattern)
        j = len(text)

        dp = [[-1 for x in range(j + 1)] for y in range(i + 1)]

        dp[0][0] = True

        for x in range(1, j + 1):
            dp[x][0] = True

        for x in range(1, i + 1):
            dp[0][x] = True if pattern == "*"*(x+1) else False

        for m in range(1, i+1):
            for n in range(1, j+1):

                if text[m - 1] == pattern[n - 1] or pattern[n - 1] == "?":
                    dp[m][n] = dp[m-1][n-1]

                elif pattern[n - 1] == "*":
                    dp[m][n] = dp[m-1][n] or dp[m][n-1]

                else:
                    dp[m][n] = False

        return dp[i][j]


if __name__ == "__main__":

    wcm = WildCardMatching()

    text = "ray"
    pattern = "?ay"

    # print(wcm.wildcardMatching(text, pattern))

    print(wcm.wildcardMatchingTabulation(text, pattern))
