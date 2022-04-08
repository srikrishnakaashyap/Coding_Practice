from numpy import outer


class Triangle:

    # def f()

    def triangle(self, triangle):

        n = len(triangle)

        dp = [[-1 for i in range(n)] for j in range(n)]

        def f(outer_index, inner_index, dp):

            if outer_index == n - 1:
                return triangle[outer_index][inner_index]

            if dp[outer_index][inner_index] != -1:
                return dp[outer_index][inner_index]
            same_index = triangle[outer_index][inner_index] + \
                f(outer_index + 1, inner_index, dp)

            next_index = triangle[outer_index][inner_index] + \
                f(outer_index + 1, inner_index + 1, dp)

            dp[outer_index][inner_index] = min(same_index, next_index)
            return dp[outer_index][inner_index]

        return f(0, 0, dp)

    def triangle_tab(self, triangle):

        n = len(triangle)

        dp = [[-1 for i in range(n)] for j in range(n)]

        # dp[0][0] = triangle[0][0]

        for j in range(0, n):
            dp[n - 1][j] = triangle[n-1][j]

        for i in range(n - 2, -1, -1):

            for j in range(i, -1, -1):
                left = triangle[i][j] + dp[i + 1][j]
                right = triangle[i][j] + dp[i + 1][j+1]
                dp[i][j] = min(left, right)

        return dp[0][0]


if __name__ == "__main__":

    triangle = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]

    t = Triangle()

    # print(t.triangle(triangle))

    print(t.triangle_tab(triangle))
