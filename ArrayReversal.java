import java.util.Arrays;

public class ArrayReversal {

    public void swap(int arr[], int first, int second) {
        int temp = arr[first];
        arr[first] = arr[second];
        arr[second] = temp;
    }

    public void reverseArray(int arr[], int left, int right) {

        if (left < right) {
            this.swap(arr, left, right);
            this.reverseArray(arr, left + 1, right - 1);
        }
        return;

    }

    public static void main(String args[]) {

        int arr1[] = { 1, 2, 3, 4, 5 };
        int arr2[] = { 1, 2, 3, 4, 5, 6 };
        int arr3[] = {};

        ArrayReversal ar = new ArrayReversal();

        ar.reverseArray(arr1, 0, arr1.length - 1);
        ar.reverseArray(arr2, 0, arr2.length - 1);
        ar.reverseArray(arr3, 0, arr3.length - 1);

        System.out.println(Arrays.toString(arr1));
        System.out.println(Arrays.toString(arr2));
        System.out.println(Arrays.toString(arr3));

    }

}
