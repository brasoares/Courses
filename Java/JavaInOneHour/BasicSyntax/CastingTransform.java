public class CastingTransform {
    public static void main(String[] args) {
        int age1 = 22;
        double age2 = age1;

        // not allowed: age1 = age2; as the double is bigger than the int!
        // But an explicit casting is possible

        age1 = (int) age2;

        char letter = 'A';
        // String name = letter; not allowed, but:
        String name = String.valueOf(letter);
        letter = name.charAt(0);
    }
}
