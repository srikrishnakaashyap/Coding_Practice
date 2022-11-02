def pascal(arr):
    n = len(arr)
    if n < 3:
        return "".join(str(i) for i in arr)
    a2 = []
    while n != 2:
        for i in range(0, n - 1):
            d = arr[i] + arr[i + 1]
            d = d % 10
            a2.append(d)
        arr = a2
        n = len(arr)
        a2 = []
    return "".join(str(i) for i in arr)


print(pascal([4, 5, 6, 7]))
print(pascal([1, 2]))
