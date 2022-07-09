import math


class FrogJumps:

    def minimumJumps(self, arr, n):
        dp = [math.inf for i in range(n)]

        def f(presentIndex, dp):
            # print(presentIndex)
            if presentIndex == n-1:
                return 0

            if presentIndex >= n:
                return math.inf

            if dp[presentIndex] != math.inf:
                return dp[presentIndex]

            mini = math.inf
            for i in range(1, arr[presentIndex] + 1):
                jump = 1 + f(presentIndex + i, dp)
                if jump != math.inf:
                    mini = min(mini, jump)

                print(presentIndex, jump)

            dp[presentIndex] = min(dp[presentIndex], mini)
            return dp[presentIndex]

        answer = f(0, dp)
        if answer == math.inf:
            return -1
        return answer

    def frogJumps(self, n, heights, k):

        temp = [0 for i in range(n)]

        for i in range(1, n):

            ans = 10**9
            for j in range(i - 1, i - k - 1, -1):
                if j < 0:
                    break
                te = temp[j] + abs(heights[i] - heights[j])
                ans = min(ans, te)
            temp[i] = ans
            ans = 10**9
        return temp[n - 1]


if __name__ == "__main__":

    f = FrogJumps()

    # n = len(arr)

    # print(f.frogJumps(n, arr, k))
    arr = [2, 1, 3, 2, 4]
    n = len(arr)

    print(f.minimumJumps(arr, n))
