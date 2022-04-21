class MergeIntervals:

    def mergeIntervals(self, arr):
        arr = sorted(arr, key=lambda x: x[0])

        toret = []
        answer = 0
        ctr = 1
        n = len(arr)
        while(ctr < n):
            if arr[ctr][0] <= arr[ctr - 1][1]:
                arr[ctr][0] = min(arr[ctr-1][0], arr[ctr][0])
                arr[ctr][1] = max(arr[ctr-1][1], arr[ctr][1])
                arr[ctr-1][0] = min(arr[ctr-1][0], arr[ctr][0])
                arr[ctr-1][1] = max(arr[ctr-1][1], arr[ctr][1])
                # answer = ctr
            else:
                ctr += 1

        print(arr)
        for lst in arr:
            if lst not in toret:
                toret.append(lst)
        return toret


if __name__ == "__main__":

    mi = MergeIntervals()

    arr = [[1, 4], [0, 2], [3, 5]]

    print(mi.mergeIntervals(arr))
