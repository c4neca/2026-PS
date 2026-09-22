# BiblioTech
​
Sistema de emprestimo de livros para a biblioteca do campus.
​
## 1. O projeto
​Os clientes são a Dona Marli, bibliotecária do campus e os alunos do campus. Os problemas são: a dificuldade da Dona Marli em controlar datas e processos da biblioteca de forma manual, e dos alunos, que precisam de deslocar até a biblioteca para se informar. O sistema resolve o problema tanto para os biliotecários - automatizando o empréstimo e devolução dos livros para que esse controle não precise ser feito por conta dos profissionais, além das datas, que são definidas no proprio sistema - quanto para os alunos, que podem realizar empréstimos e reservas de livros, consultar volumes disponíveis e acompanhar prazos de qualquer lugar.

## 2. Historias de usuario
​
| # | Historia de usuario |
|---|---|
| HU01 | Como leitor, quero consultar a disponibilidade de um livro, para saber se posso pega-lo emprestado sem ir ate o balcao. |
| HU02 | Como leitor, quero devolver um livro, para nao ficar com pendencia na biblioteca. |
| HU03 | Como bibliotecaria, quero registrar um emprestimo, para saber quem esta com cada exemplar. |
| HU04 | Como bibliotecaria, quero cadastrar um livro novo, para que ele possa ser encontrado no sistema. |
| HU05 | Como bibliotecaria, quero ver os emprestimos atrasados, para cobrar a devolucao. |
| HU06 | Como bibliotecaria, quero que uma multa seja aplicada pelos dias de atraso.
## 3. Requisitos
​
### Requisitos funcionais
​
| # | Requisito funcional | Veio da |
|---|---|---|
| RF01 | O sistema deve permitir que a bibliotecaria cadastre um livro no acervo. | HU04 |
| RF02 | O sistema deve permitir que a bibliotecaria cadastre um leitor. | regra de acesso: so quem tem cadastro leva livro |
| RF03 | O sistema deve permitir que o leitor consulte a disponibilidade de um livro. | HU01 |
| RF04 | O sistema deve permitir que a bibliotecaria registre a devolucao de um livro. | HU02 |
| RF05 | O sistema deve permitir que a bibliotecaria registre o emprestimo de um livro. | HU03 |
| RF06 | O sistema deve calcular a multa pelos dias de atraso | HU6 |
​
### Requisitos nao funcionais
​
| # | Requisito nao funcional |
|---|---|
| RNF01 | A consulta de disponibilidade deve responder em menos de 3 segundos. |
| RNF02 | Somente usuarios identificados como bibliotecarios podem alterar o acervo. |

## 4. Diagramas (feitos em APS)
​
### Casos de uso
​
![Diagrama de casos de uso do BiblioTech](docs/casos-de-uso.svg)
​
### Classes
​
![Diagrama de classes do BiblioTech](docs/classes.svg)