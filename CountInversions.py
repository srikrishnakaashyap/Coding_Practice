import sys


def merge(arr, left, mid, right):

    temp = [0 for i in range(len(arr))]

    i = left
    j = mid
    ctr = left
    inversions = 0

    while(i < mid and j <= right):

        if arr[i] <= arr[j]:
            temp[ctr] = arr[i]
            i += 1
        else:
            temp[ctr] = arr[j]
            inversions += (mid - i)
            j += 1
        ctr += 1

    while i < mid:
        temp[ctr] = arr[i]
        i += 1
        ctr += 1

    while j <= right:
        temp[ctr] = arr[j]
        j += 1
        ctr += 1

    for i in range(left, right + 1):
        arr[i] = temp[i]

    return inversions


def mergeSort(arr, left, right):
    inversions = 0
    if left < right:
        mid = (left + right) // 2
        inversions += mergeSort(arr, left, mid)
        inversions += mergeSort(arr, mid + 1, right)
        inversions += merge(arr, left, mid + 1, right)

    return inversions


def getInversions(arr, n):
    inversion = mergeSort(arr, 0, n - 1)
    # print(inversion)
    return inversion


# Taking inpit using fast I/O.
def takeInput():
    n = int(input())
    arr = list(map(int, sys.stdin.readline().strip().split(" ")))
    return arr, n


# Main.
arr, n = takeInput()
print(getInversions(arr, n))
