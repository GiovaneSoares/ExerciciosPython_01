"""Exercício 07.

Comparação de Preços
Desenvolva um programa que pergunte o preço de três produtos e informe ao usuário qual
produto deve ser comprado, optando sempre pelo mais econômico.
"""
lista = []

produto1 = float(input("Digite um valor do primeiro produto: "))
produto2 = float(input("Digite um valor do primeiro produto: "))
produto3 = float(input("Digite um valor do primeiro produto: "))
lista.extend([produto1, produto2, produto3])

def menor_numero(numero):
    return min(numero)

print(f"Com base em minha pesquisa, o item mais economico de sua lista é: R$",menor_numero(lista))