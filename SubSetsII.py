class SubSetsII:

    def subsetsWithDup(nums):

        ans = []
        n = len(nums)

        nums = sorted(nums)

        def permutations(index, array):

            # if index >= n:
            ans.append(array.copy())
            # return
            for i in range(index, n):
                if i > index and nums[i] == nums[i-1]:
                    # array.append(nums[])
                    continue

                array.append(nums[i])
                # ans.append(array.copy())
                permutations(i + 1, array)
                array.pop()

        permutations(0, [])

        return ans

    if __name__ == "__main__":

        nums1 = [1, 2, 2]
        nums2 = [0]

        # obj = SubSetsII()

        print(subsetsWithDup(nums1))
        print(subsetsWithDup(nums2))
