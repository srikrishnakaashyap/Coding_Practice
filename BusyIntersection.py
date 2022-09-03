from collections import deque

# Working Code
def getResult(arrival, street):
    present_second, prev_second_street, prev_second = 0, None, None
    main_street, first_street = deque(), deque()
    answer = [0] * len(arrival)

    for i in range(len(arrival)):
        if street[i] == 0:
            main_street.append((arrival[i], i))
        else:
            first_street.append((arrival[i], i))

    while main_street and first_street:

        if present_second < main_street[0][0] and present_second < first_street[0][0]:
            present_second = min(main_street[0][0], first_street[0][0])

        if (
            main_street[0][0] < first_street[0][0]
            and main_street[0][0] >= present_second
        ):
            present_second = main_street[0][0]
            temp = main_street.popleft()
            answer[temp[1]] = present_second
            prev_second = present_second
            prev_second_street = 0
            present_second += 1

        elif (
            main_street[0][0] > first_street[0][0]
            and first_street[0][0] >= present_second
        ):
            present_second = first_street[0][0]
            temp = first_street.popleft()
            answer[temp[1]] = present_second
            prev_second = present_second
            prev_second_street = 1
            present_second += 1
        else:
            if (
                present_second - 1 != prev_second
                and present_second >= first_street[0][0]
            ) or (
                present_second - 1 == prev_second
                and prev_second_street != 0
                and present_second >= first_street[0][0]
            ):
                while first_street and present_second >= first_street[0][0]:
                    top_element = first_street.popleft()
                    answer[top_element[1]] = present_second
                    prev_second = present_second
                    prev_second_street = 1
                    present_second += 1
            else:
                while main_street and present_second >= main_street[0][0]:
                    top_element = main_street.popleft()
                    answer[top_element[1]] = present_second
                    prev_second = present_second
                    prev_second_street = 1
                    present_second += 1

    while first_street:
        top_element = first_street.popleft()
        answer[top_element[1]] = max(present_second, top_element[0])
        present_second = max(present_second, top_element[0]) + 1

    while main_street:
        top_element = main_street.popleft()
        answer[top_element[1]] = max(present_second, top_element[0])
        present_second = max(present_second, top_element[0]) + 1
    return answer


class BusyIntersection:
    def busyIntersection(self, arrival, street):

        n = len(arrival)
        answer = [-1 for i in range(len(arrival))]
        pq_1 = []  # MainStreet
        pq_2 = []  # 1st Avenue

        for i in range(n):
            if street[i] == 0:
                pq_1.append((arrival[i], i))
            else:
                pq_2.append((arrival[i], i))

        heapq.heapify(pq_1)
        heapq.heapify(pq_2)

        prevStreet = -1
        prevSecond = -1
        curr = 0
        fromElse = False
        while pq_1 and pq_2:
            temp_1 = pq_1[0]
            temp_2 = pq_2[0]

            if fromElse:
                if prevStreet == 0:
                    if temp_1[0] > curr:
                        fromElse = False
                else:
                    if temp_2[0] > curr:
                        fromElse = False

            if temp_1[0] > curr and temp_2[0] > curr:
                curr = min(temp_1[0], temp_2[0])
                continue
            if temp_1[0] < temp_2[0] and not fromElse:
                answer[temp_1[1]] = curr
                heapq.heappop(pq_1)
                prevSecond = curr
                curr += 1
                prevStreet = 0
                # prev =
            elif temp_1[0] > temp_2[0] and not fromElse:
                answer[temp_2[1]] = curr
                heapq.heappop(pq_2)
                prevSecond = curr
                curr += 1
                prevStreet = 1
            else:
                fromElse = True
                if temp_1[0] == prevSecond + 1:

                    if prevStreet == 0:
                        answer[temp_1[1]] = curr
                        heapq.heappop(pq_1)
                        prevSecond = curr
                        curr += 1
                        prevStreet = 0
                    else:
                        answer[temp_2[1]] = curr
                        heapq.heappop(pq_2)
                        prevSecond = curr
                        curr += 1
                        prevStreet = 1
                else:
                    answer[temp_2[1]] = curr
                    heapq.heappop(pq_2)
                    prevSecond = curr
                    curr += 1
                    prevStreet = 1

        while pq_1:
            temp_1 = heapq.heappop(pq_1)
            answer[temp_1[1]] = max(curr, temp_1[0])
            curr = max(curr, temp_1[0]) + 1

        while pq_2:
            temp_2 = heapq.heappop(pq_2)
            answer[temp_2[1]] = max(curr, temp_2[0])
            curr = max(curr, temp_2[0]) + 1

        return answer


if __name__ == "__main__":

    bi = BusyIntersection()

    arrival = [3, 2, 2, 1]
    street = [0, 1, 0, 0]

    # 0, 2, 1, 4, 3

    print(bi.busyIntersection(arrival, street))
