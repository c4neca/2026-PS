public class Chamado {
    private String idChamado;
    private String titulo;
    private String descricao;
    private int prioridade;
    private String status;
    private int diasAberto;

    public Chamado(String idChamado, String titulo, String descricao, int prioridade) {
        this.idChamado = idChamado;
        this.titulo = titulo;
        this.descricao = descricao;
        this.prioridade = prioridade;
        this.status = "ABERTO";
        this.diasAberto = 0;
    }

    public Chamado(String idChamado, String titulo, String descricao) {
        this(idChamado, titulo, descricao, 1);
    }
}