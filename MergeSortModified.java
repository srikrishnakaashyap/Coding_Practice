import java.util.*;

public class MergeSortModified {

    public void merge(int arr[], int start, int mid, int end, int aux[]) {

        int left = start;
        int right = mid + 1;

        int ctr = start;

        while (left <= mid && right <= end) {
            if (aux[left] < aux[right]) {
                arr[ctr] = aux[left];
                left++;
            } else {
                arr[ctr] = aux[right];
                right++;
            }
            ctr++;
        }

        while (left <= mid) {
            arr[ctr] = aux[left];
            ctr++;
            left++;
        }

        while (right <= end) {
            arr[ctr] = aux[right];
            ctr++;
            right++;
        }

        // return ans;

    }

    public void mergeSort(int arr[], int start, int end, int aux[]) {

        if (start < end) {

            int mid = start + (end - start) / 2;
            this.mergeSort(aux, start, mid, arr);
            this.mergeSort(aux, mid + 1, end, arr);
            this.merge(arr, start, mid, end, aux);

        }

    }

    public void mergeSortHelper(int arr[]) {

        int[] auxilliary = Arrays.copyOfRange(arr, 0, arr.length);
        this.mergeSort(arr, 0, arr.length - 1, auxilliary);

        System.out.println(Arrays.toString(arr));
    }

    public static void main(String args[]) {

        int arr[] = { 8, 5, 2, 9, 5, 6, 3 };
        int length = arr.length;

        MergeSortModified msm = new MergeSortModified();

        // ms.mergeSort(arr, length);

        // System.out.println(Arrays.toString(ms.mergeSortHelper(arr)));
        msm.mergeSortHelper(arr);

    }

}
