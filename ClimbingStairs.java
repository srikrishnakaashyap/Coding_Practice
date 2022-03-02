import java.util.*;

public class ClimbingStairs {

    public long climbStairs(long n) {

        if (n == 0) {
            return 1;
        }

        long arr[] = new long[(int) n];
        arr[0] = 1;
        arr[1] = 2;
        for (int i = 2; i < arr.length; i++) {
            arr[i] = arr[i - 1] + arr[i - 2];
        }

        return arr[(int) n - 1];
    }

    public static void main(String args[]) {

        ClimbingStairs cs = new ClimbingStairs();

        long n = 92;
        System.out.println(cs.climbStairs(n));
        // cs.climbStairs(n, 0);
    }

}
