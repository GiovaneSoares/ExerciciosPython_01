""" Exercício 16.

Utilizando tratamento de exceções, crie um programa que, dado um valor inteiro informado pelo usuário, retorne a divisão de 1 por este. Se o valor informado for zero, o programa deve informar "Infinito" como resultado. Caso o valor informado não seja um número, o programa deve informar o usuário e continuar solicitando valores até que este seja."""

while True:
    try:
        numero = int(input("Digite um número inteiro: "))
        divisao: float = 1 / numero
    except ValueError:
        print("Informe um número inteiro.") 
    except ZeroDivisionError:
        print("Infinito")
        break
    else:
        print(f"O resultado {divisao}. ")
        break