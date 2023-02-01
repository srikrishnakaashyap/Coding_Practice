import heapq


def intern(arr1, arr2, k):

    finished_tasks = set()

    heap = []

    for i, j in enumerate(arr1):
        if arr2[i] <= arr1[i]:
            heap.append((-j, i))

    remainingTasksToFinish = 0
    if len(heap) < k:
        remainingTasksToFinish = k - len(heap)

    heapq.heapify(heap)

    profit = 0
    while len(heap) > 0:
        elem = heapq.heappop(heap)
        profit += abs(elem[0])
        finished_tasks.add(elem[1])
        heapq.heapify(heap)

    heap = []

    tasksIntern2ShouldFinish = len(arr2) - k

    for i, j in enumerate(arr2):
        if i not in finished_tasks:
            heap.append((-j, i))

    while tasksIntern2ShouldFinish > 0:
        elem = heapq.heappop(heap)
        profit += abs(elem[0])
        finished_tasks.add(elem[1])
        heapq.heapify(heap)
        tasksIntern2ShouldFinish -= 1

    if remainingTasksToFinish > 0:
        for i, j in enumerate(arr1):
            if i not in finished_tasks:
                profit += j

    return profit


if __name__ == "__main__":
    arr1 = [5, 4, 3, 2, 1]
    arr2 = [1, 2, 3, 4, 5]
    k = 3

    print(intern(arr1, arr2, k))
