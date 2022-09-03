import java.util.*;

public class AmazonServer {

  public static void main(String args[]) {
    int[] locations = { 1, 2, 3 };
    int[] movedFrom = { 1, 2 };
    int[] movedTo = { 5, 6 };

    int m = locations.length;
    int n = movedTo.length;

    // int i = 0

    HashSet<Integer> hs = new HashSet<>();

    for (int i = 0; i < m; i++) {
      hs.add(locations[i]);
    }

    for (int i = 0; i < n; i++) {
      hs.remove(movedFrom[i]);
      hs.add(movedTo[i]);
    }

    List<Integer> answer = new ArrayList<Integer>(hs);
  }
}
