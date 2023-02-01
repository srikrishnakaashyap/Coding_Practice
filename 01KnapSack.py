class KnapSack:
    def sol(budget, adTypes):

        n = len(adTypes)
        K = [[0 for x in range(budget + 1)] for x in range(n + 1)]

        for i in range(n + 1):
            for w in range(budget + 1):
                if i == 0 or w == 0:
                    K[i][w] = 0
                elif adTypes[i - 1][0] <= w:
                    K[i][w] = max(
                        adTypes[i - 1][1] + K[i - 1][w - adTypes[i - 1][0]], K[i - 1][w]
                    )
                else:
                    K[i][w] = K[i - 1][w]
        return K[n][budget]


def rotateRight(n, r, k):
    b = bin(n)[2:]
    b.zfill("0", k)
    # r = r % k
    b1 = b[k - r :] + b[: k - r]

    return int(b1, 2)


if __name__ == "__main__":
    weights = [10, 20, 30]
    values = [60, 100, 120]
    w = 50

    n = 2**32 - 1
    print(rotateRight(n, 30, 31))
