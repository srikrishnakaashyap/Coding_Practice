class PalindromeSubstrings:

    def palindromeSubstrings(self, string, k):

        isPalindrome = [[False for _ in range(
            len(string))] for _ in range(len(string))]

        def isP(s):

            for i in range(len(s)):
                c = i
                r = 0
                while r < len(s) and c < len(s):

                    if r == c:
                        isPalindrome[r][c] = True
                    else:
                        if s[r] == s[c]:
                            if c - r == 1:
                                isPalindrome[r][c] = True
                            else:
                                isPalindrome[r][c] = isPalindrome[r+1][c-1]
                    r += 1
                    c += 1

        isP(string)

        n = len(string)

        dp = [[-1 for i in range(n)] for j in range(n)]

        def f(i, j, dp):
            if i > j or i > n or j < 0:
                return 0

            if dp[i][j] != -1:
                return dp[i][j]

            if j - i + 1 < k:
                dp[i][j] = max(f(i+1, j, dp), f(i, j-1, dp))
                return dp[i][j]
            else:
                nonlocal isPalindrome
                if isPalindrome[i][j]:
                    pick = 1 + f(j+1, n-1, dp)
                    nopick = max(f(i+1, j, dp), f(i, j-1, dp))

                    dp[i][j] = max(pick, nopick)
                    return max(pick, nopick)
                else:

                    dp[i][j] = max(f(i+1, j, dp), f(i, j-1, dp))
                    return dp[i][j]

        f(0, n-1, dp)

        return dp[0][n-1]


if __name__ == "__main__":

    ps = PalindromeSubstrings()

    # OP = 2
    string = "aababaabce"
    k = 3
    n = len(string)

    print(ps.palindromeSubstrings(string, k))
