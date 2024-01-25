# neste exemplo KEYWORD ONLY o asteristico significa que todos os argumentos tem de ser passados por nome e não por posição.

def criar_carro(*,modelo, ano, marca, combustivel):
    print(modelo, ano, marca, combustivel)

print(criar_carro(modelo="Sentra", ano=2008, marca="Nissan", combustivel="Gasolina")) 