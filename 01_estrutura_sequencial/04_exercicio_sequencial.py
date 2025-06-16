# """Exercício 04.
# Média das Notas
# Faça um programa que peça quatro notas bimestrais e apresente a média delas.

nota_1 = float(input("Digite a primeira nota: "))
nota_2 = float(input("Digite a segunda nota: "))
nota_3 = float(input("Digite a terceira nota: "))
nota_4 = float(input("Digite a quarta nota: "))

media = float(nota_1 + nota_2 + nota_3 + nota_4) / 4

print(f"A média das notas apresentadas é de {media:.2f}\n")

if media > 10:
    print("MÉDIA INVÁLIDA! Os valores devem estár entre 0 - 10.")

if media == 10:
    print("APROVADO! Com distinção.")

elif media >= 7 and media < 10:
    print("APROVADO! Voce atingiu a médía.")

elif media >= 0 and media < 7:
    print("REPROVADO! Voce não atingiu a média, estude mais.")
