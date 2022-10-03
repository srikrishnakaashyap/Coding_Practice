from collections import deque


class NumberOfIslands:
    def bfs(self, grid, visited, queue):

        row = [-1, -1, -1, 0, 0, 1, 1, 1]
        col = [0, -1, 1, -1, 1, 0, -1, 1]

        while queue:
            n = len(queue)

            for i in range(n):
                elem = queue.popleft()
                for j in range(8):

                    newRow = elem[0] + row[j]
                    newCol = elem[1] + col[j]
                    if (
                        0 <= newRow < len(grid)
                        and 0 <= newCol < len(grid[0])
                        and grid[newRow][newCol] == "1"
                        and not visited[newRow][newCol]
                    ):
                        visited[newRow][newCol] = True
                        queue.append((newRow, newCol))

        print(visited)

    def numIslands(self, grid):

        m = len(grid)
        n = len(grid[0])

        visited = [[False for i in range(n)] for j in range(m)]

        queue = deque()

        answer = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1" and not visited[i][j]:
                    visited[i][j] = True
                    print(visited)
                    queue.append((i, j))
                    self.bfs(grid, visited, queue)
                    answer += 1
        return answer


if __name__ == "__main__":

    ni = NumberOfIslands()

    grid = [[]]

    print(ni.numIslands(grid))
