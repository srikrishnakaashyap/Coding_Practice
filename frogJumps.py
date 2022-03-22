class FrogJumps:

    def frogJumps(self, n, heights, k):

        temp = [0 for i in range(n)]

        for i in range(1, n):

            ans = 10**9
            for j in range(i - 1, i - k - 1, -1):
                if j < 0:
                    break
                te = temp[j] + abs(heights[i] - heights[j])
                ans = min(ans, te)
            temp[i] = ans
            ans = 10**9
        return temp[n - 1]


if __name__ == "__main__":

    f = FrogJumps()
    # arr = 27 35 43 34 27 19 7 38 16 18 46 13 14 50 34 38 36 34 26 39 6 41 23 1 33 30 45 13 47 13 22 20 3 1 17 26 45 39 22 45 21 11 30 44 36 45 29 27 39 42 40 35 46 31 21 6 31 50 20 50 10 10 24 6 30 29 44 39 42 14 23 12 4 1 35 5 45 40 44 42 47 24 48 16 21 50 34 4 13 5 36 46 20 45 3 13, 7]
    k = int(input())
    arr = list(map(int, input().split()))
    n = len(arr)

    print(f.frogJumps(n, arr, k))
