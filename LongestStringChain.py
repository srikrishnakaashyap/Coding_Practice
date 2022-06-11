class LongestStringChain:

    def longestStringChain(self, words):
        n = len(words)
        dp = [1 for i in range(n)]
        maxi = 1

        words = sorted(words, key=lambda x: len(x))

        for i in range(n):
            for j in range(i):
                if self.compare(words[i], words[j]) == True and dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1

            if dp[i] > maxi:
                maxi = dp[i]

        return maxi

    def compare(self, word1, word2):

        m = len(word1)
        n = len(word2)

        if m != n + 1:
            return False

        i, j = 0, 0
        while(i < m):
            if j < n and word1[i] == word2[j]:
                i += 1
                j += 1
            else:
                i += 1

        if i == m and j == n:
            return True
        else:
            return False


if __name__ == "__main__":

    lsc = LongestStringChain()

    words = ["xbc", "pcxbcf", "xb", "cxbc", "pcxbc"]

    print(lsc.longestStringChain(words))
