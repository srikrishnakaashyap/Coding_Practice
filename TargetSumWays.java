import java.util.Arrays;

public class TargetSumWays {

  public static int numWays(int index, int[] arr, int remaining, int[][] dp) {
    if (index == 0 && remaining % arr[index] == 0) {
      return 1;
    }

    if (dp[index][remaining] != -1) {
      return dp[index][remaining];
    }
    dp[index][remaining] =
      numWays(index - 1, arr, remaining, dp) +
      numWays(index, arr, remaining - arr[index], dp);

    return dp[index][remaining];
  }

  public static void main(String args[]) {
    int k = 2;
    int total = 4;

    int arr[] = new int[k];

    for (int i = 1; i <= k; i++) {
      arr[i - 1] = i;
    }

    int dp[][] = new int[k][total];

    Arrays.fill(dp, -1);

    System.out.println(Arrays.toString(dp));

    System.out.println(numWays(k - 1, arr, total, dp));
  }
}
