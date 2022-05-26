class MatrixMedian:

    def numberLessN(self, arr, n):

        low = 0
        high = len(arr) - 1

        while(low <= high):
            mid = (low + high) // 2
            if arr[mid] <= n:
                low = mid + 1
            else:
                high = mid - 1

        return low

    def matrixMedian(self, matrix):
        low = 1
        high = 10**5

        total = len(matrix) * len(matrix[0])

        # print(total)
        while low <= high:
            mid = (low + high) // 2

            # print(low, mid, high)
            nless = 0
            for i in matrix:
                nless += self.numberLessN(i, mid)

            if nless <= (total / 2):
                low = mid + 1
            else:
                high = mid - 1

        print(low, mid, high)
        return low


if __name__ == "__main__":
    mm = MatrixMedian()

    matrix = [[1, 2, 6, 6, 10],
              [2, 4, 4, 5, 7],
              [2, 5, 5, 6, 6]]

    m2 = [[2, 6, 8], [1, 4, 7], [6, 8, 9]]

    # print(mm.numberLessN(matrix[0], 1))
    print(mm.matrixMedian(matrix))
