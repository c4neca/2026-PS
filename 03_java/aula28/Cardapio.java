import java.util.Scanner;
public class Cardapio {
    static void exibirProduto(String nome) {
        System.out.println("Produto: " + nome);
    }
    static void exibirProduto(String nome, double preco) {
        System.out.println("Produto: " + nome + " e Preço: " + preco);
    }
    public static void main(String[] args) {
        exibirProduto("Banana");
        exibirProduto("Maçã", 3.5);
    }
}