public class Palindrome {

    public boolean isPalindrome(String str, int left, int right) {

        if (left < right) {

            if (str.charAt(left) != str.charAt(right)) {
                return false;
            }

            return isPalindrome(str, left + 1, right - 1);

        }

        return true;
    }

    public static void main(String args[]) {

        Palindrome p = new Palindrome();

        String str1 = "nitin";
        String str2 = "appa";
        String str3 = "danny";
        String str4 = "dannys";

        System.out.println(p.isPalindrome(str1, 0, str1.length() - 1));
        System.out.println(p.isPalindrome(str2, 0, str2.length() - 1));
        System.out.println(p.isPalindrome(str3, 0, str3.length() - 1));
        System.out.println(p.isPalindrome(str4, 0, str4.length() - 1));

    }

}
