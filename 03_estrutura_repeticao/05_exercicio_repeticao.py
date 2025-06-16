"""Exercício 05.

Simulador de Crescimento Populacional Personalizado
Modifique o programa anterior para permitir que o usuário defina as populações iniciais
e as taxas de crescimento de ambos os países.
O programa deve validar as entradas e permitir a repetição da operação.
"""
população_A = float(input("Digite a quantidade da população do país: "))
taxa_cres_A = float(input("Qual a taxa de crescimento da população do país? "))

população_B = float(input("Digite a quantidade da população do país: "))
taxa_cres_B = float(input("Qual a taxa de crescimento da população do país? "))

anos = 0

while população_A < população_B:
    população_A += população_A * taxa_cres_A
    população_B += população_B * taxa_cres_B
    anos += 1

print(f"A população do país A, levará {anos} anos para ultrapassar a população B.")