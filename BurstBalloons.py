class BurstBalloons:
    def maxCoins(self, nums):
        def getValue(arr, index):
            if index < 0 or index >= len(arr):
                return 1
            return arr[index]

        def multiply(arr, index, h):
            left = index - 1

            while left >= 0 and h[left]:
                left -= 1

            right = index + 1

            while right < len(arr) and h[right]:
                right += 1

            return getValue(arr, left) * getValue(arr, index) * getValue(arr, right)

        h = [False for i in range(len(nums))]

        def f(index, array, h):

            if index < 0:
                print(h)
                return 0

            pick = 0
            if not h[index]:
                h[index] = True
                pick = multiply(array, index, h) + f(index - 1, array, h)
                h[index] = False

            nopick = f(index - 1, array, h)

            # print(pick, nopick)

            return max(pick, nopick)

        n = len(nums)

        return f(n - 1, nums, h)


if __name__ == "__main__":

    bb = BurstBalloons()

    nums = [3, 1, 5, 8]

    print(bb.maxCoins(nums))
