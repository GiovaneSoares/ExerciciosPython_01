# """Exercício 32.
# Atualização de Profissão em Dicionário
# Escreva um programa que comece com um dicionário contendo "Nome": "Ana", "Idade": 25,
# "Profissão": "Engenheira", e "País": "Brasil".
# O programa deve atualizar a profissão de "Engenheira" para "Engenheira de Software" e
# exibir o dicionário modificado.
identidade = {"Nome": "Ana", "Idade": "25", "Profissão": "Engenheira", "País": "Brasil"}
#identidade["Profissão"] = "Engenheira de Software"
identidade.update({"Profissão": "Engenheira de Software"})
print(identidade)