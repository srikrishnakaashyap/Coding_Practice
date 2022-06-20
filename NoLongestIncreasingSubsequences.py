from tokenize import Number


class NumberOfSub:

    def findNumberOfLIS(self, nums):
        n = len(nums)
        dp = [1 for i in range(n)]
        cnt = [1 for i in range(n)]
        maxi = 1

        for i in range(n):

            for j in range(i):

                if nums[i] > nums[j] and dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
                    cnt[i] = cnt[j]
                elif nums[i] > nums[j] and dp[j] + 1 == dp[i]:
                    cnt[i] += cnt[j]

            maxi = max(maxi, dp[i])

        answer = 0

        for i in range(n):
            if dp[i] == maxi:
                answer += cnt[i]

        return answer


if __name__ == "__main__":

    num = NumberOfSub()

    nums = [1, 3, 5, 4, 7]

    print(num.findNumberOfLIS(nums))
