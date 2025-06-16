"""Exercício 24.

Média Aritmética de Notas
Implemente um programa que calcule e mostre a média aritmética de N notas fornecidas
pelo usuário.
"""
quantidade_notas = int(input("Digite a quantidade de notas a serem inseridas: "))
notas = []

for n in range(quantidade_notas):
    nota = float(input(f"Informe a {n + 1}ª nota: "))
    notas.append(nota)

media = sum(notas) / len(notas)

print(f"A sua média aritmetica é {media:.2f} ")

