public class ClassesAre {

    String name; // This attribute 'name' holds the state information for an instance of the ClassesAre class.
    static String name2; // This static variable 'name2' can be referenced by static methods and is associated with the class itself.

    public static void main(String[] args) { // static means it belongs to the class, not the object instances
        // The main method is the entry point for the Java program.
        // It can be used to demonstrate the functionality of the ClassesAre class.
        // Example usage: ClassesAre instance = new ClassesAre(); instance.declaresName();
    }

    // The declaresName method sets the value of the 'name' attribute to "Light."
    void declaresName() {
        System.out.println(name2);
        ClassesAre.main(); // Also possible to call the main method directly on the ClassesAre class.
        name = "Light";
    }

    // The getName method retrieves and returns the current value of the 'name' attribute.
    String getName() {
        return name;
    }
}
