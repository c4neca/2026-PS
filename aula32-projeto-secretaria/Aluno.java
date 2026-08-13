/*
 * Disciplina : 2026-PS
 * Estudante  : Ana Vitória Schactae Brandão
 * Data       :      2026.08.13
 * Projeto    :   aula32-projeto-secretaria
 * Arquivo    : Aluno.java 
*/

public class Aluno {
    private String nome;
    private String matricula;
    private String curso;

    public Aluno(String nome, String matricula, String curso) {
        // "this" diferencia variáveis locais de atributos com o mesmo nome
        this.nome = nome;
        this.matricula = matricula;
        this.curso = curso;
    }
    // getters: obtém o valor de um atributo privado;  
    public String getNome() {
        return nome;
    }

    public String getMatricula() {
        return matricula;
    }

    public String getCurso(){
        return curso;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public void setCurso(String curso) {
        this.curso = curso;
    }
}
