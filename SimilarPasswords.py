import math
import heapq


def similarPasswords(string):

    n = len(string)

    k = n // 2

    vowels = [ord("a"), ord("e"), ord("i"), ord("o"), ord("u")]

    distance = [0 for i in range(n)]

    numberOfVowels = 0
    for i, j in enumerate(string):
        if ord(i) in vowels:
            numberOfVowels += 1
        else:
            leftDistance = math.inf
            rightDistance = math.inf

            asc = ord(i)

            if asc > vowels[-1]:
                leftDistance = vowels[-1]
            else:
                for v, index in enumerate(vowels):
                    if v > asc:
                        break

                leftDistance = vowels[index] - 1 if index > 0 else math.inf
                rightDistance = vowels[index]
            distance[j] = min(leftDistance, rightDistance)

    if numberOfVowels == k:
        return 0

    if numberOfVowels > k:
        return numberOfVowels - k

    if numberOfVowels < k:
        answer = 0

        toFind = k - numberOfVowels

        while toFind:
            heapq.heapify(distance)
            answer += heapq.heappop(distance)

        return answer
