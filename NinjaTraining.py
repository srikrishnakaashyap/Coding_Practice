class NinjaTraining:

    def ninjaTraining(self, n, points):

        def f(index, previous):
            if index == 0:
                maxi = 0

                for i in range(0, 2):
                    if i != previous:
                        maxi = max(maxi, points[0][i])

                return maxi


if __name__ == "__main__":

    nt = NinjaTraining()
    points = [[1, 2, 5], [3, 1, 1], [3, 3, 3]]
    n = 3
    print(nt.ninjaTraining(n, points=points))
