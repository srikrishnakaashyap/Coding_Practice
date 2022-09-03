from collections import deque


class AvoidFloods:
    def avoidFlood(self, rains):

        n = len(rains)

        hs = set()

        zeroDeque = deque()
        rainArray = [0 for i in range(max(rains) + 1)]

        answer = [-1 for i in range(n)]

        for i, j in enumerate(rains):

            if j == 0:
                zeroDeque.append(i)

            if j != 0:
                if rainArray[j] == 1:

                    if not zeroDeque:
                        return []

                    index = zeroDeque.popleft()
                    if index > rainArray[j]:

                        answer[index] = j
                else:
                    rainArray[j] = i

        while zeroDeque:
            index = zeroDeque.popleft()
            answer[index] = 1
        return answer


if __name__ == "__main__":
    af = AvoidFloods()

    rains = [1, 2, 0, 0, 2, 1]

    print(af.avoidFlood(rains))
