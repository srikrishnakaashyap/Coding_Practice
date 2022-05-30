import java.util.Arrays;

public class Trie {

  Trie arr[];
  boolean flag;

  public Trie() {
    arr = new Trie[26];
    flag = false;
  }

  public void insert(String word) {
    int n = word.length();
    int i = 0;

    Trie array[] = this.arr;
    Trie obj = this;

    while (i < n) {
      if (array[(int) word.charAt(i) - 97] != null) {
        obj = array[(int) word.charAt(i) - 97];
        array = obj.arr;
      } else {
        obj = new Trie();
        array[(int) word.charAt(i) - 97] = obj;
        array = obj.arr;
      }
      i++;
    }

    obj.flag = true;
  }

  public boolean search(String word) {
    int i = 0;
    int n = word.length();

    Trie array[] = this.arr;
    Trie obj = this;

    while (i < n) {
      if (array[(int) word.charAt(i) - 97] != null) {
        obj = array[(int) word.charAt(i) - 97];
        array = obj.arr;
      } else {
        return false;
      }
      i++;
    }
    if (obj.flag) return true;
    return false;
  }

  public boolean startsWith(String word) {
    int i = 0;
    int n = word.length();

    Trie array[] = this.arr;
    Trie obj = this;

    while (i < n) {
      if (array[(int) word.charAt(i) - 97] != null) {
        obj = array[(int) word.charAt(i) - 97];
        array = obj.arr;
      } else {
        return false;
      }
      i++;
    }

    return true;
  }

  public static void main(String args[]) {
    Trie trie = new Trie();

    trie.insert("apple");
    System.out.println(trie.search("apple"));
    System.out.println(trie.startsWith("app"));
    // System.out.println(trie.search(""));
    // System.out.println(trie.search("apple"));

  }
}
