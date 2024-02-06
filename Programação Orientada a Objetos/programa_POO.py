
class Bicicleta: 
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

    def buzinar(self):
        print("Biii Bii...")

    def parar(self):
        print("Parando bicicleta...")
        print("Bicicleta parada.")

    def correr(self): 
        print("Correndo")


b1 = Bicicleta("Preto", "Caloi", "2013", "2.000 R$")

b1.buzinar()
b1.correr()
b1.parar()

print(b1.cor)