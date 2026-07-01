import java.util.Scanner;
public class Calc {
    static double calcularDesconto(double valor, double desconto){
    double valorFinal = valor - (valor * desconto / 100);
    return valorFinal;
    }
    public static void main (String[] args){
        Scanner entrada = new Scanner(System.in);
        System.out.print("Digite o valor: ");
        double valor = entrada.nextDouble();
        System.out.print("Digite o desconto: ");
        double desconto = entrada.nextDouble();
        double valFinal = calcularDesconto(valor, desconto);
        System.out.println("Valor final + desconto: " + valFinal);
    }
}