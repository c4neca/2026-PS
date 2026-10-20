public class TesteLivroDAO {

    public static void main(String[] args) {

        LivroDAO dao = new LivroDAO();

        boolean livro1 = dao.adicionarLivro(
            "Dom Casmurro",
            "Machado de Assis",
            1899
        );

        boolean livro2 = dao.adicionarLivro(
            "A Hora da Estrela", 
            "Clarice Lispector", 
            1977
            );

        boolean livro3 = dao.adicionarLivro(
            "A Guerra da Papoula", 
            "R. F. Kuang", 
            2018);

        System.out.println(
            "Livro 1 adicionado: " + livro1
        );

        System.out.println(
            "Livro 2 adicionado: " + livro2
        );

        System.out.println(
            "Livro 3 adicionado: " + livro3
        );

    }
}