# """Exercício 03.
# Identificação de Gênero
# Desenvolva um programa que peça ao usuário para digitar "F" para feminino ou "M" para
# masculino.
# O programa deve exibir "Feminino" para "F", "Masculino" para "M", ou "Sexo inválido"
# para qualquer outra entrada.

genero = input("Digite 'F' para feminino e 'M' para masculino: ").upper()
if genero == "F":
    print("Feminino!")
elif genero == "M":
    print("Masculino!")
else:
    print("ERRO: tente novamente. Digite 'F' para feminino e 'M' para masculino. ")