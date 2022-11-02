from collections import defaultdict


def solution(matrix):
    n = len(matrix)
    ycount = defaultdict(int)
    nonycount = defaultdict(int)
    for i in range(n):
        for j in range(n):
            if i < n // 2:
                if i == j or i + j == n - 1:
                    ycount[matrix[i][j]] += 1
                else:
                    nonycount[matrix[i][j]] += 1
            else:
                if j == n // 2:
                    ycount[matrix[i][j]] += 1
                else:
                    nonycount[matrix[i][j]] += 1
    su = sum(nonycount)
    changes = [
        ycount[1] + ycount[2] + nonycount[0],
        ycount[0] + ycount[2] + nonycount[1],
        ycount[0] + ycount[1] + nonycount[2],
    ]
    print(ycount)
    print(nonycount)
    print(changes)
    return min(changes)


matrix = [[1, 0, 2], [1, 2, 0], [0, 2, 0]]
print(solution(matrix))
