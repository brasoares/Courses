import java.util.ArrayList;

public class MyArrayListExample {
  // ArrayList: Class to help represent a dynamic list
  public static void main(String[] args) {
    // It's necessary to tell what is going to be stored (type)
    // "Integer", the class is requested in this case (native from Java language, not being aprimitive type, but a class, as the case of String).
    ArrayList < Integer > age = new ArrayList < Integer > ();
    // We can manipulate the data inside via methods:
    age.add(22);
    age.add(33);
    age.add(44);
    age.remove(0);
    age.get(1);
    age.size();
    // Gather a length from normal circumstances:
    int[] age1 = new int[10];
    age1.length;
  }
}
