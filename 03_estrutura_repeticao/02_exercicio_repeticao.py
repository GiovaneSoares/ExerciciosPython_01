"""Exercício 02.

Cadastro de Usuário e Senha
Desenvolva um programa que receba um nome de usuário e sua senha.
O sistema deve validar se a senha é diferente do nome do usuário.
Caso seja igual, uma mensagem de erro deve ser exibida e as informações solicitadas
novamente até que sejam válidas.
"""

# usuario = str(input("Cadastre um nome para seu login: "))
# senha = str(input("Digite a sua nova senha: "))
# passaword = str(input("Digite novamente para validação de sua senha: "))

# if senha != passaword:
#     print("A senha digitada está divergente da informada acima. Tente novamente! ")
#     senha = str(input("Digite a sua nova senha: "))
#     passaword = str(input("Digite novamente para validação de sua senha: "))
#     if senha == passaword:
#         print("Senha validade com sucesso. ")


# elif senha == passaword:
#     print("Senha validada com sucesso. ")
#     print(20 * "*")

# login = str(input("Digite seu login: "))
# verificacao = str(input("Digite sua senha: "))

# if usuario == login and senha == verificacao:
#     print("Usuario e senha autentificado. ")

# else:
#     print("Usuario ou senha invalidos. Tente novamente! ")
#     login = str(input("Digite seu login: "))
#     verificacao = str(input("Digite sua senha: "))
# ***********************************************************************
usuario = str(input("Cadastre um nome para seu login: "))
senha = str(input("Digite a sua nova senha: "))

while usuario == senha:
    print("ERRO: A sua senha não pode ser igual ao login")
    senha = str(input("Digite uma nova senha: "))

print(f"Login efetuado com sucesso.\nBem vindo {usuario}!")
