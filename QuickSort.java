import java.util.Arrays;

public class QuickSort {

    public void quickSort(int arr[]) {

        this.quickSortHelper(arr, 0, arr.length - 1);

        System.out.println(Arrays.toString(arr));

    }

    public void swap(int index1, int index2, int arr[]) {

        int temp = arr[index1];
        arr[index1] = arr[index2];
        arr[index2] = temp;
    }

    public int partition(int arr[], int start, int end) {

        int pivot = end;

        int left = start;
        int right = end - 1;

        while (left <= right) {

            if (arr[left] <= arr[pivot]) {
                left++;
            }
            if (arr[right] > arr[pivot]) {
                right--;
            }
            if (arr[left] > arr[pivot] && arr[right] <= arr[pivot]) {
                this.swap(left, right, arr);
            }
        }

        this.swap(left - 1, pivot, arr);
        return left;

    }

    public void quickSortHelper(int arr[], int start, int end) {

        if (start < end) {

            int pi = this.partition(arr, start, end);

            this.quickSortHelper(arr, start, pi - 1);
            this.quickSortHelper(arr, pi + 1, end);
        }

    }

    public static void main(String args[]) {

        int arr[] = { 8, 5, 2, 9, 5, 6, 3 };

        QuickSort qs = new QuickSort();

        qs.quickSort(arr);
    }

}
