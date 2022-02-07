import java.util.Arrays;

public class SortedSquares {

    public int[] sortedSquares(int[] nums) {

        int length = nums.length;
        int answer[] = new int[length];

        int pos = 0;

        while (pos < length && nums[pos] < 0) {
            pos++;
        }

        System.out.println("POS: " + pos);

        int left = pos - 1;
        int right = pos;
        pos = 0;

        while (left >= 0 && right < length) {

            if ((int) Math.abs(nums[left]) <= nums[right]) {
                answer[pos] = (int) Math.pow(nums[left], 2);
                left--;
            } else {
                answer[pos] = (int) Math.pow(nums[right], 2);
                right++;
            }
            pos++;

        }

        if (left >= 0) {

            while (left >= 0) {
                answer[pos] = (int) Math.pow(nums[left], 2);
                left--;
                pos++;
            }
        }

        if (right < length) {

            while (right < length) {
                answer[pos] = (int) Math.pow(nums[right], 2);
                right++;
                pos++;
            }
        }

        return answer;

    }

    public static void main(String args[]) {

        int[] nums = { -1 };

        SortedSquares sq = new SortedSquares();
        System.out.println(Arrays.toString(sq.sortedSquares(nums)));

    }

}
