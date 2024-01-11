// The ConstructorsAre class defines a constructor that sets the 'name' attribute when an instance is created.
public class ConstructorsAre {

    String name;
    int age;

    static String name2;

    public static void main(String[] args) {
        System.out.println(name2);
    }

    // A constructor is a special method with the same name as the class.
    // It is called automatically every time a new instance of this class is created.
    // The access modifier 'public' here allows the constructor to be called from outside the class.
    // If the constructor is made private, it can only be called within the same class.
    public ConstructorsAre(String name) {
        this.name = name;
    }

    public ConstructorsAre(String name, int age) {
        this.name = name;
        this.age = age;
    }
}

// To create a new instance of ConstructorsAre and call the constructor,
// use the following syntax: new ConstructorsAre("exampleName");

// Note: The constructor doesn't necessarily need to be public;
// its visibility depends on the use case.

// The Person class demonstrates the application of the ConstructorsAre class.
class Person {

    // The createConstructor method creates an instance of ConstructorsAre,
    // setting the 'name' attribute to "Mary" by calling the constructor.
    void createConstructor() {
        ConstructorsAre myConstructorsAre = new ConstructorsAre("Mary", 99);
    }
}
