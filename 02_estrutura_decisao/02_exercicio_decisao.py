# """Exercício 02.
# Avaliação de Valor
# Crie um programa que peça um número ao usuário e informe se este é positivo ou
# negativo.
nm = float(input("Digite um número: "))
if nm > 0:
    print(f"{nm} È positivo.")
elif nm < 0:
    print(f"{nm} È negativo.")
else: 
    print(f"{nm} È igual a 0.")
