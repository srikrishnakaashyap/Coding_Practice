import java.util.Arrays;

public class Operations {


    public void swap(int arr[], int index1, int index2){

        int temp = arr[index1];
        arr[index1] = arr[index2];
        arr[index2] = temp;
    }

    public void heapify(int[] arr, int index){
        int smallest = index;
        int left = index * 2;
        int right = index * 2 + 1;

        if(left < arr.length && arr[left] < arr[smallest]){

            smallest = left;
        }

        if(right < arr.length && arr[right] < arr[smallest]){

            smallest = right;
        }

        if(smallest != index) {

            int temp = arr[index];
            arr[index] = arr[smallest];
            arr[smallest] = temp;

            this.heapify(arr, smallest);

        }

    }


    public void heapHelper(int[] arr){

        int start = arr.length / 2;

        for(int i = start; i > 0; i--){

            this.heapify(arr, i);

        }
    }


    public static void main(String args[]){

        int arr[] = { 0, 100, 19, 36, 17, 3, 25, 1, 2, 7 };

        Operations ops = new Operations();

        ops.heapHelper(arr);

        System.out.println(Arrays.toString(arr));
    }
    
}
