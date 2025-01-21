# """Exercício 03.
# Soma de Dois Números
# Desenvolva um programa que solicite dois números ao usuário e mostre o resultado da soma
# desses números.

numeros = []
numeros.append(int(input("Digite o primeiro numero para adicionar a lista: ")))
numeros.append(int(input("Digite o segundo numero para adicionar a lista: ")))
soma = numeros[0] + numeros[1]
print(f"A soma dos numeros informados é de {soma}.")
