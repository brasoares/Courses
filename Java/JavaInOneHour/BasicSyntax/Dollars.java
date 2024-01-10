public class Dollars{
    public static void main(String[] args) {
        // Printing a message indicating the purpose.
        System.out.println("Learning the basics.");

        // Array declarations.
        BigDecimal[] dollars = {1000000, 1008520, 9050307};
    }
}
/*
* Using double for representing money can lead to precision issues due to the way floating-point numbers are stored 
* in computers. Floating-point arithmetic might introduce small rounding errors, 
* which can accumulate over time and result in incorrect calculations.

* In Java, it's generally recommended to use the BigDecimal class for precise arithmetic with currency values.
* BigDecimal is designed to handle arbitrary precision and avoids the rounding errors 
* associated with floating-point numbers. 
*/
