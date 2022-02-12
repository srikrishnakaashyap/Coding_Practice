import java.util.*;

public class LongestSubstring {

    public int lengthOfLongestSubstring(String string) {
        int length = 0;

        Set<Character> set = new HashSet<>();

        int i = 0, j = 0;

        while (i < string.length() && j < string.length() && i <= j) {
            if (!set.contains(string.charAt(j))) {
                set.add(string.charAt(j));
                length = Math.max(length, j - i);
                j++;
            } else {
                // arr[(int) string.charAt(i) - 97]--;
                set.remove(string.charAt(j));
                i++;
            }
        }

        return length;
    }

    public static void main(String args[]) {

        String string = "pwwkew";

        LongestSubstring ls = new LongestSubstring();

        System.out.println(ls.lengthOfLongestSubstring(string));
    }

}
