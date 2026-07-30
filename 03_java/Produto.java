public class Produto {
    private String nome;
    private double preco;
    private int quantidade;
}

public class Main {
    public static void main(String[] args) {
        Produto produto1 = new Produto();

        produto1.nome = "Teclado";
        produto1.preco = 120.00;
        produto1.quantidade = 8;

        System.out.println(produto1.nome);
        System.out.println(produto1.preco);
        System.out.println(produto1.quantidade);
    }
}