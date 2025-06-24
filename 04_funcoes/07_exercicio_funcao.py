"""Exercício 07.

Cálculo de Pagamento de Prestação
Desenvolva um programa que utilize a função "valor_pagamento" para determinar o valor a
ser pago por uma prestação de uma conta.
A função deve receber o valor da prestação e o número de dias em atraso, calcular o
valor a ser pago e retorná-lo ao programa principal, que exibirá este valor.
O cálculo do valor a ser pago é feito da seguinte forma:
    a. Para pagamentos sem atraso, cobrar o valor da prestação;
    b. Quando houver atraso, cobrar 3% de multa, mais 0,1% de juros por dia de atraso.
O programa deve continuar solicitando novos valores até que uma prestação informada
seja zero, encerrando o programa e exibindo o relatório do dia com a quantidade e o
valor total de prestações pagas.
"""

def valor_pagamento(valor_prestacao, dias_atrasado):
    if dias_atrasado > 0:
        multa = valor_prestacao * 0.03
        juros = dias_atrasado * 0.001 * valor_prestacao

        return valor_prestacao + multa + juros
    return valor_prestacao

total_prestacao = 0
valor_total_pago = 0

while True:
    valor_prestacao = int(input("Informe o valor da prestação. (ou 0 para sair): "))

    if valor_prestacao == 0:
        break

dias_atraso = int(input("Informe os número de dias em atrasos "))

valor_a_pagar = valor_pagamento(valor_prestacao, dias_atraso)

print(f"Valor a pagar R${valor_a_pagar:.2f}")

total_prestacao += 1
valor_total_pago += valor_a_pagar

print(f"    Relatorio do dia: ")
print(f"Total das prestações: R${total_prestacao}")
print(f"Valor total pago: R${valor_total_pago:.2f}")
