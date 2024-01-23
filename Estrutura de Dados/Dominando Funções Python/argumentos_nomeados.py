def salvarCarros(modelo, ano):
    print(f"Carro inserido: {modelo}/{ano}")

salvarCarros(**{"modelo" : "Uno", "ano" : "1999"})
salvarCarros("Uno", "1990")
salvarCarros(modelo="Uno", ano="1997")