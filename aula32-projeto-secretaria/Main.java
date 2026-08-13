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

        while(true) {
            System.out.println("===========================================");
            System.out.println("SECRETARIA DA ANA VITÓRIA SCHACTAE BRANDÃO");
            System.out.println("===========================================");
            System.out.println("[1] Cadastrar aluno");
            System.out.println("[2] Listar alunos");
            System.out.println("[0] Sair");
            System.out.println("Sua escolha: ");
            String opcao = teclado.nextLine().trim();

            if (opcao.equals("0")) {
                System.out.println("Secretaria fechada. Até a próxima!");
                break;
            } else if (opcao.equals("1")) {
                cadastrar(lista, teclado);
            } else if (opcao.equals("2")) {
                listar(lista);
            } else {
                System.out.println("Opcao invalida! Escolha 0, 1 ou 2.");
            }
        }
    }

    static void cadastrar(ArrayList<Aluno> lista, Scanner teclado) {
        System.out.print("Nome     : ");
        String nome = teclado.nextLine().trim();
        System.out.print("Matrícula: ");
        String matricula = teclado.nextLine().trim();
        System.out.print("Curso    : ");
        String curso = teclado.nextLine().trim();
        Aluno novoAluno = new Aluno(nome, matricula, curso); // Permite armazenar os novos objetos dentro de novoAluno
        lista.add(novoAluno); // adiciona o novo objeto a lista
        System.out.println("Ficha de " + novoAluno.getNome() + " arquivada!");
    }

    static void listar(ArrayList<Aluno> lista) {
        if (lista.size() == 0) { // Se a lista não tiver armazenado nenhum objeto imprime a mensagem
            System.out.println("Nenhuma ficha...");
        } else {
            System.out.println("--- FICHAS NO GAVETEIRO: " + lista.size() + " ---"); 
            for (int i = 0; i<lista.size(); i++){
                System.out.println(lista.get(i).getMatricula() + " | " + lista.get(i).getNome() + " | " + lista.get(i).getCurso()); // Mostra as informações de todos os objetos da lista 
            }
        }
    }
}