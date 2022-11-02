class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, data):
        self.head = Node(data)
        self.tail = self.head

    # h         t
    # 0 -> 1 -> 2 -> None
    # 0 -> 1 -> 2 -> 3 -> None
    def pushTail(self, data):
        node = Node(data)
        self.tail.next = node
        self.tail = node

    def pushHead(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node

    # 1 -> 2 -> None
    def printList(self):

        node = self.head
        while True:
            if node == None:
                break
            print(node.data, end=" ")
            node = node.next


class operations:
    def operations(self):

        linkedlist = LinkedList(2)

        linkedlist.pushHead(1)
        # linkedlist.printList()
        linkedlist.pushHead(0)

        linkedlist.pushTail(3)

        # print(linkedlist.tail.data)

        linkedlist.printList()


if __name__ == "__main__":

    op = operations()

    op.operations()
