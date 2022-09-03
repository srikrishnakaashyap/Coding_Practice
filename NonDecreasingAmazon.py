class NonDecreasing:
    def nonDecreasing(self, nums):

        toAdd = 0

        n = len(nums)
        for i in range(1, n):
            if nums[i] + toAdd < nums[i - 1]:
                toAdd += nums[i - 1] - nums[i]

        return toAdd


if __name__ == "__main__":

    nd = NonDecreasing()

    nums = [3, 4, 1, 1, 2]

    print(nd.nonDecreasing(nums))
