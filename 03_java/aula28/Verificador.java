import java.util.Scanner;

public class Soma {
    
    // Método para inteiros
    static int somar(int a, int b) {
        return a + b;
    }
    
    // Método para decimais (double)
    static double somar(double a, double b) {
        return a + b;
    }

    public static void main(String[] args) {
        // Testando a sobrecarga
        System.out.println("Soma int: " + somar(5, 3));
        System.out.println("Soma double: " + somar(2.5, 3.5));
    }
}