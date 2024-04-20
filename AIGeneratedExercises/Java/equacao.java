import java.util.Scanner;

public class EncontrarIncognita {
  public static void main(String[] args) {
    Scanner scanner = new Scanner(System.in);

    System.out.println("Enter the values of a, b, and c in the equation ax + b = c:");
    System.out.print("a: ");
    double a = scanner.nextDouble();

    System.out.print("b: ");
    double b = scanner.nextDouble();

    System.out.print("c: ");
    double c = scanner.nextDouble();

    // Encontrando a incógnita x
    double x = (c - b) / a;

    System.out.println("The value of the unknown x is: " + x);
  }
}
