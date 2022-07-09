class DominatingXor:

    def dominatingXor(self, arr, n):

        cnt = 0
        for i in range(n):
            for j in range(i, n):

                if arr[i] ^ arr[j] > arr[i] and arr[j]:
                    cnt += 1

        return cnt


if __name__ == "__main__":

    dx = DominatingXor()

    arr = [1, 2, 4, 8, 16, 32]
    n = len(arr)

    print(dx.dominatingXor(arr, n))
