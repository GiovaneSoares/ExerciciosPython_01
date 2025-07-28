"""Exercício 14.
Multa por Excesso de Pesca
Você foi contratado pela Secretaria de Meio Ambiente para criar um sistema que ajude na
fiscalização da pesca em reservas naturais.
De acordo com a legislação local, pescadores têm um limite de captura de 50 quilos de
peixes por dia para evitar a superexploração.
Para cada quilo excedente, é imposta uma multa de R$ 4,00.
Seu programa deve:
    a. Solicitar a quantidade total de peixes pescados (em quilos) por um pescador em
        um único dia;
    b. Calcular e exibir qualquer excesso de peso além do limite permitido de 50
        quilos;
    c. Se houver excesso, calcular e exibir o valor da multa que o pescador deve pagar."""

peso_peixes = float(input("Quantidade em kg dos peixes adquiridos na pesca: "))

excesso = peso_peixes - 50

multa = excesso * 4

if peso_peixes < 0:
    print("Número invalido, digite um valor maior que 0")

if peso_peixes >= 50:
    # print(f"Quantidade adquirada: {peso_peixes} Kg.")
    # print(f"Excesso de kg: {excesso}.")
    # print(f"Multa: R$ {multa}.")
    print(f"Ultrapassou a quantidade de permitida de 50 Kg! O excesso foi de {excesso:.2f} kg e a multa é de R$ {multa:.2f}.")

elif peso_peixes < 50 or peso_peixes == 0:
    print("Quantidade permitida! Não há excesso e nem multas a serem cobradas!")
