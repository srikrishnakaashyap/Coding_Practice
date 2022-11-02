class DisjointSet:
    def __init__(self, n=0):
        self.rank = [0 for i in range(n + 1)]
        self.parent = [i for i in range(n + 1)]

    def findParent(self, u):
        if u == self.parent[u]:
            return u
        parent = self.findParent(self.parent[u])
        self.parent[u] = parent
        return parent

    def union(self, a, b):

        aPar = self.findParent(a)
        bPar = self.findParent(b)
        if aPar == bPar:
            return

        if self.rank[aPar] == self.rank[bPar]:

            self.parent[bPar] = aPar
            self.rank[bPar] += 1
            return

        if self.rank[aPar] < self.rank[bPar]:
            aPar, bPar = bPar, aPar

        self.parent[bPar] = aPar


if __name__ == "__main__":

    ds = DisjointSet(7)

    ds.union(1, 2)
    ds.union(2, 3)
    ds.union(4, 5)
    ds.union(6, 7)
    ds.union(5, 6)

    print(ds.findParent(3) == ds.findParent(7))

    ds.union(3, 7)

    print(ds.findParent(3) == ds.findParent(7))
