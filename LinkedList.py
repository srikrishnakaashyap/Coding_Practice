class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:
    head = None

    def __init__(self, val=None):
        if val is not None:
            self.head = Node(val)

    def printList(self):
        head = self.head
        while head is not None:
            print(head.val, end=" ")
            head = head.next
        print()

    def pushHead(self, val):
        if self.head is not None:
            n = Node(val)
            n.next = self.head
            self.head = n
        else:
            self.head = Node(val)

    def popHead(self):
        if self.head is None:
            return None

        val = self.head
        self.head = self.head.next
        return val.val


class LinkedListOperations:
    def operate(self):

        ll = LinkedList()

        # print(ll.head)
        ll.printList()

        ll.pushHead(5)
        ll.printList()

        print(ll.popHead())
        print(ll.popHead())


if __name__ == "__main__":

    llo = LinkedListOperations()

    llo.operate()
