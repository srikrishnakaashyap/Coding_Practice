class KthSmallestMatrix:

    def lower_bound(self, row, element):
        low = 0
        high = len(row)

        while low < high:
            mid = (low + high) // 2

            if row[mid] <= element:
                low = mid + 1
            else:
                high = mid

        return high

    def kthSmallest(self, matrix, k):

        low = matrix[0][0]
        high = matrix[len(matrix) - 1][len(matrix) - 1]

        while(low < high):

            mid = (low + high) // 2

            nsmaller = 0
            for row in matrix:
                nsmaller += self.lower_bound(row, mid)

            if nsmaller < k - 1:
                low = mid + 1
            else:
                high = mid

        return int(low)


if __name__ == "__main__":

    ksm = KthSmallestMatrix()

    matrix = [[-5]]
    k = 1

    print(ksm.kthSmallest(matrix, k))

    # print(ksm.lower_bound(matrix[1], 12))
