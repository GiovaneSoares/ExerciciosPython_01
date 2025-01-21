"""Exercício 08.

Cálculo de Salário
Elabore um programa que calcule o salário mensal de uma pessoa, com base nas horas
trabalhadas por mês e no valor por hora.
"""

valor_hora = float(input("Digite o valor que voce ganha por hora: "))
hora_mes = float(input("Qual a quantidade de horas trabalhadas durante a semana: "))
print(f"O seu salario no referido mes é de R$ {valor_hora * hora_mes}!")
