/* Write a function that accepts an array of 10 integers (between 0 and 9), that returns a string of those numbers in the form of a phone number.
 
 Example:
 Kata.createPhoneNumber(new int[] {1, 2, 3, 4, 5, 6, 7, 8, 9, 0}) // => returns "(123) 456-7890"
 
 The returned format must be correct in order to complete this challenge.

 Don't forget the space after the closing parentheses!

*/

public class Kata {
  public static String createPhoneNumber(int[] numbers) {
      // Convert the array's values into a formatted US phone number style for the output
      StringBuilder sb = new StringBuilder("(");
      // Append first three values in the format of (XXX)
      for (int i = 0; i < 3; i++) {
        sb.append(numbers[i]);
      }
      sb.append(") ");
  }
}
