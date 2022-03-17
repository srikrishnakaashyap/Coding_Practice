public class MooresVoting {

    public int maxRepeating(int[] arr, int n) {

        int element = 0;
        int count = 0;

        for(int i = 0; i < n; i++){

            if(count == 0) {
                element = arr[i];
            }
            if(element == arr[i]){
                count++;
            }
            else{
                count--;
            }

        }
        return element;
    }

    public static void main(String args[]) {

        int arr[] = {2,2,1,1,1,2,2};

        MooresVoting mv = new MooresVoting();

        System.out.println(mv.maxRepeating(arr, arr.length));
    }
}
