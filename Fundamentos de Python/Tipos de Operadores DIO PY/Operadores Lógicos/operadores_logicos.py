# AND para ser True todos tem que ser True.
# No OR apenas um sendo True já vai dar True. 


print(True and True)
print(True and False)
print(False and False)
print(True or True)
print(True or False)
print(False or False)


saldo = 1000
saque = 250
limite = 200
conta_especial = True

exp1 = saldo >= saque and saque <= limite or conta_especial >= saque
print(exp1)

exp2 = (saldo >= saque and saque <= limite) or (conta_especial >= saque)
print(exp2)

