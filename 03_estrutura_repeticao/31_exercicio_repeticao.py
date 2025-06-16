"""Exercício 31.

Análise de Temperaturas
Desenvolva um programa que leia um conjunto indeterminado de temperaturas e informe a
menor, a maior e a média das temperaturas registradas.
"""
temperatura = []

while True:
    primeira_temperatura = float(input("Digite uma temperatura ou tecle '0' para finalizar: "))

    if primeira_temperatura == 0:
        break
    temperatura.append(float(primeira_temperatura))

menor_temperatura = min(temperatura)
maior_temperatura = max(temperatura)
media_temperatura = sum(temperatura) / len(temperatura)

print(f"\nMenor Temperatura: {menor_temperatura:.2f}°C\nMaior Temperatura: {maior_temperatura:.2f}°C\nMédia de Temperatura: {media_temperatura:.2f} °C")