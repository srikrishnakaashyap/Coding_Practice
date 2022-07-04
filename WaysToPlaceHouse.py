class WaysToPlace:

    def countHousePlacements(self, n):

        def f(plotno, index, row, grid=[[]]):
            # print(grid)
            if index >= n or plotno >= n:
                print(grid)
                return 1

            pick = 0
            # print(index, grid)
            if (index > 0 and index < n and grid[index - 1][row] == 0) or (index == 0 and grid[index][row] == 0):

                grid[index][row] = plotno
                pick = f(plotno + 1, index+2, row, grid) + \
                    f(plotno, index, not(row), grid)
                grid[index][row] = 0

            nopick = f(plotno + 1, index + 1, row, grid)
            # f(plotno + 1, index, not(row), grid)

            return pick + nopick

        grid = [[0 for i in range(2)] for j in range(n)]
        answer = f(1, 0, False, grid)
        return answer


if __name__ == "__main__":

    wtp = WaysToPlace()
    n = 2
    print(wtp.countHousePlacements(n))
