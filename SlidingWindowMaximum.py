import collections


class SlidingWindowMaximum:

    def maxSlidingWindow(self, nums, k):
        deque = collections.deque()
        n = len(nums)
        answer = []
        for i in range(n):

            if len(deque) > 0 and deque[0] == i - k:
                deque.popleft()

            while len(deque) > 0 and nums[deque[-1]] < nums[i]:
                deque.pop()

            deque.append(i)

            if i >= k - 1:
                answer.append(nums[deque[0]])

        return answer


if __name__ == "__main__":
    swm = SlidingWindowMaximum()

    nums = [1]
    k = 1

    print(swm.maxSlidingWindow(nums, k))
