import java.util.Scanner;

public class EncontrarIncognita {
  public static void main(String[] args) {
    Scanner scanner = new Scanner(System.in);

    System.out.println("Digite os valores de a, b e c na equação ax + b = c:");
    System.out.print("a: ");
    double a = scanner.nextDouble();

    System.out.print("b: ");
    double b = scanner.nextDouble();

    System.out.print("c: ");
    double c = scanner.nextDouble();

    // Encontrando a incógnita x
    double x = (c - b) / a;

    System.out.println("O valor da incógnita x é: " + x);
  }
}
