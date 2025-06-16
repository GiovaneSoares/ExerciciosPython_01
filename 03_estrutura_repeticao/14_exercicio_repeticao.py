"""Exercício 14.

Contagem de Pares e Ímpares
Elabore um programa que solicite 10 números inteiros ao usuário e indique quantos são
pares e quantos são ímpares.
"""
numeros = [int(input(f"Informe o {i + 1}° numero: "))for i in range(10)]
cont_pares = [n for n in numeros if n % 2 == 0]
cont_impares = [n for n in numeros if n % 2 != 0]

print(f"Quantidade de numeros pares: {len(cont_pares)}")
print(f"Quantidade de numeros impares: {len(cont_impares)}")