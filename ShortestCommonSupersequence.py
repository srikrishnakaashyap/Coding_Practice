class ShortestCommonSupersequence:

    def shortestCS(self, str1, str2):
        m = len(str1)
        n = len(str2)
        dp = [[0 for i in range(n + 1)] for j in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):

                if str1[i-1] == str2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        i = m
        j = n
        answer = ""
        while(i > 0 and j > 0):

            if str1[i-1] == str2[j-1]:
                answer += str1[i-1]
                i -= 1
                j -= 1
            elif dp[i-1][j] > dp[i][j-1]:
                answer += str1[i-1]
                i -= 1
            else:
                answer += str2[j-1]
                j -= 1

        while i > 0:
            answer += str1[i-1]
            i -= 1

        while j > 0:
            answer += str2[j-1]
            j -= 1

        return answer[::-1]


if __name__ == "__main__":

    scs = ShortestCommonSupersequence()

    str1 = "abac"
    str2 = "cab"
    print(scs.shortestCS(str1, str2))
