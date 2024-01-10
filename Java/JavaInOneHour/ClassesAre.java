/*
 * Classes are fundamental building blocks in Java programs, allowing us to model objects.
 * Objects have attributes representing their state and behaviors declared through methods.
 */

// Attributes are variables that define the state of an object.

public class ClassesAre {

    String name; // This attribute 'name' holds the state information for an instance of the ClassesAre class.

    public static void main(String[] args) {
        // The main method is the entry point for the Java program.
        // It can be used to demonstrate the functionality of the ClassesAre class.
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
