# """Exercício 25.
# Atualização de Lista de Cores
# Desenvolva um programa que comece com uma lista contendo cinco cores distintas.
# O programa deve então solicitar ao usuário uma cor.
# Esta cor fornecida pelo usuário será utilizada para substituir a terceira cor na lista
# original.
# Após a substituição, o programa deve exibir a lista atualizada, mostrando a alteração
# feita.
cores = ["Azul", "branca", "rosa", "pink", "laranja"]
adicionar = input("Digite a cor que deseja adicionar na lista: ")
cores[2] = adicionar
print(cores)