import math


class DistinctRollSequence:

    def gcd(self, a, b):
        if b == 0:
            return a
        return self.gcd(b, a % b)

    def distinctSequence(self, n):

        def f(ind, prev, secondPrev, dp):
            if ind == n:
                return 1

            if dp[ind][prev][secondPrev] != -1:
                return dp[ind][prev][secondPrev]

            ans = 0
            for i in range(1, 7):
                if(i != prev and i != secondPrev and math.gcd(i, prev) == 1) or prev == 0:
                    ans = (ans + f(ind + 1, i, prev, dp)) % ((10**9) + 7)

            dp[ind][prev][secondPrev] = ans

            return ans

        answer = 0

        dp = [[[-1 for i in range(7)] for j in range(7)] for k in range(n)]
        # for i in range(1, 7):
        answer = f(0, 0, 0, dp)

        return (answer % ((10**9) + 7))


if __name__ == "__main__":

    drs = DistinctRollSequence()

    n = 4

    print(drs.distinctSequence(n))
