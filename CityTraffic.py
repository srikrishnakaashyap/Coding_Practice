import json
import math


def CityTraffic(strArray):
    def dfs(currKey, adjMap, visited, currValue, maximumValue):

        val = 0

        for adj in adjMap[currKey]:
            if adj not in visited:
                visited.add(adj)
                currValue = currValue + adj
                val += adj + dfs(adj, adjMap, visited, currValue, maximumValue)
                visited.remove(adj)
                currValue -= adj
        return val

    adjMap = {}

    for elem in strArray:
        dct = elem.split(":")
        key = int(dct[0])
        adjMap[key] = set(json.loads(dct[1]))

    answer = []
    for key, value in adjMap.items():
        visited = {key}
        val = 0
        for neighbours in adjMap[key]:
            visited.add(neighbours)
            tv = dfs(neighbours, adjMap, visited, 0, -math.inf)
            visited.remove(neighbours)
            val = max(val, tv + neighbours)

        answer.append(
            "{}:{}".format(
                key,
                val,
            )
        )

    answer = sorted(answer, key=lambda x: int(x.split(":")[0]))

    return ",".join(answer)


if __name__ == "__main__":
    strArr = [
        "1:[5]",
        "2:[5,18]",
        "3:[5,12]",
        "4:[5]",
        "5:[1,2,3,4]",
        "18:[2]",
        "12:[3]",
    ]

    print(CityTraffic(strArr))
