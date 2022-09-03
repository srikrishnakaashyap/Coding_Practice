class CodeSignalNumberOfChanges:
    def numberOfChanges(self, arr):

        n = len(arr)

        answer = 0
        i = 0
        while i < n:
            j = i + 1
            while j < n and arr[j].lower() == arr[i].lower():
                j += 1
            i = j
            answer += 1

        return answer - 1


if __name__ == "__main__":

    cs = CodeSignalNumberOfChanges()

    arr = ["w", "w", "a", "w", "a"]

    print(cs.numberOfChanges(arr))
