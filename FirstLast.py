class Solution:
    def searchRange(self, nums, target):

        # mid = 0
        # if(len)

        def startIndexBinarySearch(start, end):
            if(start < end):
                mid = start + (end - start) // 2
                # print(mid)
                if(nums[mid] == target):
                    if(mid > 0 and nums[mid - 1] == target):
                        return startIndexBinarySearch(start, mid)
                    return mid

                if(nums[mid] > target):
                    return startIndexBinarySearch(start, mid)
                return startIndexBinarySearch(mid + 1, end)
            return -1

        def endIndexBinarySearch(start, end):
            if(start < end):
                mid = start + (end - start) // 2
                # print(mid)
                if(nums[mid] == target):
                    if(mid + 1 < len(nums) and nums[mid + 1] == target):
                        return endIndexBinarySearch(mid + 1, end)
                    return mid

                if(nums[mid] > target):
                    return endIndexBinarySearch(start, mid)
                return endIndexBinarySearch(mid + 1, end)
            return -1

        startIndex = startIndexBinarySearch(0, len(nums))
        if startIndex == -1:
            return [-1, -1]

        endIndex = endIndexBinarySearch(0, len(nums))

        return[startIndex, endIndex]


if __name__ == "__main__":

    s = Solution()

    print(s.searchRange([1, 3, 4, 5], 1))
