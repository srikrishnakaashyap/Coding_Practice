import json


def BE2ndDiagonal(strArr):

    matrix = []
    for row in strArr:
        elem = json.loads(row)
        matrix.append(elem)

    N, M = len(matrix), len(matrix[0])

    result, intermediate = [], []

    for d in range(N + M - 1):

        intermediate.clear()

        r, c = 0 if d < M else d - M + 1, d if d < M else M - 1

        while r < N and c > -1:
            intermediate.append(matrix[r][c])
            r += 1
            c -= 1
        if d % 2 == 0:
            result.extend(intermediate[::-1])
        else:
            result.extend(intermediate)

    # 1, 2, 3, 4
    answer = ""
    for i, elem in enumerate(result):

        answer += "{}".format(elem)
        if i != len(result) - 1:
            answer += ", "
    return answer.strip()


if __name__ == "__main__":

    strArr = ["[1, 2, 3, 4, 5]", "[6, 7, 8, 9, 10]", "[11, 12, 13, 14 ,15]"]

    print(BE2ndDiagonal(strArr))
