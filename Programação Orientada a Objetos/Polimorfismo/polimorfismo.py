class Veiculo: 
    def barulho(self):
        print("Vrum")

class Carro(Veiculo):
    def barulho(self):
        super().barulho()

class Bicicleta(Veiculo):
    def barulho(self):
        print("Bicicleta não faz barulho")

def barulho_motor(veiculo):
    veiculo.barulho()

barulho_motor(Bicicleta())
barulho_motor(Carro())


