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
        print(f"Marca: {self.marca}\nModelo: {self.modelo}\nAno: {self.ano}\nPlaca: {self.placa}\nCor: {self.cor}\nValor R$ {self.valor:.3f}")

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
        print(f"{self.cadastrar_carro()}")

    def buscar_carro(self,):
        pass

Mercedes_G63 = Carro("Mercedes", "G63", 2026, "AST7674", "Prata", 565.000)
uno_verde = Carro("Fiat", "Uno", 2011, "AFO7674", "Verde", 25.00)
uno_verde.listar_carros_cadastrados()
Mercedes_G63.listar_carros_cadastrados()






