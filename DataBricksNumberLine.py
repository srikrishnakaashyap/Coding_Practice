class DataBricksNumberLine:
    def bs(self, low, high, arr, val):
        while low < high:
            mid = low + high // 2

            if arr[mid] == val:
                return mid

            if arr[mid] > val:
                high = mid - 1
            else:
                low = mid + 1

        return high

    def queries(self, queries):

        arr = []
        answer = ""

        for query in queries:
            if query[0] == 1:
                index = self.bs(0, len(arr) - 1, arr, query[1])

                arr.insert(index, query[1])
                answer += "0"
            elif query[0] == 2:
                lower = self.bs(0, arr - 1, arr, query[1] - query[2])
                upper = self.bs(0, arr - 1, arr, query[1] - 1)

                if lower == upper:
                    answer += "1"
                else:
                    answer += "0"

        return answer
