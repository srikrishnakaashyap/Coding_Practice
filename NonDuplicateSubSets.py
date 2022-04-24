class NonDuplicateSubsets:

    def nonDuplicateSubsets(self, nums):

        ans = []
        n = len(nums)
        nums = sorted(nums)

        def permutations(index, array):

            ans.append(array[:])
            for i in range(index, n):
                if i > index and nums[i] == nums[i-1]:
                    continue

                array.append(nums[i])
                permutations(i + 1, array)
                array.pop()

        permutations(0, [])

        return ans


if __name__ == "__main__":

    nds = NonDuplicateSubsets()

    arr = [1, 2, 2]
    print(nds.nonDuplicateSubsets(arr))
