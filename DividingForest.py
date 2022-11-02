class DividingForest:
    def dividingForest(self, grid, number):
        def f(grid, row, col, map, number):

            if number == 0:

                for i in range(row, len(grid) - 1):
                    for j in range(col, len(grid[0]) - 1):
                        if grid[i][j] == 2:
                            return 1
                return 0

        hm = {}

        for i in range(len(grid)):
            for j in range(len(grid[0])):

                if grid[i][j] == 2:
                    if i in hm:
                        hm[i].add(j)
                    else:
                        hm[i] = set()
                        hm[i].add(j)

        answer = f(grid, 0, 0, hm, number - 1)

        return answer % ((10**9) + 7)


if __name__ == "__main__":

    df = DividingForest()

    grid = [[1, 2, 3], [2, 1, 2], [3, 1, 1]]
    number = 3

    print(df.dividingForest(grid, number))
