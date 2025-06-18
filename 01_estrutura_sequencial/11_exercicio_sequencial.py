"""Exercício 11.
Manipulação Básica de Strings
Escreva um programa que:
    a. Solicite ao usuário que digite seu primeiro nome;
    b. Solicite ao usuário que digite seu sobrenome;
    c. Combine o primeiro nome e o sobrenome em uma única string, separados por um
        espaço, e mostre o nome completo;
    d. Conte e mostre o número de letras no nome completo (excluindo o espaço);
    e. Converta e mostre o nome completo em letras maiúsculas."""

nome = input("Digite seu primeiro nome: ").title()
sobrenome = input("Digite o sobrenome: ").title()
nome_completo = nome + " " + sobrenome
substituir = input("Digite um sobrone que deseja substituir pelo seu atual: ")
print(f"Bem vindo! {nome}.\n")

numero_de_letras = len(nome_completo.replace(" ", ""))
print(f"A quantidade de letras no seu nome é: {numero_de_letras}.\n")
print(f"Seu nome apresentado em caixa alta é: {nome_completo.upper()}.\n")
print(f"O seu nome apresentado em letras minusculas: {nome_completo.lower()}.\n")
print(f"Seu nome com as palavras capitalizadas: {nome_completo.title()}.\n")
print(
    f"O seu novo sobrenome agora é: {nome_completo.replace(f' {sobrenome}', ' 'f'{substituir}')}.\n"
)
