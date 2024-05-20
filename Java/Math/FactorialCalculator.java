import java.util.Scanner;

public class FactorialCalculator {
  public static void main(String[] args) {
    Scanner scanner = new Scanner(System.in);
    System.out.print("Enter a positive integer: ");
    int number = scanner.nextInt();

    long factorial = calculateFactorial(number);

    System.out.println("Factorial of" + number + " = " + factorial);

    scanner.close();
  } 

  // Recursive method to calculate factorial
  private static long calculateFactorial(int n) {
    if (n == 0 || n == 1) {
      return 1;
    } else {
      return n * calculateFactorial(n - 1);
    }
  }
}
