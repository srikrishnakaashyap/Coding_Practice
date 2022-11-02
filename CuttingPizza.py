from typing import List


class CuttingPizza:
    def ways(self, pizza: List[str], k: int) -> int:

        pizzaMatrix = []
        for i in range(len(pizza)):
            row = []
            for j in range(len(pizza[i])):
                if pizza[i][j] == "A":
                    row.append(1)
                else:
                    row.append(0)
            pizzaMatrix.append(row)

        ways = []

        def f(row, col, cuts, prefixSum, dp, way=[]):
            if cuts == 0:
                nonlocal ways
                for i in range(row, len(pizzaMatrix)):
                    for j in range(col, len(pizzaMatrix[0])):
                        if prefixSum[row][col] > 0:
                            return 1
                return 0

            if (row, col, cuts) in dp:
                return dp[(row, col, cuts)]

            horizontal = 0
            vertical = 0
            for i in range(row + 1, len(pizzaMatrix)):
                if prefixSum[row][col] - prefixSum[i][col] != 0:
                    way.append("{} - H".format(i))
                    horizontal += f(i, col, cuts - 1, prefixSum, dp)
                    way.pop(-1)

            for i in range(col + 1, len(pizzaMatrix[0])):
                if prefixSum[row][col] - prefixSum[row][i] != 0:
                    way.append("{} - V".format(i))
                    vertical += f(row, i, cuts - 1, prefixSum, dp)
                    way.pop(-1)

            dp[(row, col, cuts)] = vertical + horizontal
            return vertical + horizontal

        prefixSum = [
            [0 for i in range(len(pizzaMatrix[0]))] for j in range(len(pizzaMatrix))
        ]

        prefixSum[-1][-1] = pizzaMatrix[-1][-1]

        for i in range(len(pizzaMatrix) - 2, -1, -1):
            prefixSum[i][-1] = pizzaMatrix[i][-1] + prefixSum[i + 1][-1]

        for i in range(len(pizzaMatrix[-1]) - 2, -1, -1):
            prefixSum[-1][i] = pizzaMatrix[-1][i] + prefixSum[-1][i + 1]

        for i in range(len(pizzaMatrix) - 2, -1, -1):
            for j in range(len(pizzaMatrix[i]) - 2, -1, -1):
                prefixSum[i][j] = (
                    pizzaMatrix[i][j]
                    - prefixSum[i + 1][j + 1]
                    + prefixSum[i + 1][j]
                    + prefixSum[i][j + 1]
                )

        # print(prefixSum)
        dp = {}
        answer = f(0, 0, k - 1, prefixSum, dp)

        print(ways)

        return answer % ((10**9) + 7)


if __name__ == "__main__":
    cp = CuttingPizza()

    pizza = ["A..", "AAA", "AAA"]
    k = 3

    print(cp.ways(pizza, k))
