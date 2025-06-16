"""Exercício 13.

Peso Ideal
Desenvolva um programa que calcule o peso ideal de uma pessoa, usando fórmulas
específicas para homens e mulheres.
Fórmulas:
    Homens: (72.7 * h) - 58
    Mulheres: (62.1 * h) - 44.7
"""
genero = input("Qual genero voce se identifica? Ex (Homem/Mulher): ").upper()
if genero == "HOMEM":
    altura_homem =  float(input("Homem: Digite a sua altura e veja o seu peso ideial: "))
    peso_homem = (72.7 * altura_homem) - 58
    print(f"O Peso ideal para {altura_homem} metros é de {peso_homem:.2f} kg. ")

elif genero == "MULHER":
    altura_mulher = float(input("Mulher: Digite a sua altura e veja o seu peso ideal "))
    peso_mulher = (62.1 * altura_mulher) - 44.7
    print(f"O Peso ideal para {altura_mulher} metros é de {peso_mulher:.2f} kg. ")
