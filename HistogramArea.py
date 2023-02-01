def HistogramArea(arr):
    n = len(arr)

    left = [0 for i in range(len(arr))]
    right = [0 for i in range(len(arr))]

    stack = []

    for i in range(n):
        while len(stack) > 0 and arr[stack[-1]] >= arr[i]:
            stack.pop(-1)

        left[i] = stack[-1] + 1 if len(stack) > 0 else 0

        stack.append(i)

    stack = []

    for i in range(n - 1, -1, -1):
        while len(stack) > 0 and arr[stack[-1]] >= arr[i]:
            stack.pop(-1)

        right[i] = stack[-1] - 1 if len(stack) > 0 else n - 1

        stack.append(i)

    answer = 0

    for i in range(n):
        temp = (right[i] - left[i] + 1) * arr[i]
        answer = max(answer, temp)

    return answer
