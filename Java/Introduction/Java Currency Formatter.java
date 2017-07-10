import java.util.*;
import java.text.*;

public class Solution {
    
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        double payment = scanner.nextDouble();
        scanner.close();
        NumberFormat us = NumberFormat.getInstance(Locale.US);
        NumberFormat india = NumberFormat.getInstance(Locale.INDIA);
        NumberFormat china = NumberFormat.getInstance(Locale.CHINA);
        NumberFormat france = NumberFormat.getInstance(Locale.FRENCH);
        // Write your code here.
        String us1 = "$"+us.parse(String.format(payment));
        String india1 = "$"+india.parse(String.format(payment));
        String china1 = "$"+china.parse(String.format(payment));
        String france1 = "$"+france.parse(String.format(payment));
        System.out.println("US: " + us1);
        System.out.println("India: " + india1);
        System.out.println("China: " + china1);
        System.out.println("France: " + france1);
    }
}
