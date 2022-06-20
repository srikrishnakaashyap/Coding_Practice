import math


class MatrixChainMultiplication:

    def matrixChainMultiplication(self, arr):

        def f(i, j, arr, dp):
            if i == j:
                return 0
            if dp[i][j] != -1:
                return dp[i][j]

            mini = math.inf
            for k in range(i, j):
                steps = (arr[i-1] * arr[k] * arr[j]) + \
                    f(i, k, arr, dp) + f(k + 1, j, arr, dp)
                # nonlocal answer
                mini = min(mini, steps)

            dp[i][j] = mini
            return mini

        n = len(arr)
        dp = [[-1 for i in range(n)] for j in range(n)]
        answer = f(1, n-1, arr, dp)
        return answer


if __name__ == "__main__":

    mcm = MatrixChainMultiplication()
    nums = [4, 5, 3, 2]

    print(mcm.matrixChainMultiplication(nums))
