from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:

        #         def f(index, dp):
        #             if index < 0:
        #                 return 0

        #             if index == 0:
        #                 return nums[index]

        #             if dp[index] != -1:
        #                 return dp[index]

        #             pick = nums[index] + f(index - 2, dp)
        #             nopick = f(index-1, dp)

        #             dp[index] = max(pick, nopick)

        #             return max(pick, nopick)

        n = len(nums)
        if n == 1:
            return nums[0]

        dp = [0 for i in range(n)]
        dp[0] = max(nums[0], 0)
        dp[1] = max(nums[0], nums[1], 0)

        for i in range(2, n):
            # dp[i] = max(dp[i - 1], nums[i] + dp[i - 2], 0)
            dp[i] = max(max(dp[i - 1], nums[i] + dp[i - 2]), nums[i])

        return dp[n - 1]


if __name__ == "__main__":

    s = Solution()

    nums = [10**5, -(10**5), 1, -100, -500, 2]

    print(s.rob(nums))
