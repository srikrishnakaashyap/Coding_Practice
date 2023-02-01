def Rotate(arr, d, n):
    p = 1
    while p <= d:
        last = arr[0]
        for i in range(n - 1):
            arr[i] = arr[i + 1]
        arr[n - 1] = last
        p = p + 1


def ArrayRotation(arr):

    if len(arr) <= 1:
        return arr
    if arr[0] == 0:
        return arr

    Rotate(arr, arr[0], len(arr))

    answer = ""
    for elem in arr:
        answer += str(elem)
    return answer


if __name__ == "__main__":
    arr = [4, 3, 4, 3, 1, 2]
    print(ArrayRotation(arr))
