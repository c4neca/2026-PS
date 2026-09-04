import java.util.ArrayList;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner teclado = new Scanner(System.in);
        ArrayList<Produto> produtos = new ArrayList<>();

        while (true) {
            System.out.println("\n=== SISTEMA DE PRODUTOS ===");
            System.out.println("1 - Cadastrar");
            System.out.println("2 - Listar");
            System.out.println("3 - Buscar pelo Código");
            System.out.println("4 - Alterar preço");
            System.out.println("5 - Remover Produto");
            System.out.println("6 - Sair");
            System.out.print("Opção: ");
            String opcao = teclado.nextLine();

            if (opcao.equals("6")) {
                System.out.println("Fechando o sistema...");
                break;
            } else if(opcao.equals("1")) {
                cadastrar(produtos, teclado);
            } else if (opcao.equals("2")) {
                listar(produtos);
            } else if (opcao.equals("3")) {
                buscarPorCodigo(produtos, teclado);
            } else if (opcao.equals("4")) {
                alterar(produtos, teclado); 
            } else if (opcao.equals("5")) {
                remover(produtos, teclado);
            } else {
                System.out.println("\nSelecione apenas 1, 2, 3, 4, 5 ou 6!");
            }
        }
    }
    

    static void cadastrar(ArrayList<Produto> produtos, Scanner teclado) {
        System.out.print("Código   : ");
        int codigo = teclado.nextInt();
        teclado.nextLine();

        System.out.print("Nome     : ");
        String nome = teclado.nextLine();

        System.out.print("Preço    : ");
        double preco = teclado.nextDouble();
        teclado.nextLine();
        Produto p = new Produto(codigo, nome, preco);
        produtos.add(p);
        System.out.println("\nProduto cadastrado!");
    }

    static void listar(ArrayList<Produto> produtos) {
        for (Produto p : produtos) {
            System.out.println(p); 
        }
    }

    static void buscarPorCodigo(ArrayList<Produto> produtos, Scanner teclado) {
        System.out.print("Digite o código: ");
        int codigo = teclado.nextInt(); 
        teclado.nextLine();
        for (Produto p  : produtos){
            if (p.getCodigo() == codigo){
                System.out.println(p);  
                return;  
            }
        }
        System.out.println("Nenhum produto com o código " + codigo + ".");
    }
    
    static void alterar(ArrayList<Produto> produtos, Scanner teclado) {
        System.out.print("Código do produto a atualizar: ");
        int codigo = teclado.nextInt();
        teclado.nextLine();
        
        for (Produto p : produtos) {
            if (p.getCodigo() == codigo) {
                System.out.print("Novo preço base: ");
                double preco = teclado.nextDouble();

                System.out.print("Porcentagem de desconto (%): ");
                double desconto = teclado.nextDouble();
                teclado.nextLine();

                p.alterarPreco(preco, desconto);
                System.out.println("\nPreço alterado!");
                return;
            }
        }
        System.out.println("Nenhum produto com o código " + codigo + ".");

    }
        
    static void remover(ArrayList<Produto> produtos, Scanner teclado) {
        System.out.print("Código do produto que deseja remover: ");
        int codigo = teclado.nextInt();
        teclado.nextLine();
        for (Produto p : produtos) {
            if (p.getCodigo() == codigo) {
                produtos.remove(p);
                System.out.println("\nProduto removido!");
                return;
            }
        }
        System.out.println("Nenhum produto com o código " + codigo + ".");

    }
}

