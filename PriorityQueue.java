class Element {

  int value;
  int priority;

  Element() {
    this.value = -1;
    this.priority = -1;
  }

  Element(int value, int priority) {
    this.value = value;
    this.priority = priority;
  }
}

public class PriorityQueue {

  Element heap[];
  int length;

  PriorityQueue() {
    Element e = new Element();
    this.heap = new Element[1];
    this.heap[0] = e;
    this.length = 1;
  }

  PriorityQueue(Element[] arr) {
    Element[] arr1 = new Element[arr.length + 1];

    arr1[0] = new Element();

    for (int i = 1; i < arr1.length; i++) {
      arr1[i] = arr[i - 1];
    }

    this.heap = arr1;
    this.length = arr1.length;

    this.buildQueue();
  }

  public void shiftDown(int index) {
    int smallest = index;
    int left = index * 2;
    int right = (index * 2) + 1;

    if (
      left < this.length &&
      this.heap[left].priority >= this.heap[smallest].priority
    ) {
      smallest = left;
    }

    if (
      right < this.length &&
      this.heap[right].priority > this.heap[smallest].priority
    ) {
      smallest = right;
    }

    if (smallest != index) {
      Element swap = this.heap[index];
      this.heap[index] = this.heap[smallest];
      this.heap[smallest] = swap;

      this.shiftDown(smallest);
    }
  }

  public void bubbleUp(int index) {}

  public void buildQueue() {
    int n = this.length / 2;

    for (int i = n; i > 0; i--) {
      this.shiftDown(i);
    }
  }

  public void printPriority() {
    for (int i = 0; i < this.length; i++) {
      System.out.print(this.heap[i].priority + " ");
    }
  }

  public Element peek() {
    return this.heap[0];
  }

  public Element extractMin() {
    // Element toReturn = new Element()
    if (this.length > 1) {
      this.length--;
      Element toReturn = heap[0];
      heap[0] = heap[this.length - 1];
      this.shiftDown(0);
      return toReturn;
    }
    return new Element();
  }

  public static void main(String args[]) {
    Element e1 = new Element(5, 1);
    Element e2 = new Element(4, 2);
    Element e3 = new Element(3, 3);
    Element e4 = new Element(2, 4);
    Element e5 = new Element(1, 5);
    Element e6 = new Element(1, 6);
    Element e7 = new Element(1, 7);
    Element e8 = new Element(1, 8);
    Element e9 = new Element(1, 9);
    Element e10 = new Element(1, 10);

    Element arr[] = { e1, e2, e3, e4, e5, e6, e7, e8, e9, e10 };

    PriorityQueue pq = new PriorityQueue(arr);

    pq.printPriority();
    // pq.buildQueue();

  }
}
