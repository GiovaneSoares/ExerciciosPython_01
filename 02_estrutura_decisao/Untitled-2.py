# """Exercício 01.
# Maior entre Dois Números
# Escreva um programa que solicite ao usuário dois números e exiba o maior entre eles.
nm1 = float(input("Digite o primeiro número: "))
nm2 = float(input("Digite o segundo número: "))
if nm1 > nm2:
    print(f"O numero {nm1} é maior.")

elif nm1 == nm2:
    print(f" Ambos valores são iguais.")

else:
    print(f"{nm2} é maior.")
