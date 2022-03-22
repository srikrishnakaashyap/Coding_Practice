class SubSequence:

    def subsequence(self, arr, start, end):

        if len(arr) == 1:
            return arr[0]

        secPrev = arr[0]
        prev = max(arr[0], arr[1])

        for i in range(2, len(arr)):
            curr = max(prev, arr[i] + secPrev)

            secPrev = prev
            prev = curr

        return prev


if __name__ == "__main__":
    arr = [1, 1]

    s = SubSequence()

    print(s.subsequence(arr, 0, len(arr)))
