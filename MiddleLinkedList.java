public class MiddleLinkedList {

    public Node middleNode(Node head) {

        Node fastPtr = head;
        Node slowPtr = head;

        while (fastPtr != null && fastPtr.next != null) {
            fastPtr = fastPtr.next.next;
            slowPtr = slowPtr.next;
        }

        return slowPtr;

    }

    public static void main(String args[]) {

        LinkedList ll = new LinkedList(1);
        ll.head.next = new Node(2);
        ll.head.next.next = new Node(3);
        ll.head.next.next.next = new Node(4);
        ll.head.next.next.next.next = new Node(5);
        ll.head.next.next.next.next.next = new Node(6);

        ll.printList(ll.head);

        MiddleLinkedList mll = new MiddleLinkedList();
        Node mid = mll.middleNode(ll.head);

        System.out.println(mid.val);

    }

}
