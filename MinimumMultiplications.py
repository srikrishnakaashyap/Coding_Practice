# User function Template for python3

from typing import List
import math
from collections import deque


class MinimumMultiplications:
    def minimumMultiplications(self, arr: List[int], start: int, end: int) -> int:

        start = start % 100000
        end = end % 100000
        distance = [math.inf for i in range(100000)]

        distance[start] = 0

        queue = deque()

        queue.append((0, start))

        while queue:
            elem = queue.pop()
            dist = elem[0]
            node = elem[1]
            for i in range(len(arr)):
                val = (arr[i] * node) % 100000
                if distance[val] > dist + 1:
                    distance[val] = dist + 1
                    queue.append((dist + 1, val))

        return distance[end]


# {
# Driver Code Starts
# Initial Template for Python 3

if __name__ == "__main__":

    mm = MinimumMultiplications()

    arr = [2, 5, 7]
    start = 3
    end = 30

    print(mm.minimumMultiplications(arr, start, end))
# } Driver Code Ends
