class CyclicShift:
    def nextCycle(self, a):

        a = str(a)
        return int(a[-1] + a[:-1])

    def merge(self, l, m, r, arr):
        n1 = m - l + 1
        n2 = r - m

        # create temp arrays
        L = [0] * (n1)
        R = [0] * (n2)

        # Copy data to temp arrays L[] and R[]

        hm = {}
        for i in range(0, n1):
            elem = arr[l + i]
            if elem in hm:
                hm[elem] += 1
            else:
                hm[elem] = 1

        print(hm)

        for j in range(0, n2):
            r = arr[m + 1 + j]
            if r in hm:
                self.answer += hm[r]

            elem = self.nextCycle(r)
            if elem in hm:
                self.answer += hm[elem]
            print(elem)

            while elem != r:
                print(elem, r)
                self.answer += hm.get(elem, 0)
                elem = self.nextCycle(elem)

    def mergeSort(self, i, j, arr):

        if i < j:
            m = i + (j - i) // 2
            self.mergeSort(i, m, arr)
            self.mergeSort(m + 1, j, arr)
            self.merge(i, m, j, arr)

    def cyclicShift(self, arr):

        low = 0
        high = len(arr) - 1

        # self.hm = {}

        self.answer = 0

        self.mergeSort(low, high, arr)

        return self.answer


if __name__ == "__main__":

    cs = CyclicShift()

    arr = [13, 5604, 31, 2, 13, 4560, 546, 654, 456]

    print(cs.cyclicShift(arr))
