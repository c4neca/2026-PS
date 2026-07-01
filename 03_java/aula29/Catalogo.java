import java.util.Scanner;
import java.util.ArrayList;

public class Catalogo{
    static void adicionarProduto(ArrayList<String>produtos, String nome){
    produtos.add(nome);
    }
    static void listarProdutos(ArrayList<String>produtos){
        for(int i=0; i<produtos.size(); i++){
            System.out.println(i + 1 + "- " + produtos.get(i));
        }
    }
    public static void main(String[] args){
        Scanner entrada = new Scanner(System.in);
        ArrayList<String> produtos = new ArrayList<>();
        adicionarProduto(produtos, "Pizza");
        adicionarProduto(produtos, "Suco");
        listarProdutos(produtos);
    }
}
