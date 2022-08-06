class SegmentTree:

    def build(self, index, low, high, arr):
        if low == high:

            self.segment_tree[index] = arr[low]
            return

        mid = (low + high) // 2
        self.build((index * 2) + 1, low, mid, arr)
        self.build((index * 2) + 2, mid + 1, high, arr)

        self.segment_tree[index] = min(
            self.segment_tree[(index * 2) + 1], self.segment_tree[(index * 2) + 2])

    def segmentTree(self, arr):

        n = len(arr)

        self.segment_tree = [0 for i in range(4 * n)]

        self.build(0, 0, n-1, arr)

        print(self.segment_tree)

    def __init__(self) -> None:
        self.segment_tree = []


if __name__ == "__main__":

    st = SegmentTree()

    arr = [1, 3, 2, 0, 4, 5]

    st.segmentTree(arr)
