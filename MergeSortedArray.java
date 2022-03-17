import java.util.Arrays;

public class MergeSortedArray {

  public int[] mergeSortedArray(int[] nums1, int m, int[] nums2, int n) {
    int counter = m + n - 1;
    int left = m - 1;
    int right = n - 1;

    while (counter >= 0 && left >= 0 && right >= 0) {
      if (nums1[left] >= nums2[right]) {
        nums1[counter] = nums1[left];
        left--;
      } else {
        nums1[counter] = nums2[right];
        right--;
      }
      counter--;
    }

    if (left >= 0) {
      while (left >= 0) {
        nums1[counter] = nums1[left];
        left--;
        counter--;
      }
    }

    if (right >= 0) {
      while (right >= 0) {
        nums1[counter] = nums2[right];
        right--;
        counter--;
      }
    }

    return nums1;
  }

  public static void main(String args[]) {
    int nums1[] = { 1, 2, 3, 0, 0, 0 };
    int nums2[] = { 1, 5, 6 };

    int m = 3;
    int n = 3;

    MergeSortedArray msa = new MergeSortedArray();
    System.out.println(
      Arrays.toString(msa.mergeSortedArray(nums1, m, nums2, n))
    );
    // msa.mergeSortedArray(nums1, m, nums2, n);

    // System.out.println(Arrays.toString(msa.merge(nums1, m, nums2, n)));
  }
}
