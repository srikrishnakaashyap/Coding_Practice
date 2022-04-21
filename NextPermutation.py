class NextPermutation:

    def nextPermutation(self, nums):

        n = len(nums)
        i = n - 2
        index1 = 0
        while i >= 0:
            if nums[i] < nums[i + 1]:
                index1 = i
                break
            i -= 1

        if i >= 0:
            index2 = 0
            for i in range(n-1, -1, -1):
                if nums[i] > nums[index1]:
                    index2 = i
                    break

            print(index2)

            nums[index1], nums[index2] = nums[index2], nums[index1]

            index1 += 1

        ctr = n - 1
        while(index1 < ctr):
            nums[index1], nums[ctr] = nums[ctr], nums[index1]
            index1 += 1
            ctr -= 1

        return nums


if __name__ == "__main__":

    np = NextPermutation()
    nums = [3, 2, 1]
    print(np.nextPermutation(nums))
