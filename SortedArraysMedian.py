import sys
import math


class SortedArraysMedian:

    def sortedArraysMedian(self, nums1, nums2):

        if len(nums2) <= len(nums1):
            return self.sortedArraysMedian(nums2, nums1)

        m = len(nums1)
        n = len(nums2)

        low = 0
        high = m
        total = (m + n + 1)//2

        answer = 0

        while low <= high:
            mid = (low + high) // 2

            cut1 = mid
            cut2 = total - cut1

            l1 = -math.inf if cut1 == 0 else nums1[cut1 - 1]
            l2 = -math.inf if cut2 == 0 else nums2[cut2 - 1]
            r1 = math.inf if cut1 == m else nums1[cut1]
            r2 = math.inf if cut2 == n else nums2[cut2]

            if l1 <= r2 and l2 <= r1:
                if (m + n) % 2 == 0:

                    answer = (max(l1, l2) +
                              min(r1, r2)) / 2
                    break
                else:
                    answer = max(l1, l2)
                    break
            elif l1 > r2:
                high = mid - 1
            else:
                low = mid + 1
        return float(answer)


if __name__ == "__main__":
    sam = SortedArraysMedian()
    nums1 = [1]
    nums2 = [1]
    m = len(nums1)
    n = len(nums2)

    print(sam.sortedArraysMedian(nums1, nums2))
