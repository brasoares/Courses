/******************************************************************************

                            Online Java Compiler.
                Code, Compile, Run and Debug java program online.
Write your code in this editor and press "Run" button to execute it.

*******************************************************************************/

// Sieve of Erastosthenes algorithm

public class PrimeGenerator{
    public static void main(String[] args) {
        // Generates primes between 10 and 50
        int m = 10;
        int n = 50;
        boolean[] prime = new boolean[n + 1];
        sieveOfEratosthenes(m, n, prime);
    }
    
    public static void sieveOfEratosthenes(int m, int n, boolean[] prime) {
        // Initialize all entries as true. A value in prime[i] will
        // finally be false if i is NOT a prime, else true.
    }

