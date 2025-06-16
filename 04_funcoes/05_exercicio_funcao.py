"""Exercício 05.

Cálculo de Imposto sobre Produto
Crie um programa com uma função chamada "soma_imposto".
A função deve receber dois parâmetros: "taxa_imposto" (percentual de imposto sobre
vendas) e "custo" (custo de um item antes do imposto).
A função deve retornar o custo após adicionar o imposto sobre vendas.
"""
def soma_imposto(taxa_imposto, custo):
    return custo *(1 + taxa_imposto / 100)

custo = float(input("Digite o valor do produto: "))
taxa_imposto = float(input("Qual a taxa de imposto? "))

novo_custo = soma_imposto(taxa_imposto, custo)

print(f"Custo com taxa de imposto: {novo_custo:.2f}")