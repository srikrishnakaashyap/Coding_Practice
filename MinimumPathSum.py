class MinimumPathSum:

    def minimumPathSum(self, grid):

        # answer = 0
        m = len(grid)
        n = len(grid[0])
        dp = [[-1 for i in range(n)] for j in range(m)]
        # answer = f(m - 1, n - 1, dp)

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    dp[i][j] = grid[i][j]
                else:

                    top = 20000
                    left = 20000

                    if i > 0:
                        top = grid[i][j] + dp[i - 1][j]
                    if j > 0:
                        left = grid[i][j] + dp[i][j - 1]

                    dp[i][j] = min(top, left)
        return dp[m-1][n-1]


if __name__ == "__main__":

    mps = MinimumPathSum()

    grid = [[1, 2, 3], [4, 5, 6]]

    print(mps.minimumPathSum(grid))
