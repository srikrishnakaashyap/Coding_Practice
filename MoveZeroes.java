import java.util.Arrays;

public class MoveZeroes {

    public int[] moveZeroes(int[] nums) {

        int ctr = 0;
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] != 0) {
                nums[ctr] = nums[i];
                ctr++;
            }
        }
        for (int i = ctr; i < nums.length; i++) {
            nums[i] = 0;
        }
        return nums;
    }

    public static void main(String args[]) {

        int nums[] = { 1, 0 };

        MoveZeroes mz = new MoveZeroes();
        System.out.println(Arrays.toString(mz.moveZeroes(nums)));
    }

}
