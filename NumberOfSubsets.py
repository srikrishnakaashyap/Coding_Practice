class NumberOfSubsets:

    def numberOfWays(self, nums, tar):
        answer = 0

        def f(index, target, dp):

            if target == 0:
                return 1

            if index == 0:
                return 1 if target == nums[index] else 0

            if dp[index][target] != -1:
                return dp[index][target]

            nopick = f(index - 1, target, dp)
            pick = 0
            if nums[index] <= target:
                pick = f(index - 1, target - nums[index], dp)

            dp[index][target] = pick + nopick
            return pick + nopick

        n = len(nums)
        dp = [[-1 for i in range(tar + 1)] for j in range(n)]
        answer = f(n - 1, tar, dp)
        return answer

    def numberOfWaysTabulation(self, nums, tar):

        n = len(nums)
        dp = [[0 for i in range(tar + 1)] for j in range(n)]

        for i in range(n):
            dp[i][0] = 1

        if nums[0] <= tar:
            dp[0][nums[0]] = 1

        for index in range(1, n):
            for target in range(1, tar + 1):
                nopick = dp[index-1][target]
                pick = 0
                if nums[index] <= target:
                    pick = dp[index-1][target-nums[index]]

                dp[index][target] = pick + nopick
        return dp[n-1][tar]


if __name__ == "__main__":
    n = NumberOfSubsets()

    array = [1, 2, 2, 3]

    # print(n.numberOfWays(array, 3))

    print(n.numberOfWaysTabulation(array, 4))
