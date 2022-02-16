import java.util.*;

public class MergeSort {

    public void merge(int arr[], int start, int mid, int end) {

        int length1 = mid - start + 1;
        int length2 = end - mid;

        int left[] = new int[length1];
        int right[] = new int[length2];

        for (int i = 0; i < length1; i++) {
            left[i] = arr[start + i];
        }
        for (int i = 0; i < length2; i++) {
            right[i] = arr[mid + 1 + i];
        }

        int ctr1 = 0, ctr2 = 0;
        int ctr = start;
        while (ctr1 < length1 && ctr2 < length2) {
            if (left[ctr1] < right[ctr2]) {
                arr[ctr] = left[ctr1];
                ctr1++;
            } else {
                arr[ctr] = right[ctr2];
                ctr2++;
            }
            ctr++;
        }

        if (ctr1 < length1) {
            while (ctr1 < length1) {
                arr[ctr] = left[ctr1];
                ctr++;
                ctr1++;
            }

        }

        if (ctr2 < length2) {
            while (ctr2 < length2) {
                arr[ctr] = right[ctr2];
                ctr2++;
                ctr++;
            }

        }

        // return ans;

    }

    public void mergeSort(int arr[], int start, int end) {

        if (start < end) {

            int mid = start + (end - start) / 2;
            this.mergeSort(arr, start, mid);
            this.mergeSort(arr, mid + 1, end);
            this.merge(arr, start, mid, end);

        }

    }

    public void mergeSortHelper(int arr[]) {
        this.mergeSort(arr, 0, arr.length - 1);

        System.out.println(Arrays.toString(arr));
    }

    public static void main(String args[]) {

        int arr[] = { 8, 5, 2, 9, 5, 6, 3 };
        int length = arr.length;

        MergeSort ms = new MergeSort();

        // ms.mergeSort(arr, length);

        // System.out.println(Arrays.toString(ms.mergeSortHelper(arr)));
        ms.mergeSortHelper(arr);

    }

}
