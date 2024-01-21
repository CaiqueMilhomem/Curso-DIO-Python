def sacar(valor):
    saldo = 500

    if saldo >= valor:
        print("valor sacado!")    
    
sacar(100)

def deposito(valor):
    saldo = 500
    saldo += valor
    print(saldo)

deposito(500)    