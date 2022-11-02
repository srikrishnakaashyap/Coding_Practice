#
# @lc app=leetcode id=1011 lang=python3
#
# [1011] Capacity To Ship Packages Within D Days
#

# @lc code=start
from typing import List


class Solution:
    def check(self, weights, days, totalWeight):

        n = len(weights)
        d = 1
        i = 0
        while i < n:
            print(i)
            weight = weights[i]
            j = i + 1
            d += 1
            for j in range(i, n - 1):
                if weights[j] + weight > totalWeight:
                    break
                weight += weights[j]

            i = j

        print(d)
        if d <= days:
            return True
        return False

    def shipWithinDays(self, weights: List[int], days: int) -> int:

        print(self.check(weights, days, 15))
        return True


# @lc code=end
