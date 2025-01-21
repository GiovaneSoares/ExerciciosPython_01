# """Exercício 09.
# Conversão de Fahrenheit para Celsius
# Faça um programa que converta uma temperatura dada em Fahrenheit para Celsius.
# Fórmula:
#     C = (F - 32) / 1.8
temperatura = float(input("Digite a temperatura em Fahrenheit: "))
print(
    f"A temperatura de { temperatura} ºF convertida para Celsius é de {(temperatura - 32) / 1.8 :.1f} ºC."
)
