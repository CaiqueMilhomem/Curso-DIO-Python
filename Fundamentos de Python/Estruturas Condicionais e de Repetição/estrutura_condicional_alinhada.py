conta_normal = False
conta_universitaria = False

saldo = 1000
saque = 1500
cheque_especial = 450

if conta_normal:
    if saldo >= saque:
        print("Realizando Saque")

    elif saque <= (saldo + cheque_especial):
        print("Saque realizado com o cheque especial.")

    else: 
        print("Não foi realizado o saque, saldo insuficiente.")

elif conta_universitaria:
    if saldo >= saque:
        print("Saque realizado com sucesso.")
    
    else:
        print("Saldo insuficiente.")

else:
    print("O Sistema não reconheceu o seu tipo de conta, tente entrar novamente.")