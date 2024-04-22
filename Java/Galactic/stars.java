/**Henoc S. Freire | 4/20/2024 at Carapicuíba | V 0.0 | stars.java */

public class BrightestStar {

  // Ideally, properties should have access modifiers (private here)
  private String name;
  private double radiusSolarRadii; // Radius in solar radii (for reference)
  private double apparentMag; // Perceived brightness  

  // Constructor to initialize the properties
  public BrightestStar(String name, double radiusSolarRadii, double apparentMag) {
    this.name = name;
    this.radiusSolarRadii = radiusSolarRadii;
    this.apparentMag = apparentMag;
  }
  
}
