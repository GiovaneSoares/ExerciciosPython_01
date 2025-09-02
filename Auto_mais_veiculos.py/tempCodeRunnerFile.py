class Carro:
    def __init__(self, marca: str, modelo: str, ano: int, placa: str, cor: str, valor: float) -> None:
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.placa = placa
        self.cor = cor
        self.valor = valor
    
    def cadastrar_carro(self):
        print("\n*** CARRO CADASTRADO ***\n")
        print(f"Marca: {self.marca}\nModelo: {self.modelo}\nAno: {self.ano}\nPlaca: {self.placa}\nCor: {self.cor}\nValor R$ {self.valor:,.2f}")

    def editar_dados(self, nova_marca: str, novo_modelo: str, novo_ano: int, nova_placa: str, nova_cor: str, novo_valor: float):
        print("\n*** DADOS ATUALIZADOS ***\n")
        self.marca = nova_marca
        self.modelo = novo_modelo
        self.ano = novo_ano
        self.placa = nova_placa
        self.cor = nova_cor
        self.valor = novo_valor 
        # Mantendo a consistência na formatação do valor
        print(f"Nova Marca: {self.marca}\nNovo Modelo: {self.modelo}\nNovo Ano: {self.ano}\nNova Placa: {self.placa}\nNova Cor: {self.cor}\nNovo Valor R$ {self.valor:,.2f}\n")

    def excluir_carro(self):
        print(f"*** DADOS DELETADOS ***")
        print(f"\n{self.marca} - {self.modelo}")

    def listar_carros_cadastrados(self):
        self.cadastrar_carro()

# Função que busca o carro na lista
def buscar_carro(lista_carros: list, buscar_placa: str):
    for carro in lista_carros:
        if carro.placa == buscar_placa:
            return carro
    return None

# --- Exemplo de Uso ---
# 1. Criação dos objetos
mercedes_g63 = Carro("Mercedes", "G63", 2026, "AST7674", "Prata", 565_000.00)
uno_verde = Carro("Fiat", "Uno", 2011, "AFO7674", "Verde", 25.00)

# 2. Criação de uma lista para armazenar os carros
lista_de_carros = [mercedes_g63, uno_verde]

# 3. Utilizando a função de busca
print("--- Buscando um carro existente ---")
carro_encontrado = buscar_carro(lista_de_carros, "AST7674")

if carro_encontrado:
    carro_encontrado.listar_carros_cadastrados()
else:
    print("Carro não encontrado.")

print("\n--- Buscando um carro que não existe ---")
carro_nao_encontrado = buscar_carro(lista_de_carros, "ABC1234")

if carro_nao_encontrado:
    carro_nao_encontrado.listar_carros_cadastrados()
else:
    print("Carro com a placa ABC1234 não encontrado.")
