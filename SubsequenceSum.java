import java.util.ArrayList;

public class SubsequenceSum {

    public void printSubsequenceSum(int index, int arr[], ArrayList<Integer> al, ArrayList<ArrayList<Integer>> ans,
            int sum,
            int k) {

        if (index >= arr.length) {
            if (sum == k) {
                ans.add(new ArrayList(al));
            }

            return;
        }
        al.add(arr[index]);
        sum = sum + arr[index];
        this.printSubsequenceSum(index + 1, arr, al, ans, sum, k);
        al.remove((Integer) arr[index]);
        sum = sum - arr[index];
        this.printSubsequenceSum(index + 1, arr, al, ans, sum, k);

    }

    public static void main(String args[]) {

        int arr[] = { 1, 2, 1 };

        SubsequenceSum ss = new SubsequenceSum();

        ArrayList<ArrayList<Integer>> ans = new ArrayList<>();

        ss.printSubsequenceSum(0, arr, new ArrayList<Integer>(), ans, 0, 2);

        System.out.println(ans);
    }

}
