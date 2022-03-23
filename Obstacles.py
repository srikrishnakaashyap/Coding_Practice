import os


class Obstacles:

    def f(self, i, j, grid, dp):
        if grid[i][j] == 1:
            return 0

        if i < 0 or j < 0:
            return 0

        if i == 0 and j == 0:
            return 1

        if dp[i][j] != -1:
            return dp[i][j]

        left = self.f(i - 1, j, grid, dp)
        top = self.f(i, j - 1, grid, dp)

        dp[i][j] = left + top
        return dp[i][j]

    def obstacles(self, obstacleGrid):
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[-1 for i in range(n)]for j in range(m)]

        # dp[0][0] = 1

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0 and obstacleGrid[i][j] != 1:
                    dp[i][j] = 1
                else:
                    if obstacleGrid[i][j] != 1:
                        left = 0
                        right = 0
                        if i > 0:
                            left = dp[i - 1][j]
                        if j > 0:
                            right = dp[i][j - 1]

                        dp[i][j] = left + right
                    else:
                        dp[i][j] = 0

        return dp[m - 1][n - 1]


if __name__ == "__main__":

    grid = [[1]]
    o = Obstacles()
    print(o.obstacles(grid))
