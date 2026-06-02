import java.util.Scanner;
public class CardapioRestaurante {
    public static void main (String[] args){
        Scanner entrada = new Scanner(System.in);

        System.out.println("=====================================");
        System.out.println("       RESTAURANTE HAPPY FOOD        ");
        System.out.println("=====================================");
        System.out.println("1 - X-Burguer -------- R$ 18,00");
        System.out.println("2 - Pizza ------------ R$ 35,00");
        System.out.println("3 - Suco Natural ----- R$ 8,00");
        System.out.println("4 - Café ------------- R$ 5,00");
        System.out.println("5 - Sorvete ---------- R$ 10,00");
        System.out.print("Escolha uma opção: ");
        
        int opcao = 0;
        int quantidade = 0;
        int valor_total = 0;

            System.out.print("Escolha uma opção: ");
             opcao = entrada.nextInt();
            System.out.print("Escolha uma quantidade: ");
             quantidade = entrada.nextInt();
        
        if (opcao == 1) {
            System.out.println("Você escolheu X-Burguer - R$ 18,00.");
            System.out.println("Valor: " + (18.00*quantidade));
            valor_total = valor_total +(quantidade*opcao);
        } else if (opcao == 2) {
            System.out.println("Você escolheu Pizza - R$ 35,00.");
            System.out.println("Valor: " + (35.00*quantidade));
            valor_total = valor_total +(quantidade*opcao);
        } else if (opcao == 3) {
            System.out.println("Você escolheu Suco Natural - R$ 8,00.");
            System.out.println("Valor: " + (8.00*quantidade));
        } else if (opcao == 4) {
            System.out.println("Você escolheu Café - R$ 5,00.");
            System.out.println("Valor: " + (5.00*quantidade));
            valor_total = valor_total +(quantidade*opcao);
        } else if (opcao == 5) {
            System.out.println("Você escolheu Sorvete - R$ 10,00.");
            System.out.println("Valor: " + (10.00*quantidade));
            valor_total = valor_total +(quantidade*opcao);
         } else {
            System.out.println("Opção inválida! Escolha um número de 1 a 5.");
        }
        System.out.println("Valor total: R$ " + valor_total);
        entrada.close();
    }
}
