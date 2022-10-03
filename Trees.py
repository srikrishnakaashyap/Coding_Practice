class Node:
    def __init__(self, val):
        self.val = val
        self.left = self.right = None


class BinaryTree:

    root = None

    def __init__(self, val=None):
        if val is not None:
            self.root = Node(val)

    def printInorderRecursively(self, root):
        if root is None:
            return

        self.printInorderRecursively(root.left)
        print(root.val, end=" ")
        self.printInorderRecursively(root.right)

    def printInorder(self):

        self.printInorderRecursively(self.root)
        print()


class BinaryTreeOperations:
    def operations(self):

        tree = BinaryTree()

        tree.root = Node(5)

        tree.root.left = Node(4)
        tree.root.right = Node(7)
        tree.root.left.left = Node(2)
        tree.root.left.right = Node(3)
        tree.root.left.left.left = Node(1)
        tree.root.right.left = Node(6)
        tree.root.right.right = Node(8)

        tree.printInorder()


if __name__ == "__main__":

    bo = BinaryTreeOperations()

    bo.operations()
