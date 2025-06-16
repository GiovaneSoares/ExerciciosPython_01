"""Exercício 09.

Reverso de um Número
Crie uma função que retorne o reverso de um número inteiro informado.
Por exemplo, se a função receber o número 127, ela deve retornar 721.
A função deve aceitar um inteiro e retornar um inteiro.
"""
def reverso(numero):
    return int(str(numero)[::-1])

num = int(input("Digite um numero e veja o reverso: "))
print(f"Reverso do número: {reverso(num)}")