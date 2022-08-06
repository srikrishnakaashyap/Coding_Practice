class ShortestUnsortedContinuousArray:

    def findUnsortedSubarray(self, nums):

        n = len(nums)

        stack = []

        l = n

        # sorted_array = []

        answer = 0
        j = -1
        for i in range(n):

            while(len(stack) > 0 and nums[stack[-1]] > nums[i]):
                l = min(l, stack.pop(-1))

            stack.append(i)

        stack = []

        r = 0

        for i in range(n-1, -1, -1):

            while(len(stack) > 0 and nums[stack[-1]] < nums[i]):
                r = max(r, stack.pop(-1))

            stack.append(i)

        answer = r - l + 1

        return answer if answer > 0 else 0

        # pass


if __name__ == "__main__":

    suca = ShortestUnsortedContinuousArray()

    nums = [2, 6, 4, 8, 10, 9, 15]

    print(suca.findUnsortedSubarray(nums))
