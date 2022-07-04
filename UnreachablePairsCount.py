import datetime
from datetime import timedelta


class UnreachablePairsCount:

    def countPairs(self, n, edges):

        edgeMap = {}

        for edge in edges:
            if edge[0] in edgeMap:
                edgeMap[edge[0]].append(edge[1])
            else:
                edgeMap[edge[0]] = [edge[1]]

        print(edgeMap)

    def check_time(self, date1, date2):

        date1 = date1.split(":")
        date2 = date2.split(":")

        if date1[0] == "00":
            date1[0] = "24"

        # if date2[0] == "00":
        #     date2[0] = "24"

        time1 = timedelta(hours=int(date1[0]), minutes=int(
            date1[1]), seconds=int(date1[2]))
        time2 = timedelta(hours=int(date2[0]), minutes=int(
            date2[1]), seconds=int(date2[2]))

        print(time1.seconds, time2.seconds)

        if time1.seconds > time2.seconds and time1.seconds - time2.seconds <= 60:
            return True
        return False


if __name__ == "__main__":

    n = 7
    edges = [[0, 2], [0, 5], [2, 4], [1, 6], [5, 4]]

    upc = UnreachablePairsCount()

    # print(upc.countPairs(n, edges))

    print(upc.check_time('00:00:45', '00:00:30'))
