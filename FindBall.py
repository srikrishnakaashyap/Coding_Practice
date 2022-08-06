class FindBall:

    def findBall(self, grid):
        m = len(grid)
        n = len(grid[0])
        answer = [-1 for i in range(n)]
        for i in range(n):
            row = 0
            col = i
            while(0 <= row < m and 0 <= col < n):

                if grid[row][col] == 1 and col + 1 < n and grid[row][col+1] == 1:
                    row += 1
                    col += 1
                elif grid[row][col] == -1 and col - 1 >= 0 and grid[row][col-1] == -1:
                    row += 1
                    col -= 1
                else:
                    break
            if row == m:
                answer[i] = col

        return answer


if __name__ == "__main__":

    fb = FindBall()

    grid = [[1, 1, 1, -1, -1], [1, 1, 1, -1, -1],
            [-1, -1, -1, 1, 1], [1, 1, 1, 1, -1], [-1, -1, -1, -1, -1]]

    print(fb.findBall(grid))
