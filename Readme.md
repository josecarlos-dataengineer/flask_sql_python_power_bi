# Análise de dados
Neste repositório continuamos os estudos de análise de dados, utilizando o mesmo conjunto de dados utilizado em !["estudo_analise_vendas_sql"](https://github.com/josecarlos-dataengineer/estudo_analise_vendas_sql).

Mas aqui faremos algumas mudanças, com a finalidade de avançar na utilização de técnicas.

Aqui teremos um banco de dados SQLSERVER servindo uma API com os dados, e utilizaremos Python para coletar, tratar e salvar os dados da API em formato CSV.

Neste estudo são utilizados conceitos de modelagem de dados para Datalake e modelagem Star Schema.

## Ambiente
O primeiro passo para iniciar o ambiente é criar um ambiente virtual. Você pode utilizar o método que estiver mais familiarizado para isso.

Caso não esteja familiarizado com nenhum, você pode executar:

```
python -m venv estudo_api
```

Esse comando irá criar um ambiente virtual para que as bibliotecas sejam instaladas.

Após ativar o ambiente virtual, execute.

```
pip install -r requirements.txt
```

Este comando instalará os pacotes e suas versões contidos no arquivo requirements.txt.

```
Flask==2.0.3
SQLAlchemy==1.4.25
pyodbc==4.0.32
Werkzeug==2.0.3
PyMySQL==1.0.2
requests
pandas==2.2.2
```


## Power BI
![alt text](power_bi/imagens/analise.png)

