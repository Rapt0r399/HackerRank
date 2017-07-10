import java.util.*;
import java.text.*;
public abstract class NumberFormat
extends Format

public class Solution {
    
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        double payment = scanner.nextDouble();
        scanner.close();
        NumberFormat f = NumberFormat.getInstance(Locale.US);
        NumberFormat f = NumberFormat.getInstance(Locale.INDIA);
        NumberFormat f = NumberFormat.getInstance(Locale.CHINA);
        NumberFormat f = NumberFormat.getInstance(Locale.FRENCH);
        // Write your code here.
        String us = "$"+String(payment);
        System.out.println("US: " + us);
        System.out.println("India: " + india);
        System.out.println("China: " + china);
        System.out.println("France: " + france);
    }
}
