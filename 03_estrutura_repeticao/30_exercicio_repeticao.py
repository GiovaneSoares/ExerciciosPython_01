"""Exercício 30.

Caixa Registradora Simples
Elabore um programa que simule uma caixa registradora em uma loja, registrando os
preços das mercadorias e calculando o total da compra e o troco a partir do valor
fornecido pelo cliente.
    ------ Venda ------
    Produto 1: R$ 2.20
    Produto 2: R$ 5.80
    Produto 3: R$ 0
    Total: R$ 9.00
    Dinheiro: R$ 20.00
    Troco: R$ 11.00
"""
total_compra = 0
item = 1

while True:
    preco_produto = float(input(f"Produto {item}: R$  ").replace(",", "."))
    if preco_produto == 0:
        break

    total_compra += preco_produto
    item += 1

print(f"Total R$ {total_compra:.2f}")

valor_pago = float(input("Dinheiro R$ ").replace(",", "."))

while valor_pago < total_compra:
    print(f"Valor insuficiente!")
    valor_pago = float(input("Dinheiro R$ ").replace(",", "."))

troco = valor_pago - total_compra

print(f"Troco: R$ {troco:.2f}")