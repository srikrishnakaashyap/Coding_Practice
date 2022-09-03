import java.util.*;

public class Result {

  public static List<Integer> freqencyOfMaxValue(
    List<Integer> nums,
    List<Integer> queries
  ) {
    List<Integer> maxFreqVec = new ArrayList<>();
    // List<Integer> frequency = new ArrayList<>(nums.size());

    // System.out.println(maxFreqVec);
    int maxSoFar = 0;
    int maxFreq = 0;

    for (int i = nums.size() - 1; i >= 0; i--) {
      if (nums.get(i) > maxSoFar) {
        maxSoFar = nums.get(i);
        maxFreq = 1;
      } else if (nums.get(i) == maxSoFar) {
        maxFreq++;
      }

      maxFreqVec.add(0, maxFreq);
    }

    List<Integer> ret = new ArrayList<>();

    for (int q : queries) {
      ret.add(maxFreqVec.get(q - 1));
    }

    return ret;
  }

  public static List<Integer> freqencyOfMaxValue2(
    List<Integer> nums,
    List<Integer> queries
  ) {
    List<Integer> maxFreqVec = new ArrayList<>(nums.size());

    int maxSoFar = Integer.MIN_VALUE;
    int maxFreq = 0;

    for (int i = nums.size() - 1; i >= 0; i--) {
      if (nums.get(i) > maxSoFar) {
        maxSoFar = nums.get(i);
        maxFreq = 1;
      } else if (nums.get(i) == maxSoFar) {
        maxFreq++;
      }

      maxFreqVec.add(0, maxFreq);
    }

    List<Integer> ret = new ArrayList<>();

    for (int q : queries) {
      ret.add(maxFreqVec.get(q - 1));
    }

    return ret;
  }

  public static void main(String[] args) {
    List<Integer> nums = new ArrayList<>();
    List<Integer> queries = new ArrayList<>();

    nums.add(5);
    nums.add(4);
    nums.add(5);
    nums.add(3);
    nums.add(2);

    queries.add(1);
    queries.add(2);
    queries.add(4);
    queries.add(5);

    System.out.println("ans--" + freqencyOfMaxValue2(nums, queries));
  }
}
