# """Exercício 06.
# Área do Círculo
# Desenvolva um programa que calcule e mostre a área de um círculo a partir do raio
# fornecido.
# Fórmulas:
#     a = π*r²
#     π ≈ 3.14
raio = float(input("Digite o seu raio: "))
pi = 3.14
soma = pi * raio**2
print(f"A sua area é de {soma:.2f}.")
