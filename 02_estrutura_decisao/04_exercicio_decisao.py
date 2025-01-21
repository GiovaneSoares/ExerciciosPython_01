# """Exercício 04.
# Classificação de Letras
# Elabore um programa que solicite uma letra ao usuário e verifique se ela é uma vogal ou
# consoante.
vogal = ["A", "E", "I" , "O" , "U"]
letras = input("Digite uma letra do alfabeto de 'A' até 'Z' e veja se ela é vogal ou consoante: ").upper()
if len(letras) == 1 and letras.isalpha():
    if letras in vogal:
        print(f"'{letras}' é um vogal.")
    elif letras not in vogal:
        print(f"{letras} é uma consoante.")
else:
    print("Isso não é uma letra.")
    print("Digite uma letra do alfabeto de 'A' até 'Z' e veja se ela é vogal ou consoante: ")
