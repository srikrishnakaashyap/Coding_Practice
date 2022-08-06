class CountSquareSubmatrices:

    def countSquares(self, matrix):

        m = len(matrix)
        n = len(matrix[0])
        dp = [[0 for i in range(n)] for j in range(m)]

        for i in range(m):
            dp[i][0] = matrix[i][0]

        for i in range(n):
            dp[0][i] = matrix[0][i]

        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] != 0:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1

        answer = 0
        for i in dp:
            for j in i:
                answer += j
        return answer


if __name__ == "__main__":

    css = CountSquareSubmatrices()

    matrix = [
        [0, 1, 1, 1],
        [1, 1, 1, 1],
        [0, 1, 1, 1]]

    print(css.countSquares(matrix))
