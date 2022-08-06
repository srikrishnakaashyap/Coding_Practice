class CountSmallerThanSelf:

    def countSmaller(self, nums):
        self.ans = [0]*len(nums)

        def merge(arr, start, mid, end):
            temp_1, temp_2 = arr[start: mid + 1], arr[mid + 1: end + 1]
            i, j, k = 0, 0, start
            count = 0
            while i < len(temp_1) and j < len(temp_2):
                if temp_1[i][0] <= temp_2[j][0]:
                    self.ans[temp_1[i][1]] += count
                    arr[k] = temp_1[i]
                    i += 1
                else:
                    count += 1
                    arr[k] = temp_2[j]
                    j += 1
                k += 1

            while i < len(temp_1):
                self.ans[temp_1[i][1]] += count
                arr[k] = temp_1[i]
                i += 1
                k += 1

            while j < len(temp_2):
                arr[k] = temp_2[j]
                j += 1
                k += 1

        def mergesort(arr, start, end):
            if start < end:
                mid = (start + end) // 2
                mergesort(arr, start, mid)
                mergesort(arr, mid + 1, end)
                merge(arr, start, mid, end)

        for i in range(len(nums)):
            nums[i] = [nums[i], i]

        print(nums)
        mergesort(nums, 0, len(nums) - 1)
        return self.ans


if __name__ == "__main__":

    cs = CountSmallerThanSelf()

    nums = [5, 2, 6, 1]

    print(cs.countSmaller(nums))
