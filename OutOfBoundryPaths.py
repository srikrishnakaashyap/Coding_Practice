class OutOfBoundryPaths:

    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int):

        def f(i, j, moves, dp):

            if moves < 0:
                return 0

            if i < 0 or j < 0 or i >= m or j >= n:
                return 1

            if dp[i][j][moves] != -1:
                return dp[i][j][moves]

            if moves == 1:
                if m == 1 and n == 1:
                    return 4

                elif m == 1 or n == 1:

                    if(i == 0 and j == 0) or (i == 0 and j == n-1) or (i == m-1 and j == 0) or (i == m-1 and j == n-1):
                        # print(i, j)
                        return 3

                    elif i == 0 or j == 0 or i == m-1 or j == n-1:
                        return 2
                    else:
                        return 1

                elif m >= 2 and n >= 2:

                    if (i == 0 and j == 0) or (i == m-1 and j == n-1) or (i == 0 and j == n - 1) or (i == m-1 and j == 0):
                        return 2
                    else:
                        if i == 0 or i == m-1 or j == 0 or j == n-1:
                            return 1
                        else:
                            return 0

            top = f(i-1, j, moves-1, dp)
            bottom = f(i + 1, j, moves-1, dp)
            left = f(i, j-1, moves-1, dp)
            right = f(i, j+1, moves-1, dp)

            dp[i][j][moves] = (top + bottom + left + right) % ((10**9) + 7)

            return dp[i][j][moves]

        dp = [[[-1 for i in range(maxMove + 1)] for j in range(n + 1)]
              for k in range(m + 1)]

        return f(startRow, startColumn, maxMove, dp)


if __name__ == "__main__":

    obp = OutOfBoundryPaths()

    m = 1
    n = 2
    maxMove = 50
    startRow = 0
    startColumn = 0

    print(obp.findPaths(m, n, maxMove, startRow, startColumn))
