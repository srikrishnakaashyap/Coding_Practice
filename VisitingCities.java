import java.util.*;

public class VisitingCities {

  public int[] visitingCities(int blue[], int red[], int blueCost) {
    int m = blue.length;
    int n = red.length;

    int d = Math.min(m, n);

    int[] ans = new int[d + 1];

    int count = 0;
    for (int i = 1; i < d + 1; i++) {
      if (count == 0) {
        if (red[i - 1] >= blue[i - 1] + blueCost) {
          ans[i] = blue[i - 1] + blueCost + ans[i - 1];
          count = 1;
        } else {
          ans[i] = red[i - 1] + ans[i - 1];
        }
      } else {
        if (red[i - 1] >= blue[i - 1]) {
          ans[i] = blue[i - 1] + ans[i - 1];
        } else {
          ans[i] = red[i - 1] + ans[i - 1];
          count = 0;
        }
      }
    }

    return ans;
  }

  public static void main(String args[]) {
    int blueCost = 2;
    int red[] = { 2, 3, 4 };
    int blue[] = { 3, 1, 1 };

    VisitingCities vc = new VisitingCities();

    System.out.println(Arrays.toString(vc.visitingCities(blue, red, blueCost)));
  }
}
