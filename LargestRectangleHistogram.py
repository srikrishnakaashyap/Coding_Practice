class LargestRectangle:

    def largestRectangleArea(self, heights):

        n = len(heights)

        left = [0 for i in range(len(heights))]
        right = [0 for i in range(len(heights))]

        stack = []

        for i in range(n):
            while(len(stack) > 0 and heights[stack[-1]] >= heights[i]):
                stack.pop(-1)

            left[i] = stack[-1] + 1 if len(stack) > 0 else 0

            stack.append(i)

        stack = []

        for i in range(n-1, -1, -1):
            while(len(stack) > 0 and heights[stack[-1]] >= heights[i]):
                stack.pop(-1)

            right[i] = stack[-1] - 1 if len(stack) > 0 else n - 1

            stack.append(i)

        answer = 0

        for i in range(n):
            temp = (right[i] - left[i] + 1) * heights[i]
            answer = max(answer, temp)

        return answer


if __name__ == "__main__":
    heights = [2, 1, 5, 6, 2, 3, 1]

    lr = LargestRectangle()

    print(lr.largestRectangleArea(heights))
