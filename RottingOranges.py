class RottingOranges:

    def rottingOranges(self, grid):

        queue = []

        m = len(grid)
        n = len(grid[0])
        visited = [[False for i in range(n)] for j in range(m)]

        def bfs(visited, queue, grid):

            answer = 0

            while(len(queue) > 0):

                n = len(queue)

                for i in range(n):

                    element = queue.pop(0)
                    row = [-1, 0, 0, 1]
                    column = [0, 1, -1, 0]

                    for j in range(4):
                        if 0 <= element[0] + row[j] < len(grid) and 0 <= element[1] + column[j] < len(grid[0]) and grid[element[0] + row[j]][element[1] + column[j]] == 1 and not visited[element[0] + row[j]][element[1] + column[j]]:

                            grid[element[0] + row[j]
                                 ][element[1] + column[j]] = 2
                            visited[element[0] + row[j]
                                    ][element[1] + column[j]] = True

                            queue.append(
                                (element[0] + row[j], element[1] + column[j]))
                answer += 1

            return answer

        m = len(grid)
        n = len(grid[0])

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    visited[i][j] = True
                    queue.append((i, j))

        answer = bfs(visited, queue, grid)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    return -1

        return answer - 1


if __name__ == "__main__":

    ro = RottingOranges()

    grid = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]

    print(ro.rottingOranges(grid))
