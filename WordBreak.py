class WordBreak:

    def wordBreak(self, s, wordDict):
        answer = False
        n = len(s)

        def f(start, end, dp):

            if end == n:
                if s[start:end] in wordDict:
                    return True
                else:
                    return False
            if dp[start][end] != -1:
                return dp[start][end]

            print(s[start:end+1])
            if s[start:end+1] in wordDict:
                dp[start][end] = f(start, end + 1, dp) or f(end+1, end+1, dp)
                return dp[start][end]
            else:
                dp[start][end] = f(start, end + 1, dp)
                return dp[start][end]

        n = len(s)
        dp = [[-1 for i in range(n)] for j in range(n)]
        for i in range(0, n):
            dp[0][i] = True if s[0:i+1] in wordDict else False

        for i in range(1, n):
            for j in range(1, n):
                if s[i:j + 1] in wordDict:
                    dp[i][j] = dp[i-1][j] or dp[i-1][i-1]
                else:
                    dp[i][j] = dp[i-1][j]

        return dp[n-1][n-1]


if __name__ == "__main__":

    wb = WordBreak()

    s = "leetcode"
    wordDict = ["leet", "code"]

    print(wb.wordBreak(s, wordDict))
