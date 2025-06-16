"""Exercício 27.

Média de Alunos por Turma
Crie um programa que solicite a quantidade de turmas e a quantidade de alunos para cada
turma, calculando a média de alunos por turma. Note que cada turma não pode ter mais de
40 alunos.
"""
quantidade_turmas = int(input("Qual a quantidade de turmas? "))

total_de_alunos = 0

for a in range(quantidade_turmas):
    while True:
        alunos = int(input(f"Informe a quantidade de alunos na {a + 1}ª turma."))
        if 1 <= alunos <= 40:
            total_de_alunos += alunos
            break
        else: 
            print("Numero de alunos inválidos. Tente novamente.")

media_alunos = total_de_alunos / quantidade_turmas

print(f"A média de alunos por turma é {media_alunos:.2f}.")