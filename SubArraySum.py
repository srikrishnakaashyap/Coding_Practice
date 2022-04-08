class SubArraySum:

    def subArraySum(self, nums, k):

        def f(index, target, dp):

            if target == 0:
                return True

            if index == 0:
                if target == nums[index]:
                    return True
                return False

            if dp[index][target] != -1:
                return dp[index][target]

            nopick = f(index-1, target, dp)

            pick = False

            if nums[index] <= target:
                pick = f(index - 1, target - nums[index], dp)

            dp[index][target] = pick or nopick
            return pick or nopick

        n = len(nums)
        dp = [[False for i in range(k + 1)] for j in range(n)]

        for i in range(n):
            dp[i][0] = True

        if nums[0] <= k:
            dp[0][nums[0]] = True

        for i in range(1, n):
            for j in range(1, k + 1):

                notake = dp[i - 1][j]

                take = False
                if nums[i] <= j:
                    take = dp[i - 1][j - nums[i]]

                dp[i][j] = take or notake

        # print(dp)
        return dp[n-1][k]

    def f(self, nums, k):
        n = len(nums)
        dp = [[False for i in range(k + 1)] for j in range(n)]

        for i in range(n):
            dp[i][0] = True

        if nums[0] <= k:
            dp[0][nums[0]] = True

        for i in range(1, n):

            for j in range(1, k + 1):

                nopick = dp[i-1][j]
                pick = False
                if nums[i] <= j:
                    pick = dp[i - 1][j - nums[i]]

                dp[i][j] = pick or nopick

        # print(dp)
        return dp[n - 1][k]


if __name__ == "__main__":

    array = [3, 3, 3, 4, 5]
    target = 9

    s = SubArraySum()

    print(s.subArraySum(array, target))
    print(s.f(array, target))
