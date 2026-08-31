/*
 * Disciplina: 2026-PS
 * Estudante : Ana Vitória Schactae Brandão
 * Data      : 2026.08.11
 * Projeto   : aula32-projeto-secretaria
 * Arquivo   : Main.java 
 */

import java.util.ArrayList;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner teclado = new Scanner(System.in);

        ArrayList<Aluno> lista = new ArrayList<Aluno>();

        while(true) { // Enquanto o aluno não sai do sistema, as mensagens a seguir são impressas
            System.out.println("===========================================");
            System.out.println("SECRETARIA DO CAMPUS - por ANA VITÓRIA SCHACTAE BRANDÃO");
            System.out.println("===========================================");
            System.out.println("[1] Cadastrar aluno");
            System.out.println("[2] Listar alunos");
            System.out.println("[3] Buscar por matrícula");
            System.out.println("[4] Atualizar curso");
            System.out.println("[5] Remover aluno");
            System.out.println("[6] Relatorio");
            System.out.println("[7] Buscar por nome");
            System.out.println("[0] Sair");
            System.out.println("Sua escolha: ");
            String opcao = teclado.nextLine().trim(); // Pega a opção do teclado e formata

            if (opcao.equals("0")) { // Se a opção selecionada for 0, o sistema vai ser encerrado.
                System.out.println("Encerrando o expediente porque não é só a patroa que precisa descansar né miga. Não se preocupa que eu volto antes do frank ocean tá!");
                break;
            } else if (opcao.equals("1")) { // Se a opção selecionada for 1, o sistema vai chamar a função cadastrar, utilizando os parâmetros lista (onde vai ser armazenado o aluno) e a entrada do teclado.
                cadastrar(lista, teclado);
            } else if (opcao.equals("2")) { // Se a opção selecionada for 2, o sistema vai listar todos os alunos a partir do parâmetro lista (onde eles estão armazenados).
                listar(lista);
            } else if (opcao.equals("3")) { 
                buscar1(lista, teclado);
            } else if (opcao.equals("4")) {
                atualizar(lista, teclado);
            } else if (opcao.equals("5")) {
                remover(lista, teclado);
            } else if (opcao.equals("6")) {
                relatorio(lista, teclado);
            } else if (opcao.equals("7")) { 
                buscar2(lista, teclado);
            } else { // O else aparece quando o usuário entra qualquer outro dígito além das opções mostradas
                System.out.println("Opcao invalida! Escolha 0, 1, 2, 3, 4, 5, 6 ou 7."); // Fazendo com que o sistema retorne essa mensagem de solicitação.
            }
        }
    }

    static void cadastrar(ArrayList<Aluno> lista, Scanner teclado) { // A função cadastrar utiliza dois parâmetros, a lista de alunos (que armazena os alunos cadastrados), e a entrada do teclado (Scanner)
        System.out.print("Nome           : ");
        String nome = teclado.nextLine().trim();
        System.out.print("Matrícula      : ");
        String matricula = teclado.nextLine().trim();
        Aluno existente = buscarPorMatricula(lista, matricula);
        if (existente != null) {
            System.out.println("Já existe ficha com a matrícula " + matricula + "!");
            return;
        }
        System.out.print("Curso          : ");
        String curso = teclado.nextLine().trim();
        System.out.print("Música Favorita: ");
        String musicaFav = teclado.nextLine().trim();
        Aluno novoAluno = new Aluno(nome, matricula, curso, musicaFav); // Permite armazenar os novos objetos dentro de novoAluno
        lista.add(novoAluno); // adiciona o novo objeto a lista
        System.out.println("Serviu cunt purinho! A ficha de " + novoAluno.getNome() + " foi arquivada, diva!!");
    }

    static void listar(ArrayList<Aluno> lista) {
        if (lista.size() == 0) { // Se a lista não tiver armazenado nenhum objeto imprime a mensagem:
            System.out.println("O gaveteiro flopou total. Sem ícones pra servir aqui no momento.");
            return;
        } else {
            System.out.println("--- FICHAS NO GAVETEIRO: " + lista.size() + " ---"); 
            for (int i = 0; i<lista.size(); i++){
                Aluno a = lista.get(i);
                System.out.println(a);
            }
        }
    }

    static Aluno buscarPorMatricula(ArrayList<Aluno> lista, String matricula) {
        for (int i = 0; i<lista.size(); i++){
            Aluno a = lista.get(i); 
            if (a.getMatricula().equals(matricula)){ // O equals nesse caso é utilizado porque estamos comparando textos (por isso não usamos os "==", porque eles comparam apenas valores).
                return a; 
            }
        }
        return null; // o null vai ser usado quando a matrícula não for encontrada
    }

    static void buscar1(ArrayList<Aluno> lista, Scanner teclado) {
        System.out.print("Matrícula procurada: ");
        String matricula = teclado.nextLine().trim();
        Aluno a = buscarPorMatricula(lista, matricula);
        if (a == null) {
            System.out.println("Nenhuma ficha com a matricula " + matricula + ".");
        } else {
            System.out.println("Achei: " + a);
        }
    }

    static Aluno buscarPorNome(ArrayList<Aluno> lista, String nome) {
        for (int i = 0; i<lista.size(); i++){
            Aluno a = lista.get(i); 
            if (a.getNome().equals(nome)){ // O equals nesse caso é utilizado porque estamos comparando textos (por isso não usamos os "==", porque eles comparam apenas valores).
                return a; 
            }
        }
        return null; // o null vai ser usado quando o nome não for encontrado
    }

    static void buscar2(ArrayList<Aluno> lista, Scanner teclado) {
        System.out.print("Nome procurado: ");
        String nome = teclado.nextLine().trim();
        Aluno a = buscarPorNome(lista, nome);
        if (a == null) {
            System.out.println("Nenhuma ficha com o nome " + nome + ".");
        } else {
            System.out.println("Achei: " + a);
        }
    }
    
    static void atualizar(ArrayList<Aluno> lista, Scanner teclado) {
        System.out.print("Matrícula da ficha a atualizar: ");
        String matricula = teclado.nextLine().trim();
        Aluno a = buscarPorMatricula(lista, matricula);
        if (a == null) {
            System.out.println("Nenhuma ficha com a matrícula " + matricula + ".");
            return;
        }
        System.out.print("Novo curso de " + a.getNome() + ": ");
        String novoCurso = teclado.nextLine().trim();

        a.setCurso(novoCurso);
        System.out.println("Ficha atualizada: " + a);
    }

    static void remover(ArrayList<Aluno> lista, Scanner teclado) {
        System.out.print("Matrícula da ficha a remover: ");
        String matricula = teclado.nextLine().trim();
        Aluno a = buscarPorMatricula(lista, matricula);
        if (a == null) {
            System.out.println("Nenhuma ficha com a matricula " + matricula + ".");
            return;
        }
        System.out.print("Tem certeza que quer remover " + a.getNome() + "? (s/n): ");
        String resposta = teclado.nextLine().trim();
        if (resposta.equals("s")) {
            lista.remove(a); 
            System.out.println("Ficha removida.");
        } else {
            System.out.println("Remoção cancelada.");
        }
    }
    static void relatorio(ArrayList<Aluno> lista, Scanner teclado) {
        System.out.println("--- RELATORIO DA SECRETARIA ---");
        System.out.println("Total de fichas: " + lista.size());
        System.out.print("Contar alunos de qual curso? ");
        String curso = teclado.nextLine().trim();

        int contador = 0;                                           // preparar (ANTES do for)
        for (int i = 0; i < lista.size(); i ++) {                    // percorrer
            Aluno a = lista.get(i);
            if (a.getCurso().equals(curso)) {
                contador = contador + 1;
            }
        }
        System.out.println("Alunos de " + curso + ": " + contador); // usar
    }
}