import java.util.Scanner;
import java.util.ArrayList;
import java.util.List;

public class Contador{
    static int contarAprovados(double[] notas){
        int contador = 0;
        for (int i=0; i<notas.length; i++){
            if(notas[i] >= 6.0){
                contador += 1;
            }
        }
        return contador;
    }
    public static void main (String[] args){
        Scanner entrada = new Scanner(System.in);
        double[] notas = new double[4];
        System.out.println("Digite as notas: ");
        for (int i=0; i<4; i++){
        notas[i] = entrada.nextDouble();
        }
        int aprovados = contarAprovados(notas);
        System.out.println("O número de aprovados é: " + aprovados);
    }
}