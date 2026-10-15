import java.time.LocalDate;

public class Emprestimo {
    private Livro livro;
    private Leitor leitor;
    private LocalDate dataRetirada;
    private LocalDate dataDevolucao;
    private LocalDate dataPrevista;
    private boolean ativo;

    public Emprestimo(Livro livro, Leitor leitor) {
        if (livro == null || leitor == null) {
            throw new IllegalArgumentException(
                "Livro e leitor sao obrigatorios."
            );
        }

        this.livro = livro;
        this.leitor = leitor;
        this.ativo = false;
    }

    public boolean realizarEmprestimo() {
        if (ativo || !livro.estaDisponivel()
                  || !leitor.podePegarEmprestado()) {
            return false;
        }

        livro.emprestar();
        leitor.pegouLivro();
        dataRetirada = LocalDate.now();
        dataDevolucao = null;
        dataPrevista = dataRetirada.plusDays(7);
        ativo = true;
        return true;
    }

    public boolean registrarDevolucao() {
        if (!ativo) {
            return false;
        }

        livro.devolver();
        leitor.devolveuLivro();
        dataDevolucao = LocalDate.now();
        ativo = false;
        return true;
    }
    
    public Livro getLivro() {
        return livro;
    }

    public Leitor getLeitor() {
        return leitor;
    }

    public LocalDate getDataRetirada() {
        return dataRetirada;
    }

    public LocalDate getDataDevolucao() {
        return dataDevolucao;
    }

    public LocalDate getDataPrevista() {
        return dataPrevista;
    }

    public boolean estaAtivo() {
        return ativo;
    }

    @Override
    public String toString() {
        if (dataRetirada == null) {
            return "Emprestimo ainda nao realizado: "
                 + livro.getTitulo();
        }

        String situacao = ativo
            ? "ativo (devolução prevista para: " + dataPrevista + ")"
            : "devolvido em " + dataDevolucao;

        return livro.getTitulo() + " para "
             + leitor.getNome()
             + " | retirada: " + dataRetirada
             + " | " + situacao;
    }
}