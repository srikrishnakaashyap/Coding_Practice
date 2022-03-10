import java.util.Arrays;

public class Partition {

    public void swap(int index1, int index2, int arr[]){

        int temp = arr[index1];
        arr[index1] = arr[index2];
        arr[index2] = temp;

        // arr[index1], arr[index2] = arr[index2], arr[index1];
    }
    
    public int partition(int arr[], int left, int right){

        int i = left - 1;

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

    public void partitionHelper(int arr[]){

        int partition = this.partition(arr, 0, arr.length - 1);

        System.out.println(partition);
        System.out.println(Arrays.toString(arr));

    }

    public static void main(String args[]) {

        int arr[] = { 8, 5, 2, 9, 5, 6, 3 };

        Partition p = new Partition();

        p.partitionHelper(arr);
    }
}
