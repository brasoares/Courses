public class ClassesAre {

    String name; // This attribute 'name' holds the state information for an instance of the ClassesAre class.
    static String name2; // This one can be referenced by the static main as it is static && also, in the other methods, this one can be referenced!

    public static void main(String[] args) { // static means it belongs to the class, not the object instances
        // The main method is the entry point for the Java program.
        // It can be used to demonstrate the functionality of the ClassesAre class.
        /*
        * String cannot be called here, as it would present an error such as:
        * "Non-static field 'name' cannot be referenced from a static context" in IntelliJ.
        * It is due to the fact that this static belongs to the class ClassesAre itself, not an instance.
        */
    }

    // The declaresName method sets the value of the 'name' attribute to "Light."
    void declaresName() {
        System.out.println(name2);
        ClassesAre.main(); // Also possible to call Main directly without creating a class object for the Main class.
        name = "Light";
    }

    // The getName method retrieves and returns the current value of the 'name' attribute.
    String getName() {
        return name;
    }
}
