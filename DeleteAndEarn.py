class DeleteAndEarn:

    def deleteAndEarn(self, nums):

        def f(index, h, dp):

            if index == 0:
                if h.get(nums[index], 0) == 0 or h.get(nums[index] - 1, 0) == 0 or h.get(nums[index] + 1, 0) in h:
                    return 0
                else:
                    return nums[index]

            if dp[index] != -1:
                return dp[index]

            nopick = f(index - 1, h, dp)
            pick = 0
            if(h.get(nums[index]) == 1) or (h.get(nums[index], 0) == 0 and h.get(nums[index] - 1, 0) == 0 and h.get(nums[index] + 1, 0) == 0):
                h[nums[index]] = 1
                pick = nums[index] + f(index - 1, h, dp)
                h[nums[index]] = 0

            dp[index] = max(pick, nopick)
            return max(pick, nopick)

        h = {}
        n = len(nums)
        dp = [-1 for i in range(n)]

        return f(n - 1, h, dp)


if __name__ == "__main__":

    nums = [2, 2, 3, 3, 3, 4]

    de = DeleteAndEarn()

    print(de.deleteAndEarn(nums))
