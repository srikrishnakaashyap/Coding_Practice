class SESA:

    def singleNonDuplicate(self, nums):
        answer = 0
        n = len(nums)
        start = 0
        end = n - 1
        mid = -1
        while(start < end):

            mid = start + ((end - start) // 2)
            if nums[mid] != nums[mid + 1] and nums[mid] != nums[mid - 1]:
                return nums[mid]
            if mid % 2 == 0:
                if nums[mid] == nums[mid - 1]:
                    end = mid - 1
                else:
                    start = mid + 1
            else:
                if nums[mid] == nums[mid + 1]:
                    end = mid - 1
                else:
                    start = mid + 1

        return nums[start]


if __name__ == "__main__":

    s = SESA()
    nums = [1, 1, 2, 3, 3, 4, 4, 8, 8]
    nums2 = [3, 3, 7, 7, 10, 11, 11]
    print(s.singleNonDuplicate(nums))
    print(s.singleNonDuplicate(nums2))
