"""Exercício 08.

Contagem de Dígitos
Elabore uma função que informe a quantidade de dígitos de um determinado número inteiro
informado.
A função deve aceitar um número inteiro como argumento e retornar quantos dígitos esse
número possui.
"""
def quantidade(numero):
    return len(str(abs(numero)))

print(quantidade( 25))