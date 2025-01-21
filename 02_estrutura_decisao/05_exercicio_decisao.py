# """Exercício 05.
# Avaliação do Aluno
# Implemente um programa que leia duas notas parciais de um aluno, calcule a média e
# exiba "Aprovado" se a média for maior ou igual a sete, "Reprovado" se for menor que
# sete, e "Aprovado com Distinção" se a média for igual a dez.
# """

nota1 = float(input("Digite a uma nota e veja sua média: "))
nota2 = float(input("Digite a uma nota e veja sua média: "))
nota3 = float(input("Digite a uma nota e veja sua média: "))
nota4 = float(input("Digite a uma nota e veja sua média: "))
media = (nota1 + nota2 + nota3 + nota4) / 4
print(media)

if media == 10.0:
    print("Aprovado com Distinção. Párabens!")

elif media >= 7.0:
    print(f"Aprovado!")

elif media < 7.0:
    print(f"Reprovado! Estude mais!")

print("Fim do programa!")
