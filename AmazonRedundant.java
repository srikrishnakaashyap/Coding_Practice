public class AmazonRedundant {

  public static int numberSegments(String a) {
    int answer = 1;

    int hash[] = new int[26];

    hash[(int) a.charAt(0) - 97]++;

    for (int i = 1; i < a.length(); i++) {
      if (hash[(int) a.charAt(i) - 97] == 1) {
        answer++;
        hash = new int[26];
      }
      hash[(int) a.charAt(i) - 97]++;
    }

    return answer;
  }

  public static void main(String args[]) {
    String a = "aabcdea";

    System.out.println(numberSegments(a));
  }
}
