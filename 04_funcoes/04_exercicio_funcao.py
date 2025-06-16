"""Exercício 04.

Classificação de Número
Desenvolva um programa com uma função que receba um número como argumento e retorne
"Positivo" se o número for positivo, "Negativo" se for negativo ou "Zero" se for
zero.
"""
def classificar_numero(num):
    if num > 0:
        return f"{num} é positivo."
    elif num == 0: 
        return f"Número é zero."
    return f"{num} é negativo."

print(classificar_numero(15))