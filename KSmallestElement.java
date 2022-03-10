import java.util.Arrays;
import java.util.ArrayList;
import java.util.Collections;
import java.util.*;

public class KSmallestElement {

    public void swap(int index1, int index2, int arr[]){

        int temp = arr[index1];
        arr[index1] = arr[index2];
        arr[index2] = temp;
    }

    public int partition(int arr[], int left, int right, int index){

        int i = left - 1;

        this.swap(index, right, arr);
        int pivot = arr[right];

        for(int j = left; j <= right - 1; j++){

            if(arr[j] <= pivot){
                i++;
                this.swap(i, j, arr);
            }
        }
        i++;
        this.swap(i, right, arr);
        return i;
    }

    public int median(ArrayList<Integer> arr){
        Collections.sort(arr);

        int answer = arr.get(arr.size() / 2);
        return answer;
    }

    public ArrayList<Integer> getMedians(ArrayList<Integer> lst){

        ArrayList<Integer> answer = new ArrayList<Integer>();

        int start = 0; 
        int end = lst.size();
        while(start < end){
            int last = start + 5;
            last = Math.min(last, end);
            ArrayList<Integer> al = new ArrayList<>(lst.subList(start, last));
            answer.add(this.median(al));

            start = start + 5;
        }
        return answer;

    }

    public int recurse(ArrayList<Integer> lst){
        if(lst.size() <= 2){
            int ans = (int) lst.get(0);
            return ans;
        }
        return this.recurse(this.getMedians(lst));
    }

    public static int[] convertIntegers(ArrayList<Integer> integers) {

    int[] ret = new int[integers.size()];
    for (int i=0; i < ret.length; i++)
    {
        ret[i] = integers.get(i).intValue();
    }
    return ret;
    }
    public int helper(ArrayList<Integer> arr, int k, int start, int end){
        int ans = this.recurse(arr);

        int index = arr.indexOf(ans);

        int array[] = convertIntegers(arr);

        this.partition(array, start, end, index);

        if(index == k){
            return array[index];
        }
        if(index < k){
            return this.helper(arr, k - index, index + 1, end);
        }
        else{
            return this.helper(arr, k, start, index - 1);
        }


        // return ans;
    }


    public static void main(String args[]){

        int arr[] = {7, 10, 4, 3, 20, 15};
        int k = 3;
        KSmallestElement kse = new KSmallestElement();

        ArrayList<Integer> al = new ArrayList<>(Arrays.asList(7, 10, 4, 3, 20, 15));
        System.out.println(kse.helper(al, k, 0, al.size()) - 1);
    }
    
}
