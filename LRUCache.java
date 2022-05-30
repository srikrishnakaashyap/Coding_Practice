public class LRUCache {

  class Node {

    int data;
    Node next, prev;

    Node(int data) {
      this.data = data;
      this.next = this.prev = null;
    }
  }

  class LinkedList {

    Node head;
    Node tail;

    LinkedList(int data) {
      head = new Node(data);
    }

    public void insertAtHead(int data) {
      Node n = new Node(data);

      if (this.head == null) {
        this.head = new Node(data);
        this.tail = this.head;
      } else {
        n.next = this.head;
        this.head.prev = n;

        this.head = n;
      }
    }

    public void insertAtTail(int data) {
      Node n = new Node(data);

      if (this.tail == null) {
        this.tail = n;
        this.head = n;
      } else {
        this.tail.next = n;
        n.prev = this.tail;
        this.tail = n;
      }
    }
  }

  public static void main(String args[]) {}
}
