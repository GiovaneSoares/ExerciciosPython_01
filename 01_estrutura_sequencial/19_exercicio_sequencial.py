"""Exercício 19.

Manipulação de Lista de Frutas
Desenvolva um programa que comece criando uma lista contendo cinco nomes de frutas.
Em seguida, o programa deve solicitar ao usuário o nome de uma sexta fruta, que será
adicionada ao final da lista.
Após a adição, o programa deve remover a segunda fruta da lista original.
Finalmente, exiba a lista modificada ao usuário, demonstrando as alterações feitas.
"""

frutas = ["maça", "banana", "cereja", "morango", "jaca"]
print(f"lista de frutas {frutas}")
adicionar = input("Digite o que deseja adicionar: ")
frutas.append(adicionar)
frutas.pop(2)
print(frutas)
