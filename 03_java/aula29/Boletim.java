import java.util.Scanner;
import java.util.ArrayList;

public class Boletim{
    static double calcularMedia(double[] notas){
        double soma = 0;
        for (int i=0; i<notas.length; i++){
            soma += notas[i];
        }
        return soma/notas.length;
    }
    static int contarAprovados(double[] notas){
        int contador = 0;
        for (int i=0; i<notas.length; i++){
            if(notas[i] >= 6.0){
                contador += 1;
            }
        }
        return contador;
    }
    static void exibirBoletim(double[] notas) {
        double media=calcularMedia(notas);
        int aprovados = contarAprovados(notas);
        System.out.println("Média: " + media);
        System.out.println("Aprovados: " + aprovados);
        if (media >= 6.0){
        System.out.println("Situação: APROVADA");
        } else{
            System.out.println("Situação: EM RECUPERAÇAO");
        }
    }
    public static void main(String[] args){
        double[] turma1 = {7.0, 5.0, 9.0, 6.0};
        double[] turma2 = {4.0, 3.0, 5.0};
        exibirBoletim(turma1);
        System.out.println();
        exibirBoletim(turma2);
    }
}
