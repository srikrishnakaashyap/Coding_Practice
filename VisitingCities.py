import heapq


class VisitingCities:

    def visitingCities(self, red, blue, blueCost):
        n = len(red)
        answer = [0 for i in range(n+1)]

        pq = []

        pq.append((red[0], 1, 'R'))
        pq.append((blue[0] + blueCost, 1, 'B'))

        heapq.heapify(pq)

        while(len(pq) > 0):

            elem = pq.pop(0)

            if elem[1] < n:

                if answer[elem[1]] != 0:
                    answer[elem[1]] = min(answer[elem[1]], elem[0])
                else:
                    answer[elem[1]] = elem[0]

                if elem[2] == 'R':
                    pq.append((elem[0] + red[elem[1]], elem[1] + 1, 'R'))
                    pq.append((elem[0] + blue[elem[1]] +
                               blueCost, elem[1] + 1, 'B'))
                else:
                    pq.append((elem[0] + red[elem[1]], elem[1] + 1, 'R'))
                    pq.append((elem[0] + blue[elem[1]], elem[1] + 1, 'B'))

                heapq.heapify(pq)

            elif elem[1] == n:
                if answer[elem[1]] != 0:
                    answer[elem[1]] = min(answer[elem[1]], elem[0])
                else:
                    answer[elem[1]] = elem[0]

        return answer

    def visitingCities2(self, red, blue, blueCost):

        n = len(red)
        redArray = [0 for i in range(n+1)]
        blueArray = [0 for i in range(n+1)]
        answer = [0 for i in range(n+1)]
        i = 1

        fromBlue = False

        while(i <= n):

            redArray[i] = answer[i-1] + red[i-1]
            blueArray[i] = blueArray[i-1] + blue[i-1]

            if not fromBlue:
                fromBlue = True
                blueArray[i] += blueCost

            if redArray[i] - blueArray[i] > blueCost:
                redArray[i] = blueArray[i]

                fromBlue = True
            elif blueArray[i] - redArray[i] > blueCost:
                blueArray[i] = redArray[i]
                fromBlue = False
            answer[i] = min(redArray[i], blueArray[i])

            i += 1

        return answer


if __name__ == "__main__":

    vc = VisitingCities()

    red = [40, 20]
    blue = [30, 25]

    True
    redArray = [0, 2, 5, 6, 7]
    blueArray = [0, 2, 5, 6, 8]
    answer = [0, 2, 5, 6, 7]

    blueCost = 5

    print(vc.visitingCities2(red, blue, blueCost))
