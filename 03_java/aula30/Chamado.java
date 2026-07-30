public class Chamado {
    private String idChamado;
    private String titulo;
    private String descricao;
    private int prioridade;
    private String status;
    private int diasAberto;

    public Chamado(String idChamado, String titulo, String descricao, int prioridade) {
        if (idChamado == null || idChamado.trim().equals("") || 
            titulo == null || titulo.trim().equals("") || 
            descricao == null || descricao.trim().equals("")) {
            throw new IllegalArgumentException("Campos de texto nao podem ficar vazios!");
        }

        if (prioridade < 1 || prioridade > 5) {
            throw new IllegalArgumentException("A prioridade deve ser entre 1 e 5.");
        }

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

    public String getIdChamado() { return idChamado; }
    public String getTitulo() { return titulo; }
    public String getDescricao() { return descricao; }
    public int getPrioridade() { return prioridade; }
    public String getStatus() { return status; }
    public int getDiasAberto() { return diasAberto; }

    public boolean setTitulo(String novoTitulo) {
        if (novoTitulo != null && !novoTitulo.trim().equals("")) {
            this.titulo = novoTitulo;
            return true;
        }
        return false; 
    }

    public boolean alterarPrioridade(int novaPrioridade) {
        if (this.status.equals("FECHADO")) {
            return false;
        }

        if (novaPrioridade >= 1 && novaPrioridade <= 5) {
            this.prioridade = novaPrioridade;
            return true;
        }
        return false;
    }

    public boolean avancarStatus() {
        if (this.status.equals("ABERTO")) {
            this.status = "EM_ANDAMENTO";
            return true;
        } else if (this.status.equals("EM_ANDAMENTO")) {
            this.status = "FECHADO";
            return true;
        }
        return false; 
    }

    public boolean incrementarDias(int dias) {
        if (this.status.equals("FECHADO") || dias <= 0) {
            return false;
        }
        this.diasAberto = this.diasAberto + dias;
        return true;
    }
    public String getResumo() {
        return "ID: " + idChamado + " | Titulo: " + titulo + " | Status: " + status + 
               " | Prioridade: " + prioridade + " | Dias aberto: " + diasAberto;
    }
}