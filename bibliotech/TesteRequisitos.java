public class TesteRequisitos {

    private static int passaram = 0;
    private static int falharam = 0;

    private static void verificar(String requisito, boolean condicao) {
        if (condicao) {
            passaram = passaram + 1;
            System.out.println("OK      " + requisito);
        } else {
            falharam = falharam + 1;
            System.out.println("FALHOU " + requisito);
        }
    }
    public static void main(String[] args) {
        Biblioteca biblioteca = new Biblioteca();
        biblioteca.cadastrarLivro(new Livro("Dom Casmurro", "Machado de Assis", 1899));
        biblioteca.cadastrarLivro(new Livro("Capitaes da Areia", "Jorge Amado", 1937));
        biblioteca.cadastrarLeitor(new Leitor("Pedro Alves", "2026010", 1));
        biblioteca.cadastrarLeitor(new Leitor("Ana Lima", "2026011", 2));

        Livro dom = biblioteca.buscarLivro("Dom Casmurro");
        Leitor pedro = biblioteca.buscarLeitor("2026010");

        verificar("RF01 livro cadastrado aparece na busca", dom != null);
        verificar("RF02 leitor cadastrado aparece na busca", pedro != null);

        verificar("RF03 livro novo está disponível", dom.estaDisponivel());
        verificar("RF03 titulo fora do acervo nao e encontrado", biblioteca.buscarLivro("O Cortico") == null);

        System.out.println();

        verificar("RF05 emprestimo de livro disponivel e aceito", biblioteca.emprestar("Dom Casmurro", "2026010"));
        verificar("RF05 livro emprestado fica indisponivel", !dom.estaDisponivel());
        verificar("RF05 leitor passa a ter 1 livro", pedro.getLivrosEmMaos() == 1);

        System.out.println();
        System.out.println("--- Teste das 5 Recusas do Arco");

        verificar("Recusa 1: Livro que não existe", !biblioteca.emprestar("O Cortico", "2026011" ));
        
        verificar("Recusa 2: Leitor inexistente", !biblioteca.emprestar("Capitaes da Areia", "999999"));
        
        verificar("Recusa 3: Livro já emprestado para outro", !biblioteca.emprestar("Dom Casmurro", "2026011"));
        
        verificar("Recusa 4: Leitor acima do limite", !biblioteca.emprestar("Capitaes da Areia", "2026010"));
        
        verificar("RF04 devolucao de emprestimo aceita", biblioteca.devolver("Dom Casmurro"));
        verificar("RF04 livro devolvido volta a ficar disponivel", dom.estaDisponivel());
        
        verificar("Recusa 5: livro devolvido recusado na segunda devolução", !biblioteca.devolver("Dom Casmurro"));

        System.out.println();
        System.out.println(passaram + " passaram, " + falharam + " falharam.");

    }
}
