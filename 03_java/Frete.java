import java.util.Scanner;
    public class Frete {
        static double calcularFrete(double peso){
            if (peso <= 1){
                return(10.0);
            } else if (peso <= 5){
                return(20.0);
            } else{
                return(35.0);
            }
        }
        public static void main(String[] args){
            Scanner entrada = new Scanner(System.in);
            System.out.print("Digite o peso: ");
            double peso = entrada.nextDouble();
            double frete = calcularFrete(peso);
            System.out.println("O valor do frete é: " + frete);
        }
    } 