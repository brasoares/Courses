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

  public static void main(String[] args){
    // Create BrightestStar objects with static data
    BrightestStars sirius = new BrightestStars("Sirius", 1.18, -1.46);
  }
}
