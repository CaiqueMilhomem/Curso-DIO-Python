def calcula_total(numero):
    return sum(numero)


def antecessor_sucessor(numero):
    
    antecessor = numero - 1 
    sucessor = numero + 1
    return antecessor, sucessor


print(calcula_total([10,20,40]))
print(antecessor_sucessor(11))