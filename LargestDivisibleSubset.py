class LargestDivisibleSubset:

    def largestDivisibleSubset(self, nums):
        n = len(nums)
        dp = [1 for i in range(n)]
        temp = [i for i in range(n)]
        maxi = 1
        val = 0
        nums.sort()

        for i in range(n):
            for j in range(i):
                if nums[i] % nums[j] == 0 and dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
                    temp[i] = j

            if dp[i] > maxi:
                val = i
                maxi = dp[i]

        answer = [nums[val]]
        nextval = temp[val]
        while(val != nextval):
            val = nextval
            nextval = temp[val]
            answer.append(nums[val])

        return answer


        # pass
if __name__ == "__main__":

    lds = LargestDivisibleSubset()

    nums = [1, 2, 3]

    print(lds.largestDivisibleSubset(nums))
