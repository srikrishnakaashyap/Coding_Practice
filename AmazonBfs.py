def bfs(visited, queue, grid):

    answer = 0

    while len(queue) > 0:

        n = len(queue)

        for i in range(n):

            element = queue.pop(0)
            row = [-1, 0, 0, 1]
            column = [0, 1, -1, 0]

            for j in range(4):

                if grid[element[0]][element[1]] == 9:
                    return answer
                if (
                    0 <= element[0] + row[j] < len(grid)
                    and 0 <= element[1] + column[j] < len(grid[0])
                    and grid[element[0] + row[j]][element[1] + column[j]] != 0
                    and not visited[element[0] + row[j]][element[1] + column[j]]
                ):

                    visited[element[0] + row[j]][element[1] + column[j]] = True

                    queue.append((element[0] + row[j], element[1] + column[j]))
        answer += 1

    return -1


def computeDistance(grid):

    queue = []

    queue.append((0, 0))

    visited = [[False for i in range(len(grid[0]))] for j in range(len(grid))]
    visited[0][0] = True

    return bfs(visited, queue, grid)


if __name__ == "__main__":

    grid = [[1, 0, 0], [1, 0, 0], [1, 9, 1]]

    print(computeDistance(grid))
