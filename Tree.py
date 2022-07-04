from logging import root


class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


class Tree:

    root = None

    def __init__(self, root=None):
        root = Node(root)

    def insert(self, values):

        self._insert_helper(values, 0, len(values))

    def _insert_helper(self, values, i, n):
        if i < n:
            self.root = Node(values[i])

            self.root.left = self._insert_helper(values, 2 * i + 1, n)
            self.root.right = self._insert_helper(values, 2 * i + 2, n)


if __name__ == "__main__":

    tree = Tree()

    values = [1, 2, 3, 4, 5, 6, 7]

    tree.insert(values)

    print(tree.sumDepths())
