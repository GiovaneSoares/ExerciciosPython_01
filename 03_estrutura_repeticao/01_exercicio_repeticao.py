"""Exercício 01.

Validador de Notas
Elabore um programa que solicite uma nota numérica entre zero e dez ao usuário.
Caso o valor fornecido esteja fora do intervalo permitido, o programa deve exibir uma
mensagem de erro e solicitar o valor novamente até que uma entrada válida seja
fornecida.
"""
nota = float(input("Digite uma nota númerica entre zero e dez: "))

if nota >= 0 and nota <= 10:
    print(f"O numero {nota} é valido.")

else:
    print(f"O numero {nota} não é valido.")
