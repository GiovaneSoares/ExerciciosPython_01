"""Exercício 03.

Validação de Dados de Cadastro
Crie um programa que efetue a leitura e validação dos seguintes dados de cadastro:
    a. Nome: deve conter mais de 2 caracteres;
    b. Idade: deve estar entre 0 e 150 anos;
    c. Salário: deve ser superior a zero;
    d. Sexo: deve ser "F" ou "M";
    e. Estado civil: deve ser "S", "C", "V", "D".
Cada dado deve ser validado conforme suas respectivas regras.
"""
# nome = str(input("Digite o seu nome: "))
# idade = int(input("Qual a sua idade? "))
# salario = float(input(("Digite o seu salário: ")))
# sexo = str(input("Digite o seu gênero. (Masc/Femi): "))
# estado_civil = str(input("Qual seu estado civil. (Solteiro/Casado/Viuvo/Divorciado): "))

# print("\nValidações de dados recebidos:\n ")

# if len(nome) > 2:
#     print("NOME: Valido.")
# else:
#     print("Nome: Não é valido.")

# if idade >= 0 and idade <= 150:
#     print("IDADE: valido.")
# else:
#     print("Idade: não é valida.")

# if salario > 0:
#     print("SALÁRIO: Valido.")
# else:
#     print("Sálario: não é valido.")

# if sexo == "Feminino" or sexo == "Masculino":
#     print("SEXO: Valido.")
# else:
#     print("Sexo: Não é valido.")

# if estado_civil == "Solteiro" or estado_civil == "Casado" or estado_civil == "Viuvo" or estado_civil == "Divorciado":
#     print("ESTADO CIVIL: Valido.")
# else:
#     print("Estado Civil: Não é valido.")

nome = str(input("Digite o seu nome: "))
while len(nome) < 3:
    print("A quantidade de letras para compor um nome, foi menor que 2. Tente novamente! ")
    nome = str(input("Digite o seu nome: "))

idade = int(input("Qual a sua idade? "))
while idade <= 0 or idade > 150:
    print("A idade deve ser maior que 0 e menor que 150.")
    idade = int(input("Qual a sua idade? "))

salario = float(input(("Digite o seu salário: ")))
while salario < 0:
    print("O seu salario não pode ser menor que zero.")
    salario = float(input(("Digite o seu salário: ")))

sexo = str(input("Digite o seu gênero. (Masculino/Feminino): "))
while sexo not in {"Masculino","Feminino"}:
    print("Genero não é valido. ")
    sexo = str(input("Digite o seu gênero. (Masculino/Feminino): "))

estado_civil = str(input("Qual seu estado civil. (Solteiro/Casado/Viuvo/Divorciado): "))
while estado_civil not in {"Solteiro", "Casado", "Viuvo", "Divorciado"}:
    print("Estado Civil não é valido.")
    estado_civil = str(input("Qual seu estado civil. (Solteiro/Casado/Viuvo/Divorciado): "))