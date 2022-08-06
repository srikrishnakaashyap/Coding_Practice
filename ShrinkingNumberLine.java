import java.util.ArrayList;
import java.util.List;

public class ShrinkingNumberLine {

  public static int minimize(int[] point, int k) {
    if (point == null || point.length == 0) {
      return -1;
    }

    int incre = dfs(point, k, 1, point[0] + k, point[0] + k);
    int decre = dfs(point, k, 1, point[0] - k, point[0] - k);

    return Math.min(incre, decre);
  }

  public static int dfs(int[] point, int k, int idx, int min, int max) {
    if (idx >= point.length) {
      return max - min;
    }

    int min_incre = Math.min(min, point[idx] + k);
    int max_incre = Math.max(max, point[idx] + k);
    int incre = dfs(point, k, idx + 1, min_incre, max_incre);

    int min_decre = Math.min(min, point[idx] - k);
    int max_decre = Math.max(max, point[idx] - k);
    int decre = dfs(point, k, idx + 1, min_decre, max_decre);

    return Math.min(incre, decre);
  }

  public static int minimize2(int[] point, int k) {
    if (point == null || point.length == 0) {
      return -1;
    }
    List<Integer> list = new ArrayList<>();
    return dfs2(point, k, 0, list);
  }

  public static int dfs2(int[] point, int k, int idx, List<Integer> list) {
    if (idx >= point.length) {
      int min = Integer.MAX_VALUE;
      int max = Integer.MIN_VALUE;
      for (int i = 0; i < list.size(); i++) {
        min = Math.min(min, list.get(i));
        max = Math.max(max, list.get(i));
      }
      //System.out.println(list.toString());
      return max - min;
    }

    list.add(point[idx] + k);
    int incre = dfs2(point, k, idx + 1, list);
    list.remove(list.size() - 1);

    list.add(point[idx] - k);
    int decre = dfs2(point, k, idx + 1, list);
    list.remove(list.size() - 1);

    return Math.min(incre, decre);
  }

  public static void main(String[] args) {
    System.out.println(minimize(new int[] { -3, 0, 1 }, 3)); //3
    // System.out.println(minimize2(new int[] { -3, 0, 1 }, 3)); //3

    // System.out.println(minimize(new int[] { 4, 7, -7 }, 5)); //4
    // System.out.println(minimize2(new int[] { 4, 7, -7 }, 5)); //4

    // System.out.println(minimize(new int[] { -100000, 100000 }, 100000)); //0
    // System.out.println(minimize2(new int[] { -100000, 100000 }, 100000)); //0
  }
}
