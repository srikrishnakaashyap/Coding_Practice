import java.util.*;

public class ContainsDuplicate{


    public boolean doesContainDuplicate(int[] nums){

        int length = nums.length;

        if(length == 1){
            return false;
        }

        HashSet<Integer> hs = new HashSet<>();


        for(int num: nums){

            if(!hs.contains(num)){
                hs.add(num);
            }
            else{
                return true;
            }

        }
        return false;
    }

    public static void main(String args[]){


        int nums[] = {1,1,1,3,3,4,3,2,4,2};

        ContainsDuplicate cd = new ContainsDuplicate();


        System.out.println(cd.doesContainDuplicate(nums));
    }
}