public class MaximumSubarray{

    public int maxSubArray(int[] nums){

        int length = nums.length;

        
        if(length == 1){
            return nums[0];
        }

        return -1;
    }


    public static void main(String args[]){

        int[] nums = {-2,1,-3,4,-1,2,1,-5,4};

        MaximumSubarray ms = new MaximumSubarray();

        ms.maxSubArray(nums);



    }
}