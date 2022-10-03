from collections import defaultdict


def isRowSame(matrix, rowNo):

    elem = matrix[rowNo][0]

    for row in matrix[rowNo]:
        if row != elem:
            return False, -1

    return True, elem


def isColSame(matrix, colNo):
    elem = matrix[0][colNo]

    for i in range(len(matrix[0])):
        if matrix[i][colNo] != elem:
            return False, -1

    return True, elem


def isRowNearlySame(matrix, rowNo):

    hm = defaultdict(int)
    for row in matrix[rowNo]:
        hm[row] += 1

    # print(hm)

    if len(hm) == 2 and 1 in list(hm.values()):

        keys = list(hm.keys())

        # print(keys)

        key_1 = keys[0]
        key_2 = keys[1]

        if hm[key_1] == len(matrix) - 1:
            return True, key_1, matrix[rowNo].index(key_2)
        elif hm[key_2] == len(matrix) - 1:
            return True, key_2, matrix[rowNo].index(key_1)

    return False, -1, -1


def isColNearlySame(matrix, colNo):

    hm = defaultdict(int)

    for i in range(len(matrix[0])):
        hm[matrix[i][colNo]] += 1

    if len(hm) == 2 and 1 in hm.values():
        keys = list(hm.keys())

        key_1 = keys[0]
        key_2 = keys[1]

        if hm[key_1] == len(matrix) - 1:

            diff_index = -1

            for i in range(len(matrix[0])):
                if matrix[i][colNo] != key_1:
                    diff_index = i
                    break

            return True, key_1, diff_index
        elif hm[key_2] == len(matrix) - 1:
            for i in range(len(matrix[0])):
                if matrix[i][colNo] != key_2:
                    diff_index = i
                    break

            return True, key_2, diff_index

    return False, -1, -1


def rectangleCross(matrix):

    sameRows = defaultdict(list)

    sameCols = defaultdict(list)

    if len(matrix) == 0:
        return 0

    m = len(matrix)
    n = len(matrix[0])

    for i in range(m):

        same, element = isRowSame(matrix, i)
        # print(same, element, i)

        if same:
            # sameRows.append((i, element))
            sameRows[element].append(i)

    for i in range(n):

        same, element = isColSame(matrix, i)

        if same:
            sameCols[element].append(i)

    perfectNumbers = 0

    for key, value in sameRows.items():
        if key in sameCols:

            perfectNumber = len(value) * len(sameCols[key])

    nearly_row = {}

    nearly_col = {}

    for i in range(m):

        same, element, index = isRowNearlySame(matrix, i)
        if same:
            # sameRows.append((i, element))

            if element in nearly_row:
                nearly_row[element].append((i, index))
            else:
                nearly_row[element] = [(i, index)]

    for i in range(n):
        same, element, index = isColNearlySame(matrix, i)
        if same:
            # sameRows.append((i, element))

            if element in nearly_col:
                nearly_col[element].append((i, index))
            else:
                nearly_col[element] = [(i, index)]

    print(nearly_row)

    print(nearly_col)

    # print(perfectNumber)


if __name__ == "__main__":

    matrix = [[1, 1, 1, 1], [2, 3, 1, 1], [1, 1, 1, 0], [1, 4, 1, 1]]

    print(rectangleCross(matrix))
