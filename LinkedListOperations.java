public class LinkedListOperations {

  public static Node getNode(Node node) {
    while (node.next != null) {
      node = node.next;
    }

    return node;
  }

  public static Node pushHead(Node head, String value) {
    Node n = new Node(value);
    n.next = head;
    return n;
  }

  public static Node popHead(Node head) {
    head = head.next;
    return head;
  }

  public static Node pushTail(Node tail, String val) {
    Node n = new Node(val);

    tail.next = n;
    return n;
  }

  public void operations(String[][] queries) {
    LinkedList ll = new LinkedList();

    ll.head = new Node(1);

    Node tail = getNode(ll.head);
    Node head = ll.head;

    for (int i = 0; i < queries.length; i++) {
      if (queries[i][0] == "PUSH HEAD") {
        head = pushHead(head, queries[i][1]);
      } else if (queries[i][0] == "PUSH TAIL") {
        tail = pushTail(tail, queries[i][1]);
      } else {
        head = popHead(head);
      }
    }
  }
}
