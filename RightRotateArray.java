import java.util.Arrays;

public class RightRotateArray {

    public int[] rightRotateArray(int[] nums, int k) {

        int length = nums.length;
        k = k % length;

        // if(length %2 == 0)
        int ctr = length;
        int pos = 0;
        int curr_value = nums[pos];
        int new_pos = (pos + k) % length;

        System.out.println("1: " + ctr);
        System.out.println("2: " + curr_value);
        System.out.println("3: " + new_pos);
        // System.out.println("1: " + ctr);
        // System.out.println("1: " + ctr);

        // int new_value = nums[new_pos];

        while (ctr > 0) {

            int new_value = nums[new_pos];

            nums[new_pos] = curr_value;

            pos = new_pos;

            new_pos = (pos + k) % length;

            curr_value = new_value;

            System.out.println(ctr + " " + Arrays.toString(nums));

            ctr--;
        }
        return nums;
    }

    public static void main(String args[]) {

        int nums[] = { 1, 2, 3, 4, 5, 6 };
        int k = 2;

        RightRotateArray rra = new RightRotateArray();
        System.out.println(Arrays.toString(rra.rightRotateArray(nums, k)));

    }

}
