import math


class MatrixMaximumPathSum:

    def f(self, row, column, matrix, dp, path):

        if row < 0 or column < 0 or row >= len(matrix) or column >= len(matrix[0]):
            return -10**5

        if row == 0:
            return matrix[row][column]

        if dp[row][column] != -10**5:
            return dp[row][column]

        path.append([row, column])
        down = matrix[row][column] + self.f(row-1, column, matrix, dp, path)
        down_left = matrix[row][column] + \
            self.f(row-1, column-1, matrix, dp, path)
        down_right = matrix[row][column] + \
            self.f(row-1, column+1, matrix, dp, path)

        dp[row][column] = max(down, down_left, down_right)

        # print(row, column, down, down_left, down_right, path)

        return dp[row][column]

    def matrixMaximumPathSum(self, matrix):

        answer = -math.inf

        m = len(matrix)
        n = len(matrix[0])

        dp = [[-10**5 for i in range(n)] for j in range(m)]

        # print(dp)

        for i in range(n):
            answer = max(answer, self.f(m - 1, i, matrix, dp, []))
            # print(answer, i)

        return answer


if __name__ == "__main__":

    matrix = [[1, 2, 10, 4], [100, 3, 2, 1], [1, 1, 20, 2], [1, 2, 2, 1]]

    matrix2 = [[1, 0, 0, 0, 0], [0, 1, 0, 0, 0],
               [0, 0, 1, 0, 0], [0, 0, 0, 1, 0], [0, 0, 0, 0, 1]]

    matrix3 = [[-9999, -9888, -9777, -9666, -9555],
               [1, 10, 2, 4, 5],
               [-9999, -9888, -9777, -9666, -9555],
               [0, 0, 0, 0, 0],
               [-99, -98, -97, -96, -95]]

    mps = MatrixMaximumPathSum()

    print(mps.matrixMaximumPathSum(matrix))

    print(mps.matrixMaximumPathSum(matrix3))
