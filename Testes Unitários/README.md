# Testes Unitários
    * Biblioteca usada: PyTest


## O que significa testar ?
Testar é um processo de avaliação de um sistema ou software , para garantir que ele chegue nos requisitos necessários

## Porquê Testar ?

## PyTest Anotações

* No PyTest todos os arquivos de teste devem seguir o prefixo de _test , para que o pytest interprete o tal como um arquivo de teste
Então o arquivo de teste de exemplo caso você tivesse um arquivo chamado run.py , o arquivo de teste seria chamado de run_test.py

* Nas funções de teste dentro do arquivo de teste o prefixo se mantêm , ou seja toda vez que eu fizer uma função de teste ela tem que ta escrita da seguinte
maneira test_add_two() , sempre o test_ antes do nome de qlqr função que tá

### Comandos de execução
* Para usar o pytest , basta ir no terminal na pasta do projeto e digitar pytest que ele vai executar os arquivos e as funções , dando o retorno geral do teste
Para ver os testes de maneira mais detalhada basta digitar pytest so que com os paramentros -s e -v, ficando assim : pytest -s -v
