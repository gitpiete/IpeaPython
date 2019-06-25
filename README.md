# Python4ABM exercícios e projeto final

Os arquivos exX_fn.py (1a lista) são independentes.

Os arquivos tarefa2X.py (2a lista) são dependentes, e têm que estar na mesma pasta. 
Executa tarefa2c.py para rodar o modelo. 

## Projeto final:

Modelo ABM para transporte aéreo estadual brasileiro.

Estado atual: Viagens aéreas DF-SP sem atualização do preços pela demanda. 
A Gol sempre esgota sua capacidade, vendendo as passagens mais baratas

Vários itens do modelo foram reprogramados, portanto há muito código comentado para futuras expansões. 
Para o modelo rodar mais rápido, o número de passageiros reais foi dividido por mil, 
tendo que multiplicar os resultados por mil.
###Execução:
Executar arquivo "project2.py". (python project2.py)
 
O arquivo "project1.py" tem que estar na mesma pasta. 

A execução cria informação na tela e num arquivo "flights_yyyy-mm-dd_hhmmss.txt"  