import math


class JumpGame2:
    def jumpGame2(self, nums):
        answer = math.inf

        def minJumps(index):
            print(index)
            if index == len(nums) - 1:
                return 0

            if index >= len(nums):
                return math.inf

            jumps = math.inf
            # print(index, index + nums[index] + 1)
            for i in range(1, min(len(nums), nums[index] + 1)):

                # if nums[i] != 0:
                jumps = min(jumps, 1 + minJumps(index + i))

            return jumps

        return minJumps(0)


if __name__ == "__main__":
    jg = JumpGame2()

    nums = [1, 2, 0, 1]

    print(jg.jumpGame2(nums))
