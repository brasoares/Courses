/**Henoc S. Freire | 4/20/2024 at Carapicuíba | V 0.0 | stars.java */

public class BrightestStars {

  // Ideally, properties should have access modifiers (private here)
  private String name;
  private double radiusSolarRadii; // Radius in solar radii (for reference)
  private double apparentMag; // Perceived brightness  

  // Constructor to initialize the properties
  public BrightestStars(String name, double radiusSolarRadii, double apparentMag) {
    this.name = name;
    this.radiusSolarRadii = radiusSolarRadii;
    this.apparentMag = apparentMag;
  }

  // Getter methods for accessing properties
  public String getName() {
    return name;
  }

  public double getRadiusSolarRadii() {
    return radiusSolarRadii;
  }

  public double getApparentMag() {
    return apparentMag;
  }

  public static void main(String[] args) {
    // Create BrightestStar objects with static data
    BrightestStars sirius = new BrightestStars("Sirius", 1.18, -1.46);
    BrightestStars canopus = new BrightestStars("Canopus", 310, -0.74);
    BrightestStars alphaCentauri = new BrightestStars("Alpha Centauri", 4.3, -0.01);
    BrightestStars arcturus = new BrightestStars("Arcturus", 36, -0.05);
    BrightestStars vega = new BrightestStars("Vega", 25, 0.03);
    BrightestStars capella = new BrightestStars("Capella", 42, 0.08);

    // Menu-driven system
    Scanner scanner = new Scanner(System.in);
    int choice;
    do {
      System.out.println("\nMenu:");
      System.out.println("1. Compare two specific stars");
      System.out.println("2. Compare randomly selected stars");
      System.out.println("3. Exit");
      System.out.print("Enter your choice: ");
      choice = scanner.nextInt();

      switch (choice) {
      case 1:
        compareSpecificStars(scanner, sirius, canopus, alphaCentauri, arcturus, vega, capella);
        break;
      case 2:
        compareRandomStars(sirius, canopus, alphaCentauri, arcturus, vega, capella);
        break;
      case 3:
        System.out.println("Exiting program. Goodybye!");
        break;
      default:
        System.out.println("Invalid choice. Please enter a valid option next time.");

      }
      while (choice != 3);
    }
  }
}
