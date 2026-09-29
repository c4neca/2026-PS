/*
* Disciplina: 2026-PS
* Projeto: bibliotech
* Arquivo: Leitor.java
* Autor: Ana Vitória Schactae Brandão
* Descricao : aLeitor E UM TIPO DE Usuario: herda nome, matricula e entrar().
*/
public class Bibliotecario extends Usuario {

    private String matriculaFuncional;

    public Bibliotecario(String nome, String matricula, String matriculaFuncional) {
        super(nome, matricula);
        this.matriculaFuncional = matriculaFuncional;
    }

    public String getMatriculaFuncional() {
        return matriculaFuncional;
    }

    public boolean consultarAcervo() {
        return true;
    }

    public String toString() {
        return "Bibliotecario(a) " + getNome() + " (" + getMatricula() + ", funcional " + matriculaFuncional + ")"; 
    }
}