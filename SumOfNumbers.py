import math


class SumOfNumbers:

    def minimumNumbers(self, num, k):

        if num == 0:
            return 0

        if k == 0 and num % 10 == 0:
            return 1
        elif k == 0 and num % 10 != 0:
            return -1

        def f(index, amt, dp, coins):
            if amt == 0:
                return 0

            if index < 0:
                return math.inf

            if dp[index][amt] != -1:
                return dp[index][amt]

            nopick = f(index - 1, amt, dp, coins)
            pick = math.inf
            if coins[index] <= amt:
                pick = 1 + f(index, amt - coins[index], dp, coins)

            dp[index][amt] = min(pick, nopick)

            return min(pick, nopick)

        lst = []

        for i in range(k, num+1, 10):
            lst.append(i)

        dp = [[-1 for i in range(num + 1)] for j in range(len(lst))]

        answer = f(len(lst) - 1, num, dp, lst)

        if answer == math.inf:
            return -1
        return answer


if __name__ == "__main__":
    som = SumOfNumbers()

    num = 37
    k = 2

    print(som.minimumNumbers(num, k))
