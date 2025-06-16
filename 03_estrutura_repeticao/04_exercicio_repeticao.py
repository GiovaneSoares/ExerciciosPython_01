"""Exercício 04.

Crescimento Populacional
Implemente um programa que calcule o tempo necessário para que a população do país A,
que possui 80.000 habitantes e cresce 3% ao ano, ultrapasse ou iguale a população do
país B, com 200.000 habitantes e crescimento anual de 1,5%.
"""
população_A = 80.000
taxa_cres_A = 0.03

população_B = 200.000
taxa_cres_B = 0.015

anos = 0

while população_A < população_B:
    população_A += população_A * taxa_cres_A
    população_B += população_B * taxa_cres_B
    anos += 1

print(f"A população do país A, levará {anos} anos para ultrapassar a população B.")