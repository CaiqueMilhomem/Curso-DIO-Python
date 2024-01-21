numeros = [1, 2, 4, 65, 37, 85, 88, 92, 42, 82, 87]
pares = []
quadrado = []
for numero in numeros: 
    if numero % 2 == 0:
        pares.append(numero)
        print(pares)


for numero in numeros: 
    quadrado.append(numero**2)
    print(quadrado)

