class KDiffPairs:

    def findPairs(self, nums, k):

        nums = sorted(nums)

        n = len(nums)

        i = 0
        j = i + 1
        answer = 0
        while(i < n and j < n):
            # print(nums[j], nums[i], abs(nums[j] - nums[i]))

            if abs(nums[j] - nums[i]) == k:

                counti = 1
                k = i + 1
                while(k < n and nums[k] == nums[i]):
                    k += 1
                    counti += 1

                l = j + 1
                while(l < n and nums[j] == nums[l]):
                    l += 1

                i = k
                j = l

                print(i, j)
                answer += 1
            elif abs(nums[j]) - abs(nums[i]) < k:
                j += 1
            else:
                i += 1
        return answer


if __name__ == "__main__":

    kdp = KDiffPairs()
    nums = [1, 2, 3, 4, 5]
    k = 1

    print(kdp.findPairs(nums, k))
