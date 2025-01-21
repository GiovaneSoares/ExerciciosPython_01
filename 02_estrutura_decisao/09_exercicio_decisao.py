"""Exercício 09.

Saudações conforme o Turno
Crie um programa que questione ao usuário em que turno estuda, aceitando "M" para
Matutino, "V" para Vespertino ou "N" para Noturno.
O programa deve cumprimentar o usuário com "Bom dia!", "Boa tarde!" ou "Boa noite!",
respectivamente.
Para qualquer outra entrada, deve-se exibir "Valor inválido!".
"""
nome = input("Qual é o seu nome? ")
turno = input("Qual é o seu turno 'M', 'V' ou 'N'?").upper()

if turno == 'M':
    print(f"Bom dia, {nome}!")

elif turno == 'V' :
    print(f"Boa tarde, {nome}!")

elif turno == 'N':
    print(f'Boa noite, {nome}!')

else:
    print(f"{nome}, opção invalida! Digite entre 'M', 'V' ou 'N'.")
