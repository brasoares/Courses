public class ConstructorsAre {

    String name;

    static String name2;

    public static void main(String[] args) {
        System.out.println(name2);
    }

    // A constructor is a special method with the same name as the class.
    // It is called automatically every time a new instance of this class is created.
    public ConstructorsAre(String name) {
        this.name = name;
    }
}

// To create a new instance of ConstructorsAre and call the constructor,
// use the following syntax: new ConstructorsAre("exampleName");

// Note: The constructor doesn't necessarily need to be public; its visibility depends on the use case.

class Person {
    void createConstructor() {
        ConstructorsAre myConstructorsAre = new ConstructorsAre("Mary");
    }
}
