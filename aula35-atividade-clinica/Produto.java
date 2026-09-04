/*
 * Disciplina : 2026-PS
 * Estudante  : Ana Vitória Schactae Brandão
 * Data       :      2026.09.03
 * Projeto    :   aula35-atividade-clinica
 * Arquivo    : Produto.java 
*/

public class Produto {

    private int codigo;
    private String nome;
    private double preco;

    public Produto(int codigo, String nome, double preco) {
        this.codigo = codigo;
        this.nome = nome;
        this.preco = preco;
    }
    public String getNome() {
        return nome;
    }

    public int getCodigo() {
        return codigo;
    }
    
    public double getPreco() {
        return preco;
    }

    public void setAlterarPreco(double preco) {
        this.preco = preco;
    }
    
    public void alterarPreco(double preco, double desconto) {
        double valorDesconto = preco * (desconto / 100.0);
        double novoPreco = preco - valorDesconto;

        if (novoPreco < 0) {
            System.out.println("Erro: O preço final não pode ser negativo!");
        } else {
            this.preco = novoPreco;
            System.out.println("Preço atualizado com sucesso!");
        }
    }
    
    @Override
    public String toString() {
        return "Código: " + this.codigo + " | Nome: " + this.nome + " | Preço: R$ " + this.preco;
    }

}