public class Main {
    public static void main(String[] args) {
        System.out.println("=== TESTES DO SISTEMA DE CHAMADOS ===\n");

        System.out.println("1. Criando chamados validos:");
        Chamado c1 = new Chamado("JU-CH15", "JUstificativa de Acesso", "Erro no login", 3);
        Chamado c2 = new Chamado("JU-CH16", "JUntar Relatorios", "Servidor lento", 5);
        Chamado c3 = new Chamado("JU-CH17", "JUros Incorretos", "Verificar conta");

        System.out.println(c1.getResumo());
        System.out.println(c2.getResumo());
        System.out.println(c3.getResumo());
        System.out.println();

        System.out.println("2. Testando texto em branco:");
        boolean ok1 = c1.setTitulo("   ");
        if (ok1) {
            System.out.println("Alterou com sucesso!");
        } else {
            System.out.println("Alteracao recusada (texto invalido).");
        }
        System.out.println("Titulo atual: " + c1.getTitulo());
        System.out.println();

        System.out.println("3. Testando prioridade invalida (-15):");
        boolean ok2 = c1.alterarPrioridade(-15);
        if (ok2) {
            System.out.println("Alterou com sucesso!");
        } else {
            System.out.println("Alteracao recusada (prioridade fora do limite).");
        }
        System.out.println("Prioridade atual: " + c1.getPrioridade());
        System.out.println();

        System.out.println("4. Testando acao permitida (Avancar status e somar 15 dias):");
        c1.avancarStatus();
        c1.incrementarDias(15);
        System.out.println("Estado atualizado: " + c1.getResumo());
        System.out.println();

        System.out.println("5. Testando acao impossivel:");
        c2.avancarStatus();
        c2.avancarStatus();
        System.out.println("Status do chamado 2: " + c2.getStatus());

        boolean ok3 = c2.avancarStatus();
        if (ok3) {
            System.out.println("Avancou de status!");
        } else {
            System.out.println("Operacao nao permitida (chamado ja esta fechado).");
        }
        System.out.println();

        System.out.println("----------------------------------------");
        System.out.println("ESTADO FINAL DOS CHAMADOS:");
        System.out.println(c1.getResumo());
        System.out.println(c2.getResumo());
        System.out.println(c3.getResumo());
    }
}