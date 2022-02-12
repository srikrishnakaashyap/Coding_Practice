class Node {
    int val;
    Node next;

    Node(int val) {
        this.val = val;
        next = null;
    }

}

public class LinkedList {

    Node head;

    LinkedList(int val) {
        this.head = new Node(val);
        // this.head = head;
    }

    LinkedList() {
        this.head = null;
    }

    public void printList(Node head) {
        while (head != null) {
            System.out.print(head.val + " ");
            head = head.next;
        }

        System.out.println();
    }

}
