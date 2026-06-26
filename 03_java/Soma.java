import java.util.Scanner;

public class Soma {
    
    static int somar(int a, int b) {
        return a + b;
    }
    
    static double somar(double a, double b) {
        return a + b;
    }

    public static void main(String[] args) {
        System.out.println("Soma int: " + somar(5, 3));
        System.out.println("Soma double: " + somar(2.5, 3.5));
    }
}