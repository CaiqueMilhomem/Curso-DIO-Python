# construtor = __init__         destrutor = __del__

class Cachorro:
    def __init__(self, nome, cor, acordado=True):
        print("Inicializando classe...")
        self.nome = nome
        self.cor = cor
        self.acordado = acordado

    def falar(self):
        print("Latindo...")


    def __del__(self):
        print("Removendo a instância da classe...")

c = Cachorro("Thor", "Caramelo", True)

c.falar()
