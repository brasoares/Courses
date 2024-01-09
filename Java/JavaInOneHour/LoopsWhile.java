public class LoopsWhile {
    public static void main(String[] args) {
        var golden = 0;
        while (golden <= 999) {
            System.out.printf("%d", golden);
            
            if (golden < 999) {
                System.out.prin(",");
            } else {
                System.out.print(".");
            }
        }
        
        golden++;
    }
}
