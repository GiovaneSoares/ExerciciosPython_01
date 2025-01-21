# """Exercício 33.
# Verificação de Chave em Dicionário
# Crie um programa que possua um dicionário com as informações "Nome": "Ana", "Idade":
# 25, "Profissão": "Engenheira", e "País": "Brasil".
# O programa deve verificar se a chave "Idade" está presente no dicionário e exibir uma
# mensagem confirmando sua presença.

dicionario = {"Nome": "Ana", "Idade": "25", "Profissão": "Engenheira", "País": "Brasil"}
if "Idade" in dicionario:
    print(f"sim, existe a chave 'idade' em dicionario")
else:
    print("lamento, não tem essa chave.")
