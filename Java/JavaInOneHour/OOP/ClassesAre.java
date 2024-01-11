/*
 * Classes are fundamental building blocks in Java programs, allowing us to model objects.
 * Objects have attributes representing their state and behaviors declared through methods.
 */

// Attributes are variables that define the state of an object.

public class ClassesAre {

    String name; // This attribute 'name' holds the state information for an instance of the ClassesAre class.
    static String name2; // This one can be referenced by the static main as it is static && also, in the other methods, this one can be referenced!

    public static void main(String[] args) { // static means it belongs to the class, not the object instances
        // The main method is the entry point for the Java program.
        // It can be used to demonstrate the functionality of the ClassesAre class.
        /*
        * String cannot be called here, as it would present an error such as:
        * "Non-static field 'name' cannot be referenced from a static context" IntelliJ
        * It is due to the fact that this static belongs to the class ClassesAre itself, not an instance
        */
    }

    // The declaresName method sets the value of the 'name' attribute to "Light."
    void declaresName() {
        name = "Light";
    }

    // The getName method retrieves and returns the current value of the 'name' attribute.
    String getName() {
        return name;
    }
}
