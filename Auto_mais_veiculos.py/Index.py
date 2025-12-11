class Carro:
    def __init__(self, marca: str, modelo: str, ano: int, placa: str, cor: str, valor: float, ) -> None:
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.placa = placa
        self.cor = cor
        self.valor = valor
    
    def cadastrar_carro(self):
        print("\n*** REGISTERED CAR ***\n")
        print(f"Marca: {self.marca}\nModelo: {self.modelo}\nAno: {self.ano}\nPlaca: {self.placa}\nCor: {self.cor}\nValor R$ {self.valor:.2f}")

    def editar_dados(self, nova_marca: str, novo_modelo: str, novo_ano: int, nova_placa: str, nova_cor: str, novo_valor: float):
        print("\n*** UPDATE CAR ***\n")
        self.marca = nova_marca
        self.modelo = novo_modelo
        self.ano = novo_ano
        self.placa = nova_placa
        self.cor = nova_cor
        self.valor = novo_valor 
        # self.cadastrar_carro()
        print(f"Nova Marca: {self.marca}\nNovo Modelo: {novo_modelo}\nNovo_ano: {novo_ano}\nNova Placa: {nova_placa}\nNova Cor: {nova_cor}\nNovo Valor R$ {novo_valor:.3f}\n")

    def excluir_carro(self):
        print(f"*** DELETED DATA ***")
        print(f"\n{self.marca} - {self.modelo}")

    def listar_carros_cadastrados(self):
        self.cadastrar_carro()
        # print(f"{self.cadastrar_carro()}")

def buscar_carro(lista_carros: list, buscar_placa: str):
    # for carro in lista_carros:
    #     if carro.placa == buscar_placa:
    #         return carro
    #         # print(f"{carro}")
    # return None

Mercedes_G63 = Carro("Mercedes", "G63", 2026, "AST7674", "Prata", 565_000.0)
uno_verde = Carro("Fiat", "Uno", 2011, "AFO7674", "Verde", 25.00)


# # --- FUNÇÃO CRIADA PARA PROCURAR CARRO POR PLACA --- 
# lista_de_carros = [Mercedes_G63, uno_verde]
# carro_encontrado = buscar_carro(lista_de_carros, "AST7674")
# if carro_encontrado:
#     print("carro_encontrado")
#     carro_encontrado.cadastrar_carro()
# else:  
#     print(f"Placa não encontrada!")

# uno_verde.excluir_carro() #comando para excluir um carro. 