from re import L


class AllPaths:

    def allPaths(self, grid):

        answer = []

        def f(index, g):
            if index == len(grid) - 1:
                answer.append(g[:])
                return
            for i in grid[index]:
                g.append(i)
                f(i, g)
                g.pop()

        f(0, [0])
        return answer


if __name__ == "__main__":
    ap = AllPaths()
    grid = [[4, 3, 1], [3, 2, 4], [], [4], []]
    print(ap.allPaths(grid))
