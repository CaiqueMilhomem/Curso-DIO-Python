# antes da barra ("/") é por posição, após a barra é por nome. Como mostra no exemplo a seguir:


def criar_carro(modelo, ano, /, marca, combustivel):
    print(modelo, ano, marca, combustivel)

print(criar_carro("Sentra", 2008, marca="Nissan", combustivel="Gasolina")) 