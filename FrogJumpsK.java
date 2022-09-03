import java.util.*;

public class FrogJumpsK {

  public static long recur(int index, int[] paths, long dp[], int k) {
    if (index == 0) {
      return paths[index];
    }

    if (index < 0) {
      return -1000000;
    }

    if (dp[index] != -1) {
      return dp[index];
    }

    long ans = -1000000;
    for (int j = 1; j <= k; j++) {
      ans = Math.max(ans, paths[index] + recur(index - j, paths, dp, k));
    }

    dp[index] = ans;

    return ans;
  }

  public static long solve(int n, int[] paths, int maxLength) {
    long[] dp = new long[n];

    Arrays.fill(dp, -1);

    dp[0] = paths[0];

    for (int i = 1; i < n; i++) {
      long ans = -1000000;
      for (int j = i - 1; j >= (i - k); j--) {
        if (j >= 0) ans =
          Math.max(ans, paths[i] + recur(index - j, paths, dp, k));
      }
      dp[i] = ans;
    }

    return dp[n - 1];
    // long ans = recur(n - 1, paths, dp, maxLength);

    // return ans;
  }

  public static void main(String args[]) {
    int height[] = { 100, -70, -90, -80, 100 };
    int n = height.length;
    int k = 3;
    System.out.println(solve(n, height, k));
  }
}
    int k = 3;
    System.out.println(solve(n, height, k));
  }
}
