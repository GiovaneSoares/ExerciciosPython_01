# palavra = "Python"
# primeiro_caractere = palavra[0:6:2] #[Começo:fim:passo]
# print(primeiro_caractere)

# palavra = "Python"
# primeiro_caractere = len(palavra) # Retorna a quantidade de letras em uma string
# print(primeiro_caractere)

# palavra = "Python"
# primeiro_caractere = palavra.replace("Python", "Java") # Susbstitui uma string por outra
# print(primeiro_caractere)

class Carro:
    def __init__(self, modelo: str, cor: str, ano: int, ligado: bool, nova_cor: str) -> None:
        self.modelo: str = modelo
        self.cor: str = cor
        self.ano: int = ano
        self.nova_cor: str = nova_cor
        self.ligado: bool = False

    def ligar_carro(self) -> None:
        if not self.ligado:
            print(f"Carro está sendo ligado!")
            self.ligado = True
        else:
            print(f"Carro já está ligado!")
    
    def informacoes_carro(self) -> None:
        print(f"Modelo: {self.modelo}\nCor: {self.cor}\nAno: {self.ano}")
    
    def andar(self):
        print(f"Carro: {self.modelo}, está andando!")
    
    def parar(self):
        print(f"Carro: {self.modelo}, parou!")
    
    def atualizar_cor(self, nova_cor) -> None:
        print(f"Nova cor do carro: {nova_cor}.")
        self.cor = nova_cor

uno_verde = Carro("Uno","Verde", 2011, False, "Azul")
uno_verde.ligar_carro()
uno_verde.andar()
uno_verde.parar()
uno_verde.ligar_carro()
uno_verde.atualizar_cor("preto")
uno_verde.informacoes_carro()
# uno_verde.informacoes_carro()
# uno_verde.andar()
# uno_verde.parar()