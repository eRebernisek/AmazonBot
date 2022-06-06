Para executar o script é necessário ter instalado o navegador Firefox e as seguintes bibliotecas Python:

xlsxwriter
selenium

O script foi desenvolvido e testado em ambiente Linux com Python3, também foi criada uma versão para rodar em windows embora não tenha sido possível realizar testes nela até o momento.

Quando o script for rodado ele deve passar pelas seguintes etapas:
1 - Abrir o navegador Firefox no site amazon.com
2 - Deixar o navegador em tela cheia para evitar mudar nome das classes no CSS
3 - Realizar pesquisa por "Iphone" e obter os nomes, preços e link dos produtos na primeira página
4 - Criar um arquivo xlsx chamado "Precos_Amazon" com as informações retornadas pela busca na pesquisa
5 - Após o arquivo ser gerado o browser ira fechar e a execução do script será encerrada

Obs: Produtos que estão sem preço na tela de busca são exibidos na planilha com valor zerado
