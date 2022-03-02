import java.util.ArrayList;;

public class PowerSet {

    public void printPowerSet(int index, int arr[], ArrayList<Integer> al, ArrayList<ArrayList<Integer>> ans) {

        if (index >= arr.length) {
            ans.add(new ArrayList(al));
            return;
        }

        al.add(arr[index]);
        this.printPowerSet(index + 1, arr, al, ans);
        al.remove((Integer) arr[index]);
        this.printPowerSet(index + 1, arr, al, ans);

    }

    public static void main(String args[]) {

        int arr[] = { 3, 1, 2 };

        PowerSet ps = new PowerSet();

        ArrayList<ArrayList<Integer>> ans = new ArrayList<>();

        ps.printPowerSet(0, arr, new ArrayList<Integer>(), ans);

        System.out.println(ans);
    }
}
