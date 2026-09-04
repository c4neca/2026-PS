Por que os atributos de Produto foram definidos como private?
Para respeitar o encapsulamento.O private impede que qualquer parte do sistema mude o nome ou o preço de qualquer jeito, assim as mudanças só acontecem do jeito que a classe autorizar, como os getters, os setters e o alterarPreco.
O que o método buscarPorCodigo() retorna quando encontra um produto?
Do jeito que o meu método foi escrito, ele não devolve nenhum valor, só mostra os dados do produto na tela e encerra com o return;.
O objeto retornado pela busca é uma cópia ou uma referência ao objeto armazenado no ArrayList?
Referência. No Java, quando a gente mexe em um objeto, estamos apontando direto para o lugar onde ele está salvo na memória. Qualquer alteração feita nele vai mudar o produto de verdade dentro do ArrayList.
Por que é melhor possuir um único método de busca?
Para economizar código e reutilizar código.
O que é sobrecarga de métodos?
É quando você cria dois ou mais métodos com o mesmo nome na mesma classe, mas com entradas ou parâmetros diferentes.