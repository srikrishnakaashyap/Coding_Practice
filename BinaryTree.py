class Node:

    def __init__(self, value=0, left=None, right=None):
        self.left = left
        self.right = right
        self.val = value


class BinaryTree:

    def __init__(self, value):
        self.root = Node(value)

    def inorderTraversal(self, root):

        answer = []

        curr = root

        while(curr != None):
            if curr.left == None:
                answer.append(curr.val)
                curr = curr.right
            else:
                prev = curr.left

                while prev.right != None and prev.right != curr:
                    prev = prev.right

                if prev.right == None:
                    prev.right = curr
                    answer.append(curr.val)
                    curr = curr.left

                else:
                    prev.right = None

                    curr = curr.right

        return answer

    def right_view(self, root):

        answer = []

        def f(root, level=0):
            if root is None:
                return

            if len(answer) == level:
                answer.append(root.val)

            f(root.right, level+1)
            f(root.left, level + 1)

        f(root)
        return answer

    def bottom_view(self, root):

        dic = {}
        queue = []

        queue.append((root, 0, 0))

        while(len(queue) > 0):
            element = queue.pop(0)

            if element[0] and element[0].left is not None:
                queue.append((element[0].left, element[1] + 1, element[2] + 1))

            if element[0] and element[0].right is not None:
                queue.append(
                    (element[0].right, element[1] - 1, element[2] + 1))

            if element[0]:
                if element[1] in dic:
                    temp = dic[element[1]]
                    if element[2] in temp:
                        temp2 = temp[element[2]]
                        temp2.append(element[0].val)
                        temp[element[2]] = sorted(temp2)
                    else:
                        temp[element[2]] = [element[0].val]
                    dic[element[1]] = temp
                else:
                    dic[element[1]] = {element[2]: [element[0].val]}

        dic = sorted(dic.items(), key=lambda x: (x[0], x[1]))

        answer = []

        for element in dic:
            elements = sorted(element[1].items(), key=lambda x: (x[0], x[1]))

            temp2 = []
            for x in elements:
                for y in x[1]:
                    temp2.append(y)

            if temp2:
                answer.append(temp2)
        return answer

    def maximum_width(self, root):

        if root is None:
            return 0

        queue = []
        queue.append((root, 0))
        first, last = 0, 0
        answer = 0

        while(len(queue) > 0):
            size = len(queue)
            minn = queue[0][1]

            for i in range(size):

                curr = queue[0][1] - minn
                node = queue[0][0]
                queue.pop(0)

                if node.left:
                    queue.append((node.left, (curr * 2) + 1))

                if node.right:
                    queue.append((node.right, (curr * 2) + 2))

                if i == 0:
                    first = curr

                if i == size - 1:
                    last = curr

            answer = max(answer, last - first + 1)
        return answer

    def zigZagLevelOrderTraversal(self, root):

        if root is None:
            return []

        queue = []
        queue.append(root)
        answer = []

        order = 0
        while(len(queue) > 0):

            size = len(queue)
            temp = []
            for i in range(size):
                node = queue.pop(0)

                temp.append(node.val)

                if order == 1:
                    order = 0

                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
                else:
                    order = 1
                    if node.right:
                        queue.append(node.right)
                    if node.left:
                        queue.append(node.left)

            answer.append(temp)

        return answer


if __name__ == "__main__":

    tree = BinaryTree(20)
    tree.root.left = Node(8)
    tree.root.right = Node(22)
    tree.root.left.left = Node(5)
    tree.root.left.right = Node(3)
    tree.root.right.right = Node(25)
    tree.root.left.right.left = Node(10)
    tree.root.left.right.right = Node(14)

    tree = BinaryTree(3)
    tree.root.left = Node(9)
    tree.root.right = Node(20)
    tree.root.right.left = Node(15)
    tree.root.right.right = Node(7)

    # tree.inorder(tree.root)

    print(tree.zigZagLevelOrderTraversal(tree.root))
