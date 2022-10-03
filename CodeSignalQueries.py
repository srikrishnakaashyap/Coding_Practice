from collections import defaultdict


class CodeSignalQueries:
    def processQueries(self, queries, diff):

        answer = []

        hm = defaultdict(int)

        numberOfPairs = 0

        for query in queries:

            number = int(query[1:])
            if query[0] == "+":
                hm[number] += 1
                minusCount = max(0, hm[number - diff])
                numberOfPairs += minusCount
                plusCount = max(0, hm[number + diff])
                numberOfPairs += plusCount

            if query[0] == "-":
                hm[number] -= 1
                minusCount = max(0, hm[number - diff])
                plusCount = max(0, hm[number + diff])
                numberOfPairs -= minusCount
                numberOfPairs -= plusCount

            answer.append(numberOfPairs)

        return answer


if __name__ == "__main__":

    queries = ["+2", "+2", "+4", "+3", "-2"]

    diff = 1

    cq = CodeSignalQueries()

    print(cq.processQueries(queries, diff))
