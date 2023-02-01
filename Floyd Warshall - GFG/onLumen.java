class Parent {

  String value = "Parent";

  String getValue() {
    return value;
  }
}

class Child extends Parent {

  String value = "Child";

  String getValue() {
    return value;
  }
}

public class onLumen {

  public static void main(String[] args) {
    Parent child = new Child();

    System.out.println(child.value + "&" + child.getValue());
  }
}
