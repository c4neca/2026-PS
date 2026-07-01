import java.util.Scanner;
import java.util.ArrayList;

public class Maior{
    static int maiorValor(int[] valores){
        int maior = valores[0];
        for(int i=0; i<valores.length; i++){
            if(maior<valores[i]){
                maior = valores[i];
            }
        }    
        return maior;    
    }
    static int maiorValor(int a, int b){
        if(a>b){
            return a;
        }else{
            return b;
        }
    }
    public static void main(String[] args){
        maiorValor(new int[]{3, 9, 5});
        System.out.println("O maior valor é: " + maiorValor(new int[]{3,9,5}));
        System.out.println("O maior valor é: " + maiorValor(12,7));
        System.out.println("O maior valor é: " + maiorValor(new int[]{4,4,4}));

    }
}