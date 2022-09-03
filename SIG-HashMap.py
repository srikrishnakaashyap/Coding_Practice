from collections import defaultdict

def Solution(queryType, query):

    hm = defaultdict()

    addToKey = 0
    addToValue = 0

    answer = 0

    n = len(query)

    for i in range(n):
        if queryType[i] == "insert":
            hm[query[i][0] - addToKey] = query[i][1] - addToValue
        elif queryType[i] == "get":
            answer += hm[query[i][0] - addToKey] + addToValue
        elif queryType[i] == "addToKey":
            addToKey += query[i][0]
        elif queryType[i] == "addToValue":
            addToValue += query[i][0]

    return answer

if __name__ == "__main__":
