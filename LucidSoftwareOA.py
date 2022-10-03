def bs(groups, index):
    lo = 0
    hi = index - 1

    while lo <= hi:
        mid = (lo + hi) // 2
        if groups[mid][1] < groups[index][0]:
            if groups[mid + 1][1] < groups[index][0]:
                lo = mid + 1
            else:
                return mid
        else:
            hi = mid - 1
    return -1


def phoneCalls(start, duration, volume):
    n = len(start)
    groups = []

    for i in range(n):
        groups.append(
            (start[i], start[i] + duration[i], volume[i], volume[i] / duration[i])
        )

    groups = sorted(groups, key=lambda x: x[1])

    dp = [0 for i in range(n)]
    dp[0] = groups[0][2]

    for i in range(1, n):
        inc = groups[i][2]

        l = bs(groups, i)

        if l != -1:
            inc += dp[l]

        dp[i] = max(dp[i - 1], inc)

    return dp[-1]
