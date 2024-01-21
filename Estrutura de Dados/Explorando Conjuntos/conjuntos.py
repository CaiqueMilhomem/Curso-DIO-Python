# set elimina registros duplicados
# set pode ser utilizado com parenteses e a palavra set ou com {}.

set([1, 1, 2, 3, 4, 5, 5]) # {1,2,3,4,5}

print(set("abacaxi")) #{"b", "i", "x", "c", "a"} sequência aleatória

frutas = set(("abacaxi", "limão", "limão", "uva"))

print(frutas)

#####################################################################################

# convertendo o set para lista, para acessar o valor [0]

numeros = {1, 2, 3, 2}

numeros = list(numeros)

print(numeros[0])




