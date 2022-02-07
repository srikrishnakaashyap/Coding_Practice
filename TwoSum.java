import java.util.*;

public class TwoSum {

    public int[] twoSum(int[] arr, int target) {

        int[] answer = new int[2];

        HashMap<Integer, Integer> hm = new HashMap<>();

        for (int index = 0; index < arr.length; index++) {

            hm.put(arr[index], index);
        }

        System.out.println(hm);

        for (int index = 0; index < arr.length; index++) {

            if (hm.containsKey(target - arr[index])) {

                answer = new int[] { index, hm.get(target - arr[index]) };
            }

        }

        return answer;

    }

    public static void main(String args[]) {

        int arr[] = { 3, 3 };
        int target = 6;

        TwoSum ts = new TwoSum();
        System.out.println(Arrays.toString(ts.twoSum(arr, target)));

    }

}
