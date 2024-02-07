class Veiculo: 
    def __init__(self, cor, placa, combustivel, numero_acentos):
        self.cor = cor
        self.placa = placa
        self.combustivel = combustivel
        self.nmr_rodas = numero_acentos

    def ligar_motor(self):
        print("ligando motor...")

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"


class Moto(Veiculo):
    pass

class Carro(Veiculo):
    pass

class Aviao(Veiculo):
    def __init__(self,cor, placa, combustivel, numero_acentos, carregado):
        self.carregado = carregado

        super().__init__(cor, placa, combustivel, numero_acentos)
    
    def esta_carregado(self):
        print(f"{'Sim,' if self.carregado else 'Não'} estou carregado")


moto1 = Moto("preta", "abc-1234", "alcool", 2)
carro1 = Carro("Cinza", "wer-9898", "gasolina", 4)
aviao1 = Aviao("Branco", "brl-0101", "etanol", 64, False)



print(aviao1)
print(carro1)
print(moto1)
