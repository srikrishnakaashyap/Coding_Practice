class CountPairs:

    def count(self, n, d, arr):
        dic = {}

        for i in range(n):

            if arr[i] in dic:
                dic[arr[i]].append(i + 1)
            else:
                dic[arr[i]] = [i + 1]

        count = 0
        for key, values in dic.items():
            # values = dic[key]
            # print(values)
            for i in range(len(values)):
                for j in range(i + 1, len(values)):
                    if values[i] * values[j] % d == 0:
                        count += 1
        return count


if __name__ == "__main__":

    cp = CountPairs()

    d = 6
    n = 5
    arr = [2, 2, 2, 2, 2]

    print(cp.count(n, d, arr))
