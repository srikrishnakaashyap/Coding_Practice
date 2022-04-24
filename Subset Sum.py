class SubsetSum:

    def subsetSum(self, arr):
        answer = []

        n = len(arr)

        def f(index, sum):
            if index >= n:
                answer.append(sum)
                return

            f(index + 1, sum + arr[index])
            f(index + 1, sum)

        f(0, 0)

        return sorted(answer)


if __name__ == "__main__":
    arr = [5, 2, 1]

    ss = SubsetSum()

    print(ss.subsetSum(arr))
