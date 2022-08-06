class MaximalRectangle:

    def maximalRectangle(self, matrix):

        m = len(matrix)
        n = len(matrix[0])

        rowColMatrix = [[(0, 0) for i in range(n)]for j in range(m)]

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == "1":
                    if i == 0:
                        rowColMatrix[i][j] = 1
                    else:
                        rowColMatrix[i][j] = 1 + rowColMatrix[i-1][j]

        print(rowColMatrix)
        answer = 0

        for i in range(m):
            for j in range(n):

                if rowColMatrix[i][j] != 0:
                    answer = max(answer, rowColMatrix[i][j])

                length = rowColMatrix[i][j]
                width = 1
                ctr = j - 1
                while(ctr >= 0 and rowColMatrix[i][ctr] != 0):
                    width += 1

                    length = min(length, rowColMatrix[i][ctr])
                    answer = max(answer, width * length)
                    ctr -= 1

        return answer


if __name__ == "__main__":

    mr = MaximalRectangle()

    matrix = [["1", "1"]]

    print(mr.maximalRectangle(matrix))
