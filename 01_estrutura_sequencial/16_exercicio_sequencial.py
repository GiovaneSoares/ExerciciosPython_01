"""Exercício 16.

Loja de Tintas
Faça um programa para uma loja de tintas.
O programa deve solicitar o tamanho em metros quadrados da área a ser pintada.
Considere que cada litro de tinta cobre uma área de 7 metros quadrados e que a tinta é
vendida em latas de 18 litros, custando R$ 570,00 cada.
Informe ao usuário a quantidade de latas de tinta a serem compradas e o preço total.
"""

import math

COBERTURA_TINTA = 7  # Metros quadrados cobertos por litros de tinta
LATA_LITRO = 18  # litros por lata
LATA_PRECO = 570  # preço da lata de tinta de 18 litros

area = float(input("Digite o comprimento da área a ser pintada (m²): "))

litros_necessarios = area / COBERTURA_TINTA
latas_necessarias = math.ceil(litros_necessarios / LATA_LITRO)
preco_total = latas_necessarias * LATA_PRECO

print(
    f"A quantidade de latas necessarias para pintar {area}m² é de {latas_necessarias} latas."
)
print(
    f"Preço total de latas de tintas a serem utilizadas para pintar {area}m² é R$ {preco_total:.2f}."
)
