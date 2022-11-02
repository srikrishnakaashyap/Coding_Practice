def rectangle(queries):

    ret = []
    zero = []
    one = []
    for i in range(len(queries)):
        if queries[i][0] == 0:
            zero.append(queries[i])
        else:
            one = queries[i]

            temp = False
            for i in range(len(one)):
                if len(zero) == 0:
                    temp = True
                    break

                for j in range(len(zero)):
                    if (zero[j][1] >= one[1] and zero[j][2] >= one[2]) or (
                        zero[j][1] >= one[2] and zero[j][2] >= one[1]
                    ):
                        temp = True
                    else:
                        temp = False
                        break
            ret.append(temp)

    return ret


def rectangleOptimized(operations):

    ret = []

    rows = []

    cols = []

    n = len(operations)

    for i, j in enumerate(operations):

        if j[0] == 0:
            rows.append(j[1])
            cols.append(j[2])

            rows = sorted(rows)
            cols = sorted(cols)

        else:
            if len(rows) == 0:
                ret.append(True)
                break

            localAns = True
            for k in range(len(rows)):
                if (j[1] <= rows[k] and j[2] <= cols[k]) or (
                    j[1] <= cols[k] and j[2] <= rows[k]
                ):
                    continue
                else:
                    localAns = False

            ret.append(localAns)

    return ret


if __name__ == "__main__":

    queries = [[0, 3, 3], [0, 5, 2], [1, 3, 2], [1, 2, 4]]

    queries = [[1, 1, 1]]

    print(rectangleOptimized(queries))
