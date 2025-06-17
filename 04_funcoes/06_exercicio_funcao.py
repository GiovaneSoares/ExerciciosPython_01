"""Exercício 06.

Conversão de Hora
Faça um programa que converta a hora de notação de 24 horas para notação de 12 horas.
Por exemplo, deve converter 14:25 em 2:25 P.M.
Implemente funções para a conversão e para exibir o resultado.
Inclua um loop permitindo ao usuário repetir a operação com novos valores.
"""
def converter_hora(hora_24, minutos):
    if hora_24 < 12:
        am_pm = "A.M."
    else:
        am_pm = "P.M."

    if hora_24 not in {12, 0}:
        hora_12 = hora_24 % 12
    else:
        hora_12 = 12

    return f"{hora_12:02}:{minutos:02} {am_pm}"

def imprimir_hora_convertida(hora_24, minutos):
    print(converter_hora(hora_24=hora_24, minutos=minutos))

while True:
    hora_24 = int(input("Digite as horas (0 a 23)"))
    minutos = int(input("Digite os minutos (0 a 59)"))

    if not (0 <= hora_24 <= 23 and 0 <= minutos <= 59):
        print("Digite um horario valido!")
        continue

    imprimir_hora_convertida(hora_24, minutos)

    continuar = input("Deseja converter outro horario? (S/N): ").upper()
    if continuar != "S":
        break

    print("Fim do programa!")