import math


def largest_row_smallest_col(matrix):

    rows = len(matrix)

    cols = len(matrix[0])

    if rows == 1 and cols == 1:
        return matrix[0][0]

    maxInRows = set()

    for i in range(rows):

        maxi = -math.inf

        col = -1

        for j in range(cols):
            if matrix[i][j] > maxi:
                maxi = matrix[i][j]
                col = j

        maxInRows.add((i, col))

    for j in range(cols):

        mini = math.inf
        row = -1

        for i in range(rows):
            if matrix[i][j] < mini:
                mini = matrix[i][j]
                row = i

        if (row, j) in maxInRows:
            return matrix[row][j]

    return -1


if __name__ == "__main__":
    matrix = [[1, 2], [3, 4]]

    print(largest_row_smallest_col(matrix))
