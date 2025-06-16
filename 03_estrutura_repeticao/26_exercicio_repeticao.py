"""Exercício 26.

Simulação de Eleição
Faça um programa que peça o número total de eleitores e registre o voto de cada um em
três candidatos disponíveis, mostrando ao final o número de votos de cada candidato.
"""
total_eleitores = int(input("Informe o número total de eleitores: "))

candidado_1 = 0
candidato_2 = 0
candidado_3 = 0
for i in range(total_eleitores):
    voto = int(input(f"Eleitor {i + 1}, vote( 1, 2 ou 3 para os candidatos: )"))

    if voto == 1:
        candidado_1 += 1
    if voto == 2:
        candidato_2 += 1
    if voto == 3:
        candidado_3 += 1

else:
    print("Candidato invalido. ")

print(f"Votos do candidato 1: {candidado_1}.")
print(f"Votos do candidato 2: {candidato_2}.")
print(f"Votos do candidato 3: {candidado_3}.")
