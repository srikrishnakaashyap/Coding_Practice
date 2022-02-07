public class BinarySearch {

    public int binarySearch(int[] array, int target) {

        int left = 0;
        int right = array.length - 1;
        int mid = left + (right - left) / 2;

        while (left <= right) {

            mid = left + (right - left) / 2;
            if (array[mid] == target) {
                return mid;
            } else if (array[mid] > target) {
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }

        return mid;

    }

    public static void main(String args[]) {

        int arr[] = { 1, 3, 5, 6 };
        int target = 0;

        BinarySearch bs = new BinarySearch();

        System.out.println(bs.binarySearch(arr, target));

    }

}
