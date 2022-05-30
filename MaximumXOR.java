public class MaximumXOR {

  class Trie {

    Trie arr[];

    Trie() {
      arr = new Trie[2];
    }
  }

  public int getMaximumXOR(int[] nums) {
    int ans = 0;

    Trie root = new Trie();

    for (int num : nums) {
      Trie node = root;

      for (int i = 31; i >= 0; i--) {
        int bit = (num >> i) & 1;

        if (node.arr[bit] == null) {
          node.arr[bit] = new Trie();
        } else {
          node = node.arr[bit];
        }
      }
    }

    int answer = 0;

    for (int num : nums) {
      int temp = 0;
      Trie node = root;

      for (int i = 31; i >= 0; i--) {
        int bit = (num >> i) & 1;

        if (node.arr[1 - bit] != null) {
          temp = temp | (1 << i);
          node = node.arr[1 - bit];
        } else {
          node = node.arr[bit];
        }
      }

      answer = Math.max(answer, temp);
    }

    return answer;
  }

  public static void main(String args[]) {
    MaximumXOR mx = new MaximumXOR();

    int[] nums = { 3, 10, 5, 25, 2, 8 };

    System.out.println(mx.getMaximumXOR(nums));
  }
}
