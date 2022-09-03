import java.util.*;

public class AmazonLogin {

  public static void main(String args[]) {
    String log[] = {
      "register david david123",
      "register adam 1Adam1",
      "login david david123",
      "login adam 1adam1",
      "logout david",
    };

    int n = log.length;

    HashMap<String, Integer> login = new HashMap<>();
    HashMap<String, String> registration = new HashMap<>();

    List<String> answer = new ArrayList<>();

    for (int i = 0; i < n; i++) {
      String query[] = log[i].split(" ");

      System.out.println(Arrays.toString(query));

      if (query[0].equals("logout")) {
        if (login.containsKey(query[1]) && login.get(query[1]) == 1) {
          answer.add("Logged Out Successfully");
          login.remove(query[1]);
        } else {
          answer.add("Logout Unsuccessful");
        }
      } else if (query[0].equals("register")) {
        if (registration.containsKey(query[1])) {
          answer.add("User already exists");
        } else {
          registration.put(query[1], query[2]);
          answer.add("Registered Successfully");
        }
      } else {
        if (
          registration.containsKey(query[1]) &&
          registration.get(query[1]).equals(query[2]) &&
          !(login.containsKey(query[1]))
        ) {
          login.put(query[1], 1);
          answer.add("Logged In Successfully");
        } else {
          answer.add("Login Unsuccessful");
        }
      }
    }

    System.out.println(answer);
  }
}
