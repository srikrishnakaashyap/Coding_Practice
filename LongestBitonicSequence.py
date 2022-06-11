class LongestBitonicSequence:

    def longestBitonicSequence(self, nums):

        n = len(nums)
        dp1 = [1 for i in range(n)]
        dp2 = [1 for i in range(n)]

        for i in range(n):
            for j in range(i):

                if nums[i] > nums[j] and dp1[j] + 1 > dp1[i]:
                    dp1[i] = dp1[j] + 1

        for i in range(n-1, -1, -1):
            for j in range(n-1, i, -1):

                if nums[i] > nums[j] and dp2[j] + 1 > dp2[i]:
                    dp2[i] = dp2[j] + 1

        maxi = 1

        for i in range(n):
            if dp1[i] != 1 and dp2[i] != 1:
                maxi = max(maxi, dp1[i] + dp2[i] - 1)

        return len(nums) - maxi


if __name__ == "__main__":

    lbs = LongestBitonicSequence()

    nums = [9, 8, 1, 7, 6, 5, 4, 3, 2, 1]

    print(lbs.longestBitonicSequence(nums))
