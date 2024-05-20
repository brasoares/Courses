import java.util.Scanner;

public class FactorialCalculator {
  public static void main(String[] args) {
    Scanner scanner = new Scanner(System.in);
    System.out.print("Enter a positive integer: ");
    int number = scanner.nextInt();

    long factorial = calculateFactorial(number);
  } 
}
