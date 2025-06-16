# """Exercício 01.
# Hello, World!
# Escreva um programa que exiba a mensagem "Hello, World!".
# print("Olá mundo!")

primeiro_valor = int(input("Digite o primeiro valor: "))
segundo_valor = int(input("Digite o segundo valor: "))

while segundo_valor <= primeiro_valor:
    segundo_valor = int(input("O segundo valor deve ser maior. Digite novamente: "))

soma = 0
for i in range(primeiro_valor, segundo_valor + 1):
    soma += i

print("A soma dos valores é:", soma)
