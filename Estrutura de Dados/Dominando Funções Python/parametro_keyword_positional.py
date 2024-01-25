# neste caso tem como deixar um parametro opcional, no exemplo MARCA é opcional.


def criar_carro(modelo, ano, /, marca, *,combustivel):
    print(modelo, ano, marca, combustivel)

print(criar_carro("Sentra", 2008, "Nissan", combustivel="Gasolina")) 