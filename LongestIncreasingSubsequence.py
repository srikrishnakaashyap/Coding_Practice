class LIS:

    def lis(self, nums):

        n = len(nums)

        dp = [1 for i in range(n)]

        for ind in range(n):

            for prev in range(ind - 1):

                if nums[prev] < nums[ind]:
                    dp[ind] = max(dp[prev] + 1, dp[ind])

        return max(dp)

    def bs(self, nums, value):

        low = 0
        high = len(nums) - 1

        print(nums, value)

        while low < high:

            mid = (low + high)//2
            print(low, mid, high)

            if nums[mid] >= value:
                high = mid
            else:
                low = mid + 1

        print(nums, value, high)
        return high

    def lisBs(self, nums):
        temp = []

        temp.append(nums[0])
        n = len(nums)

        for i in range(1, n):
            if nums[i] > temp[-1]:
                temp.append(nums[i])
            else:
                ind = self.bs(temp, nums[i])
                temp[ind] = nums[i]

        print(temp)

        return len(temp)


if __name__ == "__main__":

    lis = LIS()

    nums = [4, 10, 4, 3, 8, 9]

    print(lis.lisBs(nums))
