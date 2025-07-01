"""Exercício 10.

Aumento Salarial
Implemente um programa que calcule o reajuste salarial dos colaboradores de uma
organização conforme a seguinte tabela de critérios, baseando-se no salário atual:
    a. Salários até R$ 280,00 (inclusive): Aumento de 20%
    b. Salários até R$ 700,00 (inclusive): Aumento de 15%
    c. Salários até R$ 1500,00 (inclusive): Aumento de 10%
    d. Salários acima de R$ 1500,00: Aumento de 5%
O programa deve exibir o salário antes do reajuste, o percentual aplicado, o valor do
aumento e o novo salário.
"""
salario_atual = float(input("Digite o valor do salario atual R$: "))

if salario_atual > 0 and salario_atual <= 280:
    aumento = salario_atual * 0.2
    novo_salario = salario_atual + aumento
    print(
        f"O salario atual de R${salario_atual:.2f} com o novo reajuste passa a ser de R${novo_salario:.2f}."
    )

if salario_atual > 280 and salario_atual <= 700:
    aumento = salario_atual * 0.15
    novo_salario = salario_atual + aumento
    print(
        f"O salario atual de R${salario_atual:.2f} com o novo reajuste passa a ser de R${novo_salario:.2f}."
    )

if salario_atual > 700 and salario_atual <= 1500:
    aumento = salario_atual * 0.1
    novo_salario = salario_atual + aumento
    print(
        f"O salario atual de R${salario_atual:.2f} com o novo reajuste passa a ser de R${novo_salario:.2f}."
    )

elif salario_atual > 1500:
    aumento = salario_atual * 0.05
    novo_salario = salario_atual + aumento
    print(
        f"O salario atual de R${salario_atual:.2f} com o novo reajuste passa a ser de R${novo_salario:.2f}."
    )