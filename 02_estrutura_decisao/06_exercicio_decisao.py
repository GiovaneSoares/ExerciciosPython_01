# """Exercício 06.
# Maior e Menor entre Três Números
# Faça um programa que leia três números e mostre qual é o maior e o menor entre eles.
# """
def menor_numero(numeros):
    return min(numeros)

def maior_numero(numeros):
    return max(numeros)

lista_numeros = [10, 5, 3, 8, 1, 99]
print("O menor número é:", menor_numero(lista_numeros))
print("E o maior número é:", maior_numero(lista_numeros))