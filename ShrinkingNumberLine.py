import math


class ShrinkingNumberLine:

    def shirinkingNumberLine(self, point, k):
        point = sorted(point)

        n = len(point)
        ans = point[n-1] - point[0]

        minimum = point[0] + k
        maximum = point[n-1] - k

        current_min = math.inf
        current_max = -math.inf

        for i in range(0, n-1):
            current_min = min(minimum, point[i+1] - k)

            current_max = max(maximum, point[i] + k)

            if current_min >= 0:
                ans = max(ans, current_max - current_min)

        return ans


if __name__ == "__main__":
