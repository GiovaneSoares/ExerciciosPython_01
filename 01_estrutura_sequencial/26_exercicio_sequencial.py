# """Exercício 26.
# Concatenação de Caracteres
# Faça um programa que contenha uma lista com os nomes "Ana", "Bia", "Cris", "Bob", e
# "Eva".
# O programa deve gerar uma string que seja a concatenação dos três primeiros caracteres
# de cada nome, na ordem inversa da lista.
# Ao final, exiba a string resultante.
nomes = ["Ana", "Bia", "Cris", "Bob", "Eva"]

string_concatenada = ( nomes[4][:3] + nomes[3][:3] + nomes[2][:3] + nomes[1][:3] + nomes[0][:3] )

print(string_concatenada)