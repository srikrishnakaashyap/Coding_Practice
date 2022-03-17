class KSmallestElement:

    def partition(self, array, start, end, index):

        array[index], array[end] = array[end], array[index]
        left = start - 1
        pivot = array[end]

        for i in range(start, end):
            if array[i] <= pivot:
                left += 1
                array[left], array[i] = array[i], array[left]

        left += 1

        array[left], array[end] = array[end], array[left]
        return left

    def median(self, array):
        array = sorted(array)
        mid = len(array) // 2
        return array[mid]

    def computeMediansHelper(self, array):
        temp = []
        start = 0
        end = len(array)
        while(start < end):
            last = start + 5
            last = min(end, last)
            temp.append(self.median(array[start:last]))
            start = start + 5
        return temp

    def computeMedians(self, array):
        # print(array)
        if len(array) == 0:
            return
        if len(array) <= 2:
            return array[0]
        return self.computeMedians(self.computeMediansHelper(array[:]))

    def ksmallest(self, array, k):

        if len(array) <= 2:
            return array[k - 1]
        median = self.computeMedians(array)
        index = array.index(median)

        pivotIndex = self.partition(array, 0, len(array) - 1, index)

        if(pivotIndex + 1 == k):
            return array[pivotIndex]
        if(pivotIndex + 1 < k):
            # Move Right
            return self.ksmallest(array[pivotIndex: len(array)], k - pivotIndex)
        else:
            # Move Left
            return self.ksmallest(array[0: pivotIndex], k)


if __name__ == "__main__":

    array = [7, 10, 4, 3, 20, 15, 7]
    k = 7

    print(KSmallestElement().ksmallest(array, k))
