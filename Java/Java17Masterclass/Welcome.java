// This is an IntelliJ's Community Edition walkthrough code.
// As I have studied it to learn it does not start exactly like this in their turorial, it is here.

import java.util.Arrays;
import java.util.List;

class Welcome {
    public static void main(String[] args) {
        int[] array = {5, 6, 7, 8};
        System.out.println("AVERAGE of array " + Arrays.toString(array) + " is " + findAverage(array));
    }

    private static double findAverage(int[] values) {
        double result = 0;
        for (int value : values) {
            result += value;
        }
        return result;
    }
}
