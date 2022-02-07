import java.lang.*;

public class MaximumSubarray {

    public int maxSubArray(int[] nums) {

        int length = nums.length;

        if (length == 1) {
            return nums[0];
        }

        int max = 0;

        max = nums[0];

        for (int i = 0; i < nums.length; i++) {
            max = nums[i] + max;
            max = Math.max(max, nums[i]);
            if (nums[i] < 0) {
                nums[i] = 0;
            }
        }
        return max;
    }

    public static void main(String args[]) {

        int[] nums = { -2, 1 };

        MaximumSubarray ms = new MaximumSubarray();

        System.out.println(ms.maxSubArray(nums));

        // ms.maxSubArray(nums);

    }
}