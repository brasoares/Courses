/******************************************************************************

                            Online Java Compiler.
                Code, Compile, Run and Debug java program online.
Write your code in this editor and press "Run" button to execute it.

*******************************************************************************/

// Sieve of Erastosthenes algorithm

public class PrimeGenerator {
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
    for (int i = 0; i <= n; i++)
      prime[i] = true;

    for (int p = 2; p * p <= n; p++) {
      // If prime[p] is not changed, then it is a prime
      if (prime[p]) {
        // Update all multiples of p
        for (int i = p * p; i <= n; i += p)
          prime[i] = false;
      }
    }

    // Print all prime numbers
    for (int i = m; i <= n; i++) {
      if (prime[i])
        System.out.println(i);
    }
  }
