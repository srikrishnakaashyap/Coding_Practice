import math


def prefixSuffix(arr):
    n = len(arr)
    ans = math.inf

    prefix = [0 for i in range(len(arr))]
    suffix = [0 for i in range(len(arr))]

    prefix[0] = arr[0]
    for i in range(1, n):
        prefix[i] = prefix[i - 1] + arr[i]

    suffix[n - 1] = arr[n - 1]

    for i in range(n - 2, -1, -1):
        suffix[i] = suffix[i + 1] + arr[i]

    index = -1
    # print(prefix)
    # print(suffix)
    for i in range(n - 1):
        x = prefix[i] // (i + 1)
        y = suffix[i + 1] // ((n - i) - 1)

        # print(i, x, y)

        if abs(x - y) < ans:
            index = i + 1
            ans = abs(x - y)

    return index


print(prefixSuffix([1, 1, 1, 1, 1]))
print(prefixSuffix([1, 3, 2, 4, 5]))
