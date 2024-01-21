# diferença de tupla para lista é que as tuplas são imutaveis. 
# ou então, você utiliza a tupla quando quer ter um valor que é inalterável


frutas = ("Laranja","Limão","Maça",)

letras = tuple("Python")

numeros = tuple([1, 3, 5, 7])

pais = ("Brasil",)

# print(frutas[2])
# print(frutas[-2])

matriz = (
    ("a", 3, 7),
    (3, "q", "f"),
    (9, "g", "l"),
)

print(matriz[1][1]) #q
print(matriz[2][0]) #9