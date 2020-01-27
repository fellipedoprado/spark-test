# Desafio Spark

## Objetivo
Aplicação Spark criada para análise de logs HTTP da NASA. Ela responderá as seguintes perguntas:
1. Número de hosts únicos.
2. O total de erros 404.
3. Os 5 URLs que mais causaram erro 404.
4. Quantidade de erros 404 por dia.
5. O total de bytes retornados.

## Executando a aplicação
Para rodar a aplicação, você deve:
* Ter instalado Java SDK, Apache Spark e Hadoop instaldos. Caso você não tenha, você pode começar [clicando aqui](https://github.com/Cheng-Lin-Li/Spark/wiki/How-to-install-Spark-2.1.0-in-Windows-10-environment) e seguir as instruções.
* Criar a pasta `data\` na raiz desse projeto e colocar os arquivos de log dentro dessa pasta

Então para rodar a aplicação basta abrir o CMD, acessar o diretorio `\spark-test-semantix\` desse projeto e rodar o seguinte comando:
`spark-submit main.py`.

Os resultados da aplicação serão exibidos no CMD.