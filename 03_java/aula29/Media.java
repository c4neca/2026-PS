import java.util.Scanner;
import java.util.ArrayList;
import java.util.List;
public class Media{
    static double calcularMedia(double[] notas) {
        double soma = 0;
        for (int i=0; i<notas.length; i++){
            soma += notas[i];
        }
        return soma/notas.length;
    }
    public static void main (String[] args){
        Scanner entrada = new Scanner(System.in);
        double[] notas = new double[3];
        System.out.println("Digite as notas: ");
        for (int i=0; i<3; i++){
        notas[i] = entrada.nextDouble();
        }
        double media = calcularMedia(notas);
        System.out.println("A média é: " + media);
    }
}